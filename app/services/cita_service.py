from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import aiosmtplib
from email.message import EmailMessage
from datetime import datetime, timedelta
import os
from pytz import timezone
from ..models.schemas import Cita
import asyncio

SEGUNDOS_POR_HORA = 3600
TIEMPO_ANTES_ENVIO_EN_HORAS = 24

# Inicializamos el scheduler
scheduler = BackgroundScheduler()
scheduler.start()
identifier = 0

async def schedule_email(cita: Cita):
    global identifier

    fecha_cita = cita.fecha_inicio
    fecha_cita_date = datetime.strptime(fecha_cita, "%Y-%m-%d %H:%M:%S")

    hora_actual = datetime.now()

    time_difference = fecha_cita_date - hora_actual
    horas_para_cita = time_difference.total_seconds() / SEGUNDOS_POR_HORA

    if horas_para_cita <= 0:
        raise ValueError("La fecha de la cita ya pasó, no se puede programar el envío del correo.")

    job_id = f"send_email_{hora_actual.timestamp()}_{identifier}"  # ID único basado en timestamp y ID de la cita
    identifier += 1
    # Se genera contenido del mail
    msg = EmailMessage()
    msg["From"] = os.getenv("SMTP_USER")
    msg["To"] = "ctomasalvarezn@gmail.com"
    msg["Subject"] = "Recordatorio de su cita"
    msg.set_content("Estimado paciente, este es un recordatorio de su cita programada para el {fecha_cita}".format(fecha_cita=fecha_cita))

    if horas_para_cita < TIEMPO_ANTES_ENVIO_EN_HORAS:
        await send(msg)
    else:
        fecha_envio_mail = fecha_cita_date - timedelta(days=1)
        programar_email(msg, fecha_envio_mail, job_id)


async def send(msg: EmailMessage):
    try:
        await aiosmtplib.send(
            msg,
            hostname=os.getenv("SMTP_HOST"),
            port=int(os.getenv("SMTP_PORT")),
            username=os.getenv("SMTP_USER"),
            password=os.getenv("SMTP_PASSWORD"),
            start_tls=True
        )
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


def send_wrapper(msg: EmailMessage):
    asyncio.run(send(msg))


def programar_email(msg: EmailMessage, fecha_envio_mail, job_id: str):
    minute = fecha_envio_mail.minute
    hora = fecha_envio_mail.hour
    dia = fecha_envio_mail.day
    mes = fecha_envio_mail.month

    print(f"Programando email para el: {dia}/{mes} a las {hora}:{minute}")

    trigger = CronTrigger(
        hour=hora,
        minute=minute,
        day=dia,
        month=mes,
        timezone=timezone("America/Santiago")
    )
    scheduler.add_job(send_wrapper, trigger, id=job_id, args=[msg])