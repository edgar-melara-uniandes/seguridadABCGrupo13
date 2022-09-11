# Microservicio API-Gateway

Componente que actua como API Gateway del diseño inicial de la solución para el experimento

## Instrucciones 

1. Tener instalado la última versión de Python. Este código fue construido con v3.10.4
2. Tener instalado el gestor de paquetes `pip`. Se empleó pip 22.0.4
2. Crear un virtual environment para instalar las bibliotecas requeridos: `python -m venv /path/to/new/virtual/environment`
3. Activar el virtual environment. Esto varía según el sistema operativo:

Windows:
Desde Powershell, `.\venv\Scripts\activate` o `.\venv\Scripts\Activate.ps1`

Linux/MacOS:

Desde una consola bash, `.\venv\Scripts\activate`

4. Instalar dependencias mediante `pip install -r requirements.txt`

5. Para montar la aplicación:

`flask run -p <port>` donde `<port>` corresponde al puerto de escucha del microservicio de API Gateway.

No olvidar levantar el microservicio RecepcionBotonPanico que se encuentra en este mismo repositorio (ver README.md asociado)

Se cuenta con un archivo de configuración del dashboard de monitoreo Flask: `api_gateway_config.cfg`