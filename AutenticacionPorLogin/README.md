# Microservicio AutenticacionPorLogin 

Componente que actua como Autenticacion Por Login (autorizador de usuarios) en el diseño inicial de la solución para el experimento 2

## Instrucciones 

1. Tener instalado la última versión de Python. Este código fue construido con v3.10.4
2. Tener instalado el gestor de paquetes `pip`. Se empleó pip 22.0.4
2. Crear un virtual environment para instalar las bibliotecas requeridas: `python -m venv /path/to/new/virtual/environment`
3. Activar el virtual environment. Esto varía según el sistema operativo:

Windows:
Desde Powershell, `.\venv\Scripts\activate` o `.\venv\Scripts\Activate.ps1`

Linux/MacOS:

Desde una consola bash, `.\venv\Scripts\activate`

4. Instalar dependencias mediante `pip install -r requirements.txt`

5. Para montar la aplicación:

`flask run -p <port>` donde `<port>` corresponde al puerto de escucha del microservicio de Autenticacion Por Login.

6. Invocar el API asociada a la ruta POST `http://127.0.0.1:<port>/autenticacionporlogin/login` , empleando un body que respete la siguiente estructura:
```
{
    "username": "nombreDeUsuario",
    "password": "contraseñaDeUsuario"
}
```

Cargar data en la base de datos local tipo archivo `access.db`; se provee ya una precargada con usuarios y servicios a los que tienen permiso

Recomendado (más no requerido) levantar el componente API-Gateway que se encuentra en este mismo repositorio (ver README.md asociado)


