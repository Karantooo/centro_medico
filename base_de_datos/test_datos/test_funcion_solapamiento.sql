--- Test para verificar que no hayan horarios repetidos para un mismo doctor

--- FALSE

SELECT * FROM cita_verificar_disponibilidad('12345678-9','2024-11-06 08:00:00', '2024-11-06 08:30:00');
SELECT * FROM cita_verificar_disponibilidad('12345678-9','2024-11-06 08:15:00', '2024-11-06 08:30:00');
SELECT * FROM cita_verificar_disponibilidad('12345678-9','2024-11-06 08:15:00', '2024-11-06 08:25:00');

SELECT * FROM cita_verificar_disponibilidad('12345678-9', '2024-11-06 08:00:00', '2024-11-06 08:30:00');

SELECT * FROM cita_verificar_disponibilidad('12345678-9', '2024-11-06 08:15:00', '2024-11-06 08:30:00');

SELECT * FROM cita_verificar_disponibilidad('12345678-9', '2024-11-06 08:15:00', '2024-11-06 08:25:00');



--- TRUE
SELECT * FROM cita_verificar_disponibilidad('12345678-9','2024-11-06 09:00:00', '2024-11-06 09:30:00');
SELECT * FROM cita_verificar_disponibilidad('12345678-9', '2024-11-06 09:00:00', '2024-11-06 09:30:00'); 

SELECT * FROM cita_verificar_disponibilidad('12345678-9', '2024-11-06 10:00:00', '2024-11-06 10:30:00'); 

SELECT * FROM cita_verificar_disponibilidad('12345678-9', '2024-11-08 15:00:00', '2024-11-08 15:30:00'); 
