/*document.addEventListener('DOMContentLoaded', function () {
    // Seleccionar todos los botones de citas
    const appointmentButtons = document.querySelectorAll('.appointment');
    const infoContainer = document.getElementById('cita-info');
    const infoText = document.getElementById('info-text');


    // Agregar evento de clic a cada botón
    appointmentButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Obtener información de la cita del atributo data-info
            const info = button.getAttribute('data-info');

            // Mostrar la información en el contenedor
            infoText.textContent = info;
            infoContainer.style.display = 'block'; // Hacer visible el contenedor
        });
    });
});
*/

let rut_medico = null;
rut_medico = localStorage.getItem("rut_medico");
if(rut_medico != null){
    document.getElementById("filter-section").style.display = 'none';
}
else{
    get_horas();
}

