# Proyecto centro medico
## Integrantes

Pablo Villagrán Hermanns (2023439231)

Luis ignacio Martinez Neira (2023427985)

Carlos Tomás Álvares Norambuena (2022433621)

Benjamín Villarroel Rubio (2022424613)

Juan Felipe Raysz Muñoz, Matricula (2023426890)

## Dependencias
``` pip install fastapi[all] psycopg2 ```
Se requiere de postgresql.

Con postgre ejecutar los archivos:

"/home/karantooo/Documentos/ingenieria de software/centro_medico/base_de_datos/init_tablas.sql"

"/home/karantooo/Documentos/ingenieria de software/centro_medico/base_de_datos/trigger_horario_medico_disponible.sql"

"/home/karantooo/Documentos/ingenieria de software/centro_medico/base_de_datos/test_datos/datos_prueba.sql"

En ese orden.
Despues inicializar la API con:

``` uvicorn app.main:app --reload ```

Por ultimo ya se pueden ejecutar las paginas.
  
