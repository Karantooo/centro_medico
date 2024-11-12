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
