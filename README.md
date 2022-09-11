# Experimento de disponibilidad solución basada en Microservicios

Contiene el código para montar a nivel local los componentes empleados para el experimento de disponibilidad

## Instrucciones 

1. Tener instalado la última versión de Python. Este código fue construido con v3.10.4
2. Tener instalado el gestor de paquetes `pip`. Se empleó pip 22.0.4
2. Crear un virtual environment para instalar las bibliotecas requeridos: `python -m venv /path/to/new/virtual/environment`
3. Activar el virtual environment. Esto varía según el sistema operativo:

Windows:
Desde Powershell, `.\venv\Scripts\activate` o `.\venv\Scripts\Activate.ps1`

Linux/MacOS:

Desde una consola bash, source venv/bin/activate

4. Instalar dependencias mediante `pip install -r requirements.txt`

5. Para montar la aplicación:

Los componentes están basados en el framework Flask (Python). Usar 

`flask run -p <port>`

donde `<port>` corresponde al puerto de escucha del microservicio de API Gateway.

Para cada componente se han designado los siguientes puertos:

* API-Gateway: pt 5000
* RecepcionBotonPanico: pt 5005
* Monitor: pt

Se cuenta con un archivo de configuración del dashboard de monitoreo Flask para:

| Componente   | Ruta de archivo config para Dashboard     | Ruta de acceso a dashboard      |
|--------------|-------------------------------------------|---------------------------------|
| APi-Gateway  | `API-Gateway/api_gateway_config.cfg`      | http://localhost:5000/dashboard |

