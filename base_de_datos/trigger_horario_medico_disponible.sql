--- Funcion que verifica que existe un horario marcado como disponible de un medico
CREATE OR REPLACE FUNCTION medico_verificar_disponibilidad(
    p_rut_doctor VARCHAR,
    p_fecha_inicio TIMESTAMP,
    p_fecha_fin TIMESTAMP
) RETURNS BOOLEAN AS $$
DECLARE
    disponibilidad_count INTEGER;
BEGIN
    -- Consultamos cuántos rangos de disponibilidad del médico incluyen este horario
    SELECT COUNT(*)
    INTO disponibilidad_count
    FROM disponibilidad_medico
    WHERE rut_medico = p_rut_doctor
      AND inicio_disponibilidad <= p_fecha_inicio
      AND fin_disponibilidad >= p_fecha_fin;

    -- Si hay al menos un rango de disponibilidad válido, retornamos verdadero
    RETURN disponibilidad_count > 0;
END;
$$ LANGUAGE plpgsql;



--- Funcion que verifica que la cita no haya sido ocupada por otro paciente, con el fin de modificar los datos de las tablas lo menos posible
CREATE OR REPLACE FUNCTION cita_verificar_disponibilidad(
    p_rut_doctor VARCHAR,
    p_fecha_inicio TIMESTAMP,
    p_fecha_fin TIMESTAMP
) RETURNS BOOLEAN AS $$
DECLARE
    disponibilidad_count INTEGER;
BEGIN
    -- Consultamos cuántos rangos de disponibilidad del médico incluyen este horario
    SELECT COUNT(*)
    INTO disponibilidad_count
    FROM cita
    WHERE rut_doctor = p_rut_doctor
    AND GREATEST(p_fecha_inicio, fecha_inicio) < LEAST(p_fecha_fin, fecha_fin);

    -- Si hay al menos un rango de disponibilidad válido, retornamos verdadero
    RETURN disponibilidad_count = 0;
END;
$$ LANGUAGE plpgsql;



--- Funcion wrapper para las 2 funciones previas y mandar una excepcion cuando alguna marque false
CREATE OR REPLACE FUNCTION validar_cita()
RETURNS TRIGGER AS $$
BEGIN
    -- Llamamos a la función de verificación
    IF NOT medico_verificar_disponibilidad(NEW.rut_doctor, NEW.fecha_inicio, NEW.fecha_fin)
	OR NOT cita_verificar_disponibilidad(NEW.rut_doctor, NEW.fecha_inicio, NEW.fecha_fin) THEN
        RAISE EXCEPTION 'La cita no está dentro de los horarios de disponibilidad del médico';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Crear el Trigger en la tabla de citas
CREATE TRIGGER trigger_validar_cita
BEFORE INSERT ON cita
FOR EACH ROW
EXECUTE FUNCTION validar_cita();


