
CREATE OR REPLACE FUNCTION verificar_disponibilidad(
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

CREATE 

CREATE OR REPLACE FUNCTION validar_cita()
RETURNS TRIGGER AS $$
BEGIN
    -- Llamamos a la función de verificación
    IF NOT verificar_disponibilidad(NEW.rut_doctor, NEW.fecha_inicio, NEW.fecha_fin) THEN
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
