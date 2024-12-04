const rut = "66778800-3"
async function Obtener_datos(){
    try {

        const respuesta = await fetch('http://127.0.0.1:8000/Cita/');
        if (!respuesta.ok) {
            throw new Error(`Error en la solicitud: ${respuesta.status}`);
        }
        //Como citas es un objeto lo convierte a un arreglo
        const citas = await respuesta.json();
        const citasData = citas.data || [];

        //En contenedor guardo body para adjuntar la tabla al final y tambien creo la tabla que hay que añadir
        const contenedor = document.getElementById("pagina_principal");
        const tabla = document.createElement("table");
        //Crear encabezado de la tabla que se mostrara en la pagina
        const encabezado = tabla.createTHead();
        const filaEncabezado = encabezado.insertRow();
        //en encabezados guardo lo datos que se mostraran en la primera fila
        const encabezados = ["Id cita", "Rut doctor", "Rut paciente", "Estado", "Fecha de inicio", "Fecha de fin"];
        encabezados.forEach(texto => {
            const celda = document.createElement("th");
            celda.textContent = texto;
            filaEncabezado.appendChild(celda);
        });

        //Ahora se añade el cuerpo
        const cuerpo = tabla.createTBody();
        console.log(citas.id_cita);
        citasData.forEach((cita) => {

            if(String(cita.rut_paciente).trim() === String(rut).trim()){
                const fila = cuerpo.insertRow();
                fila.insertCell().textContent = cita.id_cita;
                fila.insertCell().textContent = cita.rut_doctor;
                fila.insertCell().textContent = cita.rut_paciente;
                fila.insertCell().textContent = cita.estado;
                fila.insertCell().textContent = Adaptar_fecha(cita.fecha_inicio);
                fila.insertCell().textContent = Adaptar_fecha(cita.fecha_fin);
            }
        });

        contenedor.appendChild(tabla);
    }
    catch (error){
        console.error("Error al obtener sus citas", error);
    }
}

function Mostrar_citas(){
    Obtener_datos();
}
function Adaptar_fecha(fecha) {
    const fecha_adaptada = new Date(fecha);
    return fecha_adaptada.toLocaleDateString('es-ES');
}