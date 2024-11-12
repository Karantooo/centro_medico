document.addEventListener('DOMContentLoaded', function () {
    const grid = document.getElementById('time-grid');
    const days = ["Lun", "Mar", "Mié", "Jue", "Vie"];
    const hours = Array.from({ length: 10 }, (_, i) => (i + 8) + ":00"); // Horas de 8 a 17

    // Crear encabezado de días de la semana
    const headerRow = document.createElement('div');
    headerRow.classList.add('row');
    
    // Celda vacía en la esquina superior izquierda
    const emptyCell = document.createElement('div');
    emptyCell.classList.add('header-cell');
    headerRow.appendChild(emptyCell);

    // Crear los encabezados de cada día
    days.forEach(day => {
        const dayHeader = document.createElement('div');
        dayHeader.classList.add('header-cell');
        dayHeader.textContent = day;
        headerRow.appendChild(dayHeader);
    });
    grid.appendChild(headerRow);

    // Crear filas de horas con bloques de tiempo
    hours.forEach(hour => {
        const row = document.createElement('div');
        row.classList.add('row');

        // Celda de hora en la primera columna
        const hourCell = document.createElement('div');
        hourCell.classList.add('hour-cell');
        hourCell.textContent = hour;
        row.appendChild(hourCell);

        // Crear los bloques de tiempo para cada día
        days.forEach(day => {
            const block = document.createElement('div');
            block.classList.add('time-block');
            block.dataset.day = day;
            block.dataset.hour = hour;
            row.appendChild(block);

            // Evento para seleccionar/deseleccionar el bloque
            block.addEventListener('click', () => {
                block.classList.toggle('selected');
            });
        });
        
        grid.appendChild(row);
    });
});
