# Microservicio RecepcionBotonPanico

El microservicio RecepcionBotonPanico tiene como funcionalidad principal recibir una alarma de pánico desde el usuario. Esta solicitud la recibe desde una API Gateway en un formato específico. Una vez recibida se adiciona una fecha de recepción y se almacena en una base de datos SQLite del mismo microservicio. De no ser procesada la información, se genera un mensaje con la información de petición y es publicada mediante una cola de mensajes. 


## Instrucciones 

1. Tener instalado la última versión de Python 3.9 o superior.
2. Tener instalado el gestor de paquetes `pip`.
3. Hacer usuo de un virtual environment para instalar las bibliotecas requeridos: `python -m venv "nombre_entorno"`
4. Activar el virtual environment. Esto varía según el sistema operativo:
    - Windows:
    Desde Powershell, `.\venv\Scripts\activate` o `.\venv\Scripts\Activate.ps1`
    - Linux/MacOS:
    Desde una consola bash, `source "nombre_entorno"\bin\activate`

5. Instalar las dependencias:
    - flask
    - flask_sqlalchemy
    - marshmallow
    - flask_restful
    - flask_cors
    - celery
    Tambien puede hacer uso del comando `pip install -r requirements.txt` para instalarlas.

6. Para montar la aplicación:
    `flask run -p <port>` donde `<port>` corresponde al puerto de escucha del microservicio de API Gateway en este caso esta configurado con el 5001.

7. Por último, se manejan las siguientes estructuras de datos:
    - Recibir petición de botón de pánico (API Gateway):
        ```json
           {
	            "fecha_accionada": "12-11-2018 09:15:32",
	            "lugar": "Casa",
	            "usuario": "Orlando"
            }
        ```
    - Publicar mensaje (Cola de mensajería):
        ```json
            {
               "solicitud": {
    	            "fecha_accionada": "12-11-2018 09:15:32",
    	            "lugar": "Casa",
    	            "usuario": "Orlando"
                },
                "response": {
                    "mensaje": "Mensaje del resultado de la operacion",
                    "status": "error o success"
                },
                "code": 200
            }
        ```