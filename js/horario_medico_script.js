document.addEventListener('DOMContentLoaded', function () {
    const grid = document.getElementById('time-grid');
    const days = ["Lun", "Mar", "Mié", "Jue", "Vie"];
    const hours = Array.from({ length: 10 }, (_, i) => (i + 8) + ":00"); // Horas de 8 a 17

    // Obtener el RUT del médico del input
    const nombreMedicoInput = document.getElementById('nombreMedicoInput');

    // Escuchar cuando el usuario ingrese un RUT y presione Enter
    nombreMedicoInput.addEventListener('change', function() {
        const rutMedico = nombreMedicoInput.value;

        console.log(`Fetching data for RUT: ${rutMedico}`);

        fetch(`http://localhost:8000/busqueda/rut/${rutMedico}`)
            .then(response => {
                console.log('Response received:', response);
                return response.json();
            })
            .then(data => {
                console.log('Data received:', data);
                if (data.data.length > 0) {
                    const medico = data.data[0];
                    document.getElementById('nombreMedico').innerText = medico.nombre;
                } else {
                    document.getElementById('nombreMedico').innerText = 'Médico no encontrado.';
                }
            })
            .catch(error => console.error('Error:', error));
    });

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

    // Evento para enviar la disponibilidad seleccionada
    document.getElementById('enviarDisponibilidadBtn').addEventListener('click', () => {
        const selectedBlocks = document.querySelectorAll('.time-block.selected');
        if (selectedBlocks.length === 0) {
            alert('Por favor, seleccione al menos un bloque de tiempo.');
            return;
        }

        const disponibilidad = Array.from(selectedBlocks).map(block => ({
            day: block.dataset.day,
            hour: block.dataset.hour
        }));

        const rut_medico = nombreMedicoInput.value; // Obtener el RUT del campo de texto

        // Convertir la disponibilidad a un formato adecuado para el backend
        const disponibilidadFormatted = disponibilidad.map(slot => {
            const inicio_disponibilidad = formatTimestamp(slot.day, slot.hour);
            const fin_disponibilidad = formatTimestamp(slot.day, getNextHour(slot.hour));
            return { rut_medico: rut_medico, inicio_disponibilidad, fin_disponibilidad };
        });

        disponibilidadFormatted.forEach(slot => {
            fetch('http://localhost:8000/disponibilidad', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(slot)
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                alert(data.Message);
            })
            .catch(error => console.error('Error:', error));
        });
    });

    function formatTimestamp(day, hour) {
        const today = new Date();
        const dayOfWeek = today.getDay(); // 0 (Domingo) to 6 (Sábado)
        const dayMap = {
            "Lun": 1,
            "Mar": 2,
            "Mié": 3,
            "Jue": 4,
            "Vie": 5
        };
        const targetDay = dayMap[day];
        const daysToAdd = (targetDay - dayOfWeek + 7) % 7; // Calcula los días a añadir para llegar al día objetivo
        const targetDate = new Date(today);
        targetDate.setDate(today.getDate() + daysToAdd);

        const year = targetDate.getFullYear();
        const month = String(targetDate.getMonth() + 1).padStart(2, '0');
        const date = String(targetDate.getDate()).padStart(2, '0');

        return `${year}-${month}-${date} ${hour}:00`;
    }

    function getNextHour(hour) {
        const [h, m] = hour.split(':').map(Number);
        const nextHour = h + 1;
        return `${String(nextHour).padStart(2, '0')}:${String(m).padStart(2, '0')}`;
    }
});


function volver(){
    window.location.href = "agenda_medico.html";
}