La configuración del API Gateway se realizo localmente mediante un servidor web NGNIX,
para su instalación en un entorno local se recomienda usar una maquina con sistema operativo Linux/MacOS

Los pasos de configuración son los siguientes:

Tener Homebrew previamente instalado
instalar NGINX con el comando `brew install nginx`
validar su instalacion `nginx -v`
Inicializar el server con permisos de admin `sudo nginx`
probar el serve `open http://localhost:8080/`
abrir el archivo con el siguiente comando (utilizar editor de preferencia para este caso se utiliza vscode)`code /usr/local/etc/nginx/nginx.conf`
