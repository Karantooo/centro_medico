#!/bin/bash


### Script para solo inicializar las tablas y los datos
# Configuración
DB_NAME="postgres"
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

# 1. Ejecutar cada archivo SQL en el orden especificado en la base de datos existente
for script in "${SCRIPTS[@]}"; do
  echo "Ejecutando $script en la base de datos '$DB_NAME'..."
  psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -f "$script"
  if [ $? -ne 0 ]; then
    echo "Error: Fallo al ejecutar $script."
    exit 1
  fi
done

echo "Todos los scripts se ejecutaron correctamente en la base de datos existente '$DB_NAME'."
