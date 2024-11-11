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


