let tipo_cuenta = "";

const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe al servidor
    acceder(); // Llama a tu función para manejar el inicio de sesión
});

async function acceder(){
    if(tipo_cuenta == "Médico"){
        const rut_medico = document.getElementById("RUT").value;
        const contrasena = document.getElementById("contraseña").value;
        const resultado = await verificar_datos_medico(rut_medico,contrasena);
        if(resultado === 0){
            localStorage.setItem("rut_medico", rut_medico);
            localStorage.removeItem("rut_paciente");
            localStorage.removeItem("rut_admin");
            window.location.href = '../website/agenda_medico.html'; //cambia al html de la info de los médicos
        }
        else{
            alert("Intentelo denuevo");
        }
    }
    else if(tipo_cuenta == "Paciente"){
        const rut_paciente = document.getElementById("RUT").value;
        const contrasena = document.getElementById("contraseña").value;
        const resultado = await verificar_datos_paciente(rut_paciente,contrasena);
        if(resultado === 0){
            localStorage.setItem("rut_paciente", rut_paciente);
            localStorage.removeItem("rut_medico");
            localStorage.removeItem("rut_admin");
            window.location.href = '../website/index.html'; //cambia al html de la info de los médicos
        }
        else{
            alert("Intentelo denuevo");
        }

    }
    else if(tipo_cuenta == "Admin"){
        const rut_admin = document.getElementById("RUT").value;
        const contrasena = document.getElementById("contraseña").value;
        const resultado = await verificar_datos_admin(rut_admin,contrasena);
        if(resultado === 0){
            localStorage.setItem("rut_admin", rut_admin);
            localStorage.removeItem("rut_paciente");
            localStorage.removeItem("rut_medico");
            window.location.href = '../website/agenda_medico.html'; //cambia al html de la info de los médicos
        }
        else{
            alert("Intentelo denuevo");
        }
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

function registrarse(){
    window.location.href = '../website/registrarse.html';
}
async function verificar_datos_paciente(Rut,Contra){
    const usuario = {
        rut: Rut,
        contrasenia: Contra
    };
    try {
        const response = await fetch("http://127.0.0.1:8000/usuario/paciente_login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(usuario)
        });
        if (response.status === 200) {
            return 0;
        } else {
            return 1;
        }
    }
    catch (error){
        alert("Error");
        return 1;
    }
}
async function verificar_datos_medico(Rut,Contra){
    const usuario = {
        rut: Rut,
        contrasenia: Contra
    };
    try {
        const response = await fetch("http://127.0.0.1:8000/usuario/medico_login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(usuario)
        });
        if (response.status === 200) {
            return 0;
        } else {
            return 1;
        }
    }
    catch (error){
        alert("Error");
        return 1;
    }
}
async function verificar_datos_admin(Rut,Contra){
    const usuario = {
        rut: Rut,
        contrasenia: Contra
    };
    try {
        const response = await fetch("http://127.0.0.1:8000/usuario/admin_login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(usuario)
        });
        if (response.status === 200) {
            return 0;
        } else {
            return 1;
        }
    }
    catch (error){
        alert("Error");
        return 1;
    }
}