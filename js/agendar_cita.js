// Función para obtener la disponibilidad del médico
const rut = localStorage.getItem('rut_medico');
async function obtenerHorarioMedico() {
    try {
        const response = await fetch(`http://127.0.0.1:8000/disponibilidad/${rut}`);
        const result = await response.json();

        // Limpiar el contenedor antes de añadir nuevos botones
        const contenedor = document.getElementById("horas");
        contenedor.innerHTML = "";
        let fecha_escogida = new Date(document.getElementById('fecha').value);
        fecha_escogida.setHours(fecha_escogida.getHours() + 3);
        let soloFecha = fecha_escogida.toLocaleDateString();  // Solo la fecha (sin hora)
        console.log(fecha_escogida);
        
        console.log(soloFecha);    
        console.log(typeof(fecha_escogida));
        // Crear botones dinámicamente con las horas disponibles
        result.data.forEach(item => {
            const inicio = new Date(item.inicio_disponibilidad);
            const fin = new Date(item.fin_disponibilidad);
            let hora = new Date(inicio);
            if (soloFecha == inicio.toLocaleDateString()) {
                while (hora < fin) {
                    const boton = document.createElement("button");
                    const horaFormateada = `${hora.getHours().toString().padStart(2, '0')}:${hora.getMinutes().toString().padStart(2, '0')}`;
                    boton.innerText = `${horaFormateada}`;
                    boton.onclick = () => agendarCita(horaFormateada);  // Agregar la función de agendar cita
                    contenedor.appendChild(boton);
                    hora.setHours(hora.getHours() + 1);
                }
            }
        });
    } catch (error) {
        console.error("Error al obtener la disponibilidad del médico:", error);
    }
}

// Función que se activa cuando se selecciona una fecha
function seleccionarFecha() {
    obtenerHorarioMedico();
}

// Función para agendar una cita
async function agendarCita(hora) {
    const fechaSeleccionada = document.getElementById("fecha").value;
    const rut_paciente = '11122334-5';
    let fechaInicio = new Date(`${fechaSeleccionada}T${hora}:00`);
    fechaInicio.setHours(fechaInicio.getHours() - 3);  // Crear la fecha completa para la cita
    let fechaFin = new Date(fechaInicio);  // La cita dura 1 hora
    fechaFin.setHours(fechaInicio.getHours() + 1);
    fechaInicio.toISOString;
    fechaFin.toISOString;
    const cita = {
        rut_doctor: rut,
        rut_paciente: rut_paciente,
        estado: "No confirmado",  // El estado inicial de la cita
        fecha_inicio: fechaInicio,
        fecha_fin: fechaFin
    };
    console.log(JSON.stringify(cita));
    try {
        const response = await fetch("http://127.0.0.1:8000/Cita", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(cita)
        });
        const result = await response.json();
        if (response.ok) {
            alert("Cita agendada exitosamente");
        } else {
            alert(`Error: ${result.detail}`);
        }
    } catch (error) {
        console.error("Error al agendar la cita:", error);
        alert("Hubo un problema al agendar la cita.");
    }
}