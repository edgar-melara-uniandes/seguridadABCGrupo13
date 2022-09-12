# Componente Mensajeria

## Instrucciones 

0. Se recomienda usar un sistema operativo Linux/MacOS o máquina virtual basada en Linux
1. Tener instalado redis.
2. Tener instalado la última versión de Python. Este código fue construido con v3.10.4
3. Tener instalado el gestor de paquetes `pip`. Se empleó pip 22.0.4
4. Crear un virtual environment para instalar las bibliotecas requeridos: `python -m venv /path/to/new/virtual/environment`
5. Activar el virtual environment. Esto varía según el sistema operativo:

Windows:
Desde Powershell, `.\venv\Scripts\activate` o `.\venv\Scripts\Activate.ps1`

Linux/MacOS:

Desde una consola bash, `source venv/bin/activate`

6. Usar archivo requirements que se encuentra en la raíz del proyecto, correr `pip install -r requirements.txt`
7. Ejecutar servidor redis, usar la ruta: lib/{python-version}/site-packages/redis_server/bin/redis-server
8. Ejecutar broker de tareas: `celery -A mensajeria.mensajes worker -l info`
