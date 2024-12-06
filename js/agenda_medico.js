function cambiar_a_horario(){
    console.log(window.localStorage.getItem("rut_admin"));
    if(window.localStorage.getItem("rut_admin") != null){
        localStorage.removeItem("rut_medico")
    }
    window.location.href = "horario_medico.html";
}

// Obtén el RUT del localStorage si existe
let rut_medico = localStorage.getItem("rut_medico");

// Oculta el filtro si el RUT ya está almacenado
if (rut_medico !== null) {
    document.getElementById("filter-section").style.display = 'none';
    obtenerCitas(rut_medico);
} else {
    // Agrega evento al botón de buscar
    document.getElementById("buscarCitasBtn").addEventListener("click", () => {
        const rut = document.getElementById("rutMedico").value.trim();
        if (rut) {
            localStorage.setItem("rut_medico", rut);
            obtenerCitas(rut);
        } else {
            alert("Por favor, ingrese un RUT válido.");
        }
    });
}

// Función para obtener citas del backend
async function obtenerCitas(rut) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/Cita/medico/${rut}`);
        console.log(response);
        if (response.ok) {
            const data = await response.json();
            mostrarCitas(data.data); // Pasa las citas al método para mostrarlas
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        console.error("Error al obtener citas:", error);
        alert("No se pudo conectar al servidor.");
    }
}

// Función para mostrar citas como botones
function mostrarCitas(citas) {
    const appointmentsList = document.getElementById("appointments-list");
    appointmentsList.innerHTML = ""; // Limpia la lista de citas

    if (citas.length === 0) {
        appointmentsList.innerHTML = "<p>No hay citas disponibles para este médico.</p>";
        return;
    }

    // Genera botones para cada cita
    citas.forEach((cita, index) => {
        const button = document.createElement("button");
        button.className = "appointment";
        button.textContent = `Cita ${index + 1}: ${cita.fecha_inicio}`;
        button.addEventListener("click", () => mostrarDetallesCita(cita));
        appointmentsList.appendChild(button);
    });
}

// Función para mostrar los detalles de una cita
function mostrarDetallesCita(cita) {
    const detailsDiv = document.getElementById("appointment-details");
    const infoParagraph = document.getElementById("appointment-info");

    // Muestra los detalles de la cita
    infoParagraph.innerHTML = `
        <strong>Estado:</strong> ${cita.estado}<br>
        <strong>Fecha de Inicio:</strong> ${cita.fecha_inicio}<br>
        <strong>Fecha de Fin:</strong> ${cita.fecha_fin}<br>
        <strong>Médico:</strong> ${cita.nombre_medico}<br>
        <strong>Paciente:</strong> ${cita.nombre_paciente}
    `;

    detailsDiv.style.display = "block";
}
