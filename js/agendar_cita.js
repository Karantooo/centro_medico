// Función para obtener la disponibilidad del médico
async function obtenerHorarioMedico(rut) {
    try {
    // Realiza la solicitud GET a la API
    const response = await fetch(`http://127.0.0.1:8000/disponibilidad/${rut}`);
    const result = await response.json();
    console.log(result);


    // Crear botones dinámicamente en un bucle
    const contenedor = document.getElementById("horas");
    contenedor.innerHTML = "";  // Limpia el contenedor antes de añadir nuevos botones

    // Recorre la respuesta de la API y crea los botones

    result.data.forEach(item => {
        const boton = document.createElement("button");
        boton.innerText = 'Inicio: ${item.inicio_disponibilidad}';  // Asigna la hora de inicio al texto del botón
        contenedor.appendChild(boton);
    });
} catch (error) {
    console.error("Error al obtener la disponibilidad del médico:", error);
}
}

// Función que se activa cuando se selecciona una fecha
function seleccionarFecha() {
const rutMedico = "12345678-9";  // Cambia el RUT según el médico
obtenerHorarioMedico(rutMedico);
}