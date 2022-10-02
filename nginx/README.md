La configuración del API Gateway se realizo localmente mediante un servidor web NGNIX,
para su instalación en un entorno local se recomienda usar una maquina con sistema operativo Linux/MacOS

Los pasos de configuración son los siguientes:

Tener Homebrew previamente instalado

instalar NGINX con el comando `brew install nginx`

validar su instalacion `nginx -v`

Inicializar el server con permisos de admin `sudo nginx`

probar el server `open http://localhost:8080/`

detenemos la ejecuccion del server con el comanda `sudo nginx -s stop`

para agregar las rutas proxy tenemos que abrir el archivo con el siguiente comando (utilizar editor de preferencia para este caso se utiliza vscode)`code /usr/local/etc/nginx/nginx.conf`

luego el contenido de este archivo se reemplaza con el archivo **nginx.conf** en esta misma carpeta

para crear los certificados que utilizara el server corremos el siguiente comando `sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /usr/local/etc/nginx/nginx.key -out /usr/local/etc/nginx/nginx.crt`

luego inicializamos nuevamente el server `sudo nginx`

