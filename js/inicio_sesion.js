let tipo_cuenta = "";

const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe al servidor
    acceder(); // Llama a tu función para manejar el inicio de sesión
});

function acceder(){
    console.log(tipo_cuenta);
    if(tipo_cuenta == "Médico"){
        const rut_medico = document.getElementById("RUT").value;
        localStorage.setItem("rut_medico", rut_medico);

        window.location.href = '../website/agenda_medico.html'; //cambia al html de la info de los médicos
    }
    else if(tipo_cuenta == "Paciente"){
        const rut_paciente = document.getElementById("RUT").value;
        localStorage.setItem("rut_ingresado", rut_paciente);

        window.location.href = '../website/index.html'; //cambia al html de la info de los médicos
    }
    else if(tipo_cuenta == "Admin"){
        const rut_admin = document.getElementById("RUT").value;
        localStorage.setItem("rut_ingresado", rut_admin);

        window.location.href = '../website/index.html'; //cambia al html de la info de los médicos
    }
}

function activar_incio_medicos(){
    cartel_inicio = document.getElementById('inicio_sesion');
    input_rut = document.getElementById('RUT');
    tipo_cuenta = "Médico";
    input_rut.placeholder = "RUT Médico";
    cartel_inicio.style.display = 'flex';
}

function activar_incio_paciente(){
    cartel_inicio = document.getElementById('inicio_sesion');
    input_rut = document.getElementById('RUT');
    tipo_cuenta = "Paciente";
    input_rut.placeholder = "RUT Paciente";
    cartel_inicio.style.display = 'flex';
}

function activar_incio_admin(){
    cartel_inicio = document.getElementById('inicio_sesion');
    input_rut = document.getElementById('RUT');
    tipo_cuenta = "Admin";
    input_rut.placeholder = "RUT Administrativo";
    cartel_inicio.style.display = 'flex';
}

function mostrar_error(){
    document.getElementById('mensaje-error').style.display = 'flex';   
}

function cerrar_error(){
    document.getElementById('mensaje-error').style.display = 'none';   
}