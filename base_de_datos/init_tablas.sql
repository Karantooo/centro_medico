CREATE TABLE trabajador (
    rut VARCHAR PRIMARY KEY,
    nombre VARCHAR
);

CREATE TABLE medico (
    rut VARCHAR PRIMARY KEY, 
    especialidad VARCHAR,
    FOREIGN KEY (rut) REFERENCES trabajador(rut)
);

CREATE TABLE administrativo (
    rut VARCHAR PRIMARY KEY,
    FOREIGN KEY (rut) REFERENCES trabajador(rut)
);

CREATE TABLE paciente (
    rut VARCHAR PRIMARY KEY,
    nombre VARCHAR
);a

CREATE TABLE cita (
    id_cita SERIAL PRIMARY KEY,
    duracion_minutos INTEGER,
    rut_doctor VARCHAR,
    rut_paciente VARCHAR(20),
	estado VARCHAR(20),
	fecha TIMESTAMP,
	
    FOREIGN KEY (rut_doctor) REFERENCES medico(rut),
    FOREIGN KEY (rut_paciente) REFERENCES paciente(rut),

	CONSTRAINT estado_cita CHECK (estado IN ('Confirmado', 'No confirmado', 'Cancelada', 'Disponible'))
);


CREATE TABLE usuario (
    nombre VARCHAR PRIMARY KEY,
    contrasenia VARCHAR
);

CREATE TABLE usuario_trabajador (
    nombre VARCHAR PRIMARY KEY,
    rut VARCHAR,
    FOREIGN KEY (rut) REFERENCES trabajador(rut),
    FOREIGN KEY (nombre) REFERENCES usuario(nombre)
);

CREATE TABLE usuario_paciente (
    nombre VARCHAR PRIMARY KEY,
    rut VARCHAR,
    FOREIGN KEY (rut) REFERENCES paciente(rut),
    FOREIGN KEY (nombre) REFERENCES usuario(nombre)
);





