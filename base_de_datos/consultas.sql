--- buscar cita por id

SELECT 
    c.id_cita,
    c.rut_doctor,
    c.rut_paciente,
    c.estado,
    c.fecha_inicio,
    c.fecha_fin,
    t.nombre AS nombre_medico,
    m.especialidad AS especialidad_medico,
    p.nombre AS nombre_paciente
FROM 
    cita c
JOIN 
    medico m ON c.rut_doctor = m.rut
JOIN 
    trabajador t ON m.rut = t.rut
JOIN 
    paciente p ON c.rut_paciente = p.rut
	
WHERE id_cita = 17;


--- Insertar cita medica
INSERT INTO cita (rut_doctor, rut_paciente, estado, fecha_inicio, fecha_fin) VALUES
('12345678-9', '11122334-5', 'Confirmado', '2024-11-06 08:00:00', '2024-11-06 08:30:00');


--- Obtener todos los medicos

SELECT 
    t.rut,
    t.nombre,
    m.especialidad
FROM 
    trabajador t
JOIN 
    medico m ON t.rut = m.rut;

--- Obtener todos los medicos de una misma especialidad 

SELECT 
    t.rut,
    t.nombre,
    m.especialidad
FROM 
    trabajador t
JOIN 
    medico m ON t.rut = m.rut
WHERE 
    m.especialidad = 'Cardiología';

--- Buscar medico

SELECT 
    t.rut,
    t.nombre,
    m.especialidad
FROM 
    trabajador t
JOIN 
    medico m ON t.rut = m.rut
WHERE 
    t.rut = '12345678-9';


--- Obtener disponibilidad
SELECT 
    t.rut,
    t.nombre,
    m.especialidad,
    d.inicio_disponibilidad,
    d.fin_disponibilidad
FROM 
    trabajador t
JOIN 
    medico m ON t.rut = m.rut
JOIN 
    disponibilidad_medico d ON m.rut = d.rut_medico
WHERE 
    t.rut = '12345678-9';

--- Insertar disponibilidad
INSERT INTO disponibilidad_medico (rut_medico, inicio_disponibilidad, fin_disponibilidad) VALUES
('12345678-9', '2024-11-06 07:00:00', '2024-11-06 09:00:00'); 


--- Obtener todos los datos de las citas 
SELECT * FROM cita;




-- Obtener usuario por RUT de paciente
SELECT u.nombre, u.mail, u.contrasenia, up.rut
FROM usuario u
JOIN usuario_paciente up ON u.nombre = up.nombre;



-- Obtener usuario por RUT de medico o administrativo
SELECT u.nombre, u.mail, u.contrasenia, up.rut
FROM usuario u
JOIN usuario_trabajador up ON u.nombre = up.nombre
WHERE up.rut = '12345678-9';



-- Obtener mail de usuario paciente por rut
SELECT u.mail as mail_paciente
FROM usuario u
JOIN usuario_paciente up ON u.nombre = up.nombre
WHERE up.rut = '22334466-0';

-- Obtener todas las citas que un paciente a agendado
SELECT 
	cita.estado,
	cita.fecha_inicio,
	cita.fecha_fin,
	trabajador.nombre AS nombre_medico
FROM cita
JOIN paciente on cita.rut_paciente = paciente.rut
JOIN trabajador on cita.rut_doctor = trabajador.rut
WHERE rut_paciente = '22334466-0'; 


-- Obtener todas las citas que tiene un medico en un dia
SELECT 
	cita.estado,
	cita.fecha_inicio,
	cita.fecha_fin,
	trabajador.nombre AS nombre_medico
FROM cita
JOIN trabajador on cita.rut_doctor = trabajador.rut
WHERE trabajador.rut = '12345678-9'
AND DATE(cita.fecha_inicio) = '2024-11-06 '; 


-- Obtener todas las citas que tiene un medico desde un dia en adelante
SELECT 
	cita.estado,
	cita.fecha_inicio,
	cita.fecha_fin,
	trabajador.nombre AS nombre_medico
FROM cita
JOIN trabajador on cita.rut_doctor = trabajador.rut
WHERE trabajador.rut = '12345678-9'
AND DATE(cita.fecha_inicio) >= '2024-11-06 '; 



--- Para registrar un paciente
INSERT INTO paciente (rut, nombre) 
VALUES ('33445577-9', 'Andrea Castillo');

INSERT INTO usuario (nombre, contrasenia, mail) 
VALUES ('andreacastillo', 'claveAndrea123', 'andrea.castillo@gmail.com');

INSERT INTO usuario_paciente (nombre, rut) 
VALUES ('andreacastillo', '33445577-9');

-- Login para usuario paciente
-- Aqui se obtienen los datos y desde la API se tiene que hacer la verificacion 

SELECT u.nombre, contrasenia, rut 
FROM usuario u
JOIN usuario_paciente up ON u.nombre = up.nombre
WHERE up.rut = '22334466-0';

-- Login para usuario medico
-- Aqui se obtienen los datos y desde la API se tiene que hacer la verificacion 
SELECT u.nombre, u.contrasenia, up.rut 
FROM usuario u
JOIN usuario_trabajador up ON u.nombre = up.nombre
JOIN medico m ON up.rut = m.rut
WHERE up.rut = '12345678-9';


-- Login para usuario administrativo
-- Aqui se obtienen los datos y desde la API se tiene que hacer la verificacion 
SELECT u.nombre, u.contrasenia, ut.rut 
FROM usuario u
JOIN usuario_trabajador ut ON u.nombre = ut.nombre
JOIN administrativo a ON ut.rut = a.rut
WHERE ut.rut = '44556677-8';
