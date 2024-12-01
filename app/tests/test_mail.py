from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import aiosmtplib
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Inicializamos el scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Endpoint que programa el envío del correo
@app.post("/schedule-email")
async def schedule_email():
    job_id = f"send_email_{datetime.now().timestamp()}"  # ID único basado en timestamp
    hour = 4
    minute = 21
    def send_email():
        msg = EmailMessage()
        msg["From"] = os.getenv("SMTP_USER")
        msg["To"] = "mailprueba_reemplazame@gmail.com"
        msg["Subject"] = "prueba"
        msg.set_content("aqui hay algo de mailsdansdkjna")

        # Configura los parámetros del servidor SMTP
        async def send():
            await aiosmtplib.send(
                msg,
                hostname=os.getenv("SMTP_HOST"),
                port=int(os.getenv("SMTP_PORT")),
                username=os.getenv("SMTP_USER"),
                password=os.getenv("SMTP_PASSWORD"),
                start_tls=True
            )

        # Ejecuta la tarea de manera asincrónica
        import asyncio
        asyncio.run(send())

    from pytz import timezone
    # Programamos el envío del correo para la hora y minuto especificados
    trigger = CronTrigger(hour=hour, minute=minute, timezone=timezone("America/Santiago"))
    scheduler.add_job(send_email, trigger, id=job_id)

    return {"message": f"Email programado para las {hour}:{minute}"}

# Detenemos el scheduler al cerrar la aplicación
@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
