function cambiar_html_medicos(a){
    const botones_especialidad = document.querySelectorAll('.button-group button');
    let se_puede1 = false;
    let se_puede2 = false;
    botones_especialidad.forEach(b => {
        if (b.classList.contains('selected')){
            se_puede1 = true;
        }   
    });
    const botones_convenio = document.querySelectorAll('.convenios button');
    botones_convenio.forEach(b => {
        if(b.classList.contains('selected')){
            se_puede2 = true;
        }
    });
    if(se_puede1 && se_puede2){
        window.location.href = a;
    }
    else{
        mostrar_error();
    }
}

function selecionar_medico(){

}

function selecionar_especialidad(boton){
    if(boton.classList.contains("selected")){
        boton.classList.remove("selected");
    }
    else{
        const botones = document.querySelectorAll('.button-group button');
        botones.forEach(b =>b.classList.remove('selected'));
        boton.classList.toggle("selected");
    }
}

function selecionar_convenio(boton){
    if(boton.classList.contains("selected")){
        boton.classList.remove("selected");
    }
    else{
        const botones = document.querySelectorAll('.convenios button');
        botones.forEach(b =>b.classList.remove('selected'));
        boton.classList.toggle("selected");
    }
}

function mostrar_error(){
    document.getElementById('mensaje-error').style.display = 'flex';   
}

function cerrar_error(){
    document.getElementById('mensaje-error').style.display = 'none';   
}