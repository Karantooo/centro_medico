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
);

CREATE TABLE cita (
    id_cita SERIAL PRIMARY KEY,
    rut_doctor VARCHAR,
    rut_paciente VARCHAR(20),
	estado VARCHAR(20),
	fecha_inicio TIMESTAMP,
	fecha_fin TIMESTAMP,
    FOREIGN KEY (rut_doctor) REFERENCES medico(rut),
    FOREIGN KEY (rut_paciente) REFERENCES paciente(rut),

	CONSTRAINT estado_cita CHECK (estado IN ('Confirmado', 'No confirmado', 'Cancelada'))
);

CREATE TABLE usuario (
    nombre VARCHAR PRIMARY KEY,
	mail VARCHAR NOT NULL UNIQUE,
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


CREATE TABLE disponibilidad_medico(
	rut_medico VARCHAR,
	inicio_disponibilidad TIMESTAMP,
	fin_disponibilidad TIMESTAMP,
	FOREIGN KEY (rut_medico) REFERENCES medico(rut)
);


