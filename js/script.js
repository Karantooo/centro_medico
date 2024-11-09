document.addEventListener('DOMContentLoaded', function () {
    const grid = document.getElementById('time-grid');
    const days = ["Lun", "Mar", "Mié", "Jue", "Vie"];
    const hours = Array.from({ length: 10 }, (_, i) => (i + 8) + ":00"); // Horas de 8 a 17

    // Genera la cuadrícula de bloques
    hours.forEach(hour => {
        days.forEach(day => {
            const block = document.createElement('div');
            block.classList.add('time-block');
            block.dataset.day = day;
            block.dataset.hour = hour;
            block.textContent = `${day} ${hour}`;
            grid.appendChild(block);

            // Evento para seleccionar/deseleccionar el bloque
            block.addEventListener('click', () => {
                block.classList.toggle('selected');
            });
        });
    });
});
