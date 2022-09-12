# Experimento de disponibilidad solución basada en Microservicios

Contiene el código para montar a nivel local los componentes empleados para el experimento de disponibilidad

## Instrucciones 

0. Se recomienda usar un sistema operativo Linux/MacOS o máquina virtual basada en Linux
1. Tener instalado redis. Redis server v=6.2.7 
2. Tener instalado la última versión de Python. Este código fue construido con v3.10.4
3. Tener instalado el gestor de paquetes `pip`. Se empleó pip 22.0.4
4. Crear un virtual environment para instalar las bibliotecas requeridos: `python -m venv /path/to/new/virtual/environment`
5. Activar el virtual environment. Esto varía según el sistema operativo:

Windows:
Desde Powershell, `.\venv\Scripts\activate` o `.\venv\Scripts\Activate.ps1`

Linux/MacOS:

Desde una consola bash, `source venv/bin/activate`

4. Instalar dependencias mediante `pip install -r requirements.txt`

5. Para montar la aplicación:

Los componentes están basados en el framework Flask (Python). Usar 

`flask run -p <port>` desde una consola por componente, que apunte a cada carpeta de componete

donde `<port>` corresponde al puerto de escucha designado al componente.

Para cada componente se han designado los siguientes puertos:

* API-Gateway: pt 5000
* RecepcionBotonPanico: pt 5001
* Monitor: pt 5006

Para ejectuar las tareas de celery se tiene que estar en la carpeta Monitor

`cd Monitor`

y ejecutar el comando ` Celery -A tareas.tareas worker -l info`

Se cuenta con un archivo de configuración del dashboard de monitoreo Flask para el API Gateway y ayudar en la recolección de métricas:

| Componente   | Ruta de archivo config para Dashboard     | Ruta de acceso a dashboard      |
|--------------|-------------------------------------------|---------------------------------|
| API-Gateway  | `API-Gateway/api_gateway_config.cfg`      | http://localhost:5000/dashboard |

El monitor en un archivo de log, registra los heartbeat e info asociada que manda RecepcionBotonPanico
