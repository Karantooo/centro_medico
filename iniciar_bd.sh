#!/bin/bash


### Script para generar una nueva base de datos y que contenga los scripts de abajo
# Configuración
DB_NAME="test"
DB_USER="postgres"
DB_HOST="localhost"
DB_PORT="5432"

# Lista de scripts en el orden deseado
SCRIPTS=(
  "/home/karantooo/Documentos/ingenieria de software/centro_medico/base_de_datos/init_tablas.sql"
  "/home/karantooo/Documentos/ingenieria de software/centro_medico/base_de_datos/trigger_horario_medico_disponible.sql"
  "/home/karantooo/Documentos/ingenieria de software/centro_medico/base_de_datos/test_datos/datos_prueba.sql"
  # Agrega más scripts en el orden que prefieras
)

# 1. Crear la base de datos
echo "Creando la base de datos '$DB_NAME'..."
createdb -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" "$DB_NAME"
if [ $? -ne 0 ]; then
  echo "Error: No se pudo crear la base de datos."
  exit 1
fi

# 2. Ejecutar cada archivo SQL en el orden especificado
for script in "${SCRIPTS[@]}"; do
  echo "Ejecutando $script..."
  psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -f "$script"
  if [ $? -ne 0 ]; then
    echo "Error: Fallo al ejecutar $script."
    exit 1
  fi
done

echo "Todos los scripts se ejecutaron correctamente en el orden especificado."
