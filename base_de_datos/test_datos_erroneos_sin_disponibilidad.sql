INSERT INTO cita (rut_doctor, rut_paciente, estado, fecha_inicio, fecha_fin) VALUES
('12345678-9', '11122334-5', 'No confirmado', '2024-11-06 09:30:00', '2024-11-06 10:00:00');

-- Cita sin disponibilidad para el doctor '12345678-9' fuera de su disponibilidad el 8 de noviembre
INSERT INTO cita (rut_doctor, rut_paciente, estado, fecha_inicio, fecha_fin) VALUES
('12345678-9', '66778800-3', 'No confirmado', '2024-11-08 14:30:00', '2024-11-08 15:00:00');  -- 30 min después del fin de su disponibilidad

-- Cita sin disponibilidad para el doctor '22334455-6' fuera de su disponibilidad el 6 de noviembre
INSERT INTO cita (rut_doctor, rut_paciente, estado, fecha_inicio, fecha_fin) VALUES
('22334455-6', '99887766-5', 'No confirmado', '2024-11-06 07:30:00', '2024-11-06 08:15:00');  -- 45 min antes de su disponibilidad

-- Cita sin disponibilidad para el doctor '33445566-7' fuera de su disponibilidad el 7 de noviembre
INSERT INTO cita (rut_doctor, rut_paciente, estado, fecha_inicio, fecha_fin) VALUES
('33445566-7', '22334466-0', 'No confirmado', '2024-11-07 12:30:00', '2024-11-07 13:00:00');  -- 30 min después del fin de su disponibilidad

-- Cita sin disponibilidad para el doctor '22334455-6' fuera de su disponibilidad el 7 de noviembre
INSERT INTO cita (rut_doctor, rut_paciente, estado, fecha_inicio, fecha_fin) VALUES
('22334455-6', '77665544-8', 'No confirmado', '2024-11-07 09:30:00', '2024-11-07 10:30:00');  -- 1 hora fuera del rango de su disponibilidad



