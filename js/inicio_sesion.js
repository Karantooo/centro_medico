document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Evitar el envío del formulario para manejarlo con JavaScript
        
        const rut = document.getElementById('RUT').value;
        const contrasena = document.getElementById('contraseña').value;
        
        if (rut && contrasena) {
            localStorage.setItem('rutPaciente', rut);
            // Redirigir al usuario a la página principal (index.html)
            window.location.href = '../website/index.html'; // Cambia la ruta según la estructura de carpetas
        } else {
            alert('Por favor, ingrese tanto el RUT como la contraseña.');
        }
    });
});