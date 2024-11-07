INSERT INTO trabajador (rut, nombre) VALUES
('12345678-9', 'Juan Pérez'),
('98765432-1', 'María Gómez'),
('11223344-5', 'Carlos López'),
('22334455-6', 'Ana Martínez'),
('33445566-7', 'Luis Fernández'),
('44556677-8', 'Sofía Rojas'),
('55667788-0', 'Fernando Torres'),
('66778899-2', 'Valentina Salazar'),
('77889900-4', 'Diego Silva'),
('88990011-6', 'Camila Valdés');


INSERT INTO medico (rut, especialidad) VALUES
('12345678-9', 'Cardiología'),
('98765432-1', 'Pediatría'),
('11223344-5', 'Dermatología'),
('22334455-6', 'Neurología'),
('33445566-7', 'Medicina General');


INSERT INTO administrativo (rut) VALUES
('44556677-8'),
('55667788-0'),
('66778899-2'),
('77889900-4'),
('88990011-6');


INSERT INTO paciente (rut, nombre) VALUES
('11122334-5', 'Pedro González'),
('66778800-3', 'Lucía Fernández'),
('99887766-5', 'Ricardo Martínez'),
('22334466-0', 'Elena Rodríguez'),
('77665544-8', 'Marco Díaz');


-- Datos de prueba en disponibilidad_medico que abarcan las fechas de las citas en cita
INSERT INTO disponibilidad_medico (rut_medico, inicio_disponibilidad, fin_disponibilidad) VALUES
('12345678-9', '2024-11-06 07:00:00', '2024-11-06 09:00:00'),  -- Abarca cita del 6 de nov 08:00 a 08:30
('22334455-6', '2024-11-06 08:30:00', '2024-11-06 10:00:00'),  -- Abarca cita del 6 de nov 09:00 a 09:45
('33445566-7', '2024-11-07 10:00:00', '2024-11-07 12:00:00'),  -- Abarca cita del 7 de nov 10:30 a 11:30
('22334455-6', '2024-11-07 11:00:00', '2024-11-07 12:30:00'),  -- Abarca cita del 7 de nov 11:30 a 12:00
('12345678-9', '2024-11-08 12:00:00', '2024-11-08 14:00:00');  -- Abarca cita del 8 de nov 13:00 a 13:30


-- Actualizar los datos de prueba en la tabla cita con el nuevo campo fecha_inicio y fecha_fin
INSERT INTO cita (rut_doctor, rut_paciente, estado, fecha_inicio, fecha_fin) VALUES
('12345678-9', '11122334-5', 'Confirmado', '2024-11-06 08:00:00', '2024-11-06 08:30:00'),  -- 30 min
('22334455-6', '66778800-3', 'No confirmado', '2024-11-06 09:00:00', '2024-11-06 09:45:00'),  -- 45 min
('33445566-7', '99887766-5', 'Cancelada', '2024-11-07 10:30:00', '2024-11-07 11:30:00'),  -- 60 min
('22334455-6', '22334466-0', 'Cancelada', '2024-11-07 11:30:00', '2024-11-07 12:00:00'),  -- 30 min
('12345678-9', '77665544-8', 'Confirmado', '2024-11-08 13:00:00', '2024-11-08 13:30:00');  -- 30 min


-- usuarios trabajadores

INSERT INTO usuario (nombre, contrasenia) VALUES
('juanperez', 'contraseña123'),
('mariagomez', 'segura456'),
('carloslopez', 'clave789'),
('anamartinez', 'pass1000'),
('luisfernandez', 'clave2024');


INSERT INTO usuario_trabajador (nombre, rut) VALUES
('juanperez', '12345678-9'),
('mariagomez', '98765432-1'),
('carloslopez', '11223344-5'),
('anamartinez', '22334455-6'),
('luisfernandez', '33445566-7');


-- Usuarios pacientes

INSERT INTO usuario (nombre, contrasenia) VALUES
('pedrogonzalez', 'contraseñaPedro123'),
('luciafernandez', 'seguraLucia456'),
('ricardomartinez', 'claveRicardo789'),
('elenarodriguez', 'passElena1000'),
('marcodiaz', 'claveMarco2024');


INSERT INTO usuario_paciente (nombre, rut) VALUES
('pedrogonzalez', '11122334-5'),
('luciafernandez', '66778800-3'),
('ricardomartinez', '99887766-5'),
('elenarodriguez', '22334466-0'),
('marcodiaz', '77665544-8');
