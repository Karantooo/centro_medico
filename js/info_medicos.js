async function obtenerMedicos(){
    const especialidad = localStorage.getItem('especialidad');
    const url = `http://127.0.0.1:8000/busqueda/especialidad/${especialidad}`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Error en la solicitud");

        const data = await response.json();
        mostrarMedicos(data.data);
    } catch (error) {
        console.error("Error al obtener los médicos:", error);
    }
}

function mostrarMedicos(medicos) {
    const contenedor = document.getElementById("contenedorMedicos");
    contenedor.innerHTML = "";  // Limpiar el contenedor

    medicos.forEach(medico => {
        const cuadro = document.createElement("div");
        cuadro.className = "cuadro-medico";
        cuadro.innerHTML = `
            <p><strong>Rut:</strong> ${medico.rut}</p>
            <p><strong>Nombre:</strong> ${medico.nombre}</p>
            <p><strong>Especialidad:</strong> ${medico.especialidad}</p>
            <button onclick="agendarCita('${medico.rut}')" class="Boton-siguiente">Agendar Cita</button>
        `;
        contenedor.appendChild(cuadro);
    });
}


function agendarCita(rut) {
    localStorage.setItem('rut_medico', rut);
    window.location.href = "agendar_cita.html";
}
obtenerMedicos();

function volver_especialidades(){
    window.location.href = 'index.html'
}