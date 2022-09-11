# Componente Mensajeria

## Instalar virtual
 - python3 -m venv venv
 - source venv/bin/activate

## Instalar librerias
 - pip install flask
 - pip install celery
 - pip install redis
 - pip install redis-server

 - pip install flask_sqlalchemy

 - pip install requests

 - pip install Flask-RESTful
 - pip install jsonpickle

## Ejecutar servidor redis
 - lib/{python-version}/site-packages/redis_server/bin/redis-server
 - Nota: se recomienda version de pyhton <= 3.9

## Ejecutar broker de tareas
 - celery -A mensajeria.mensajes worker -l info

 ## Puerto donde se debe configurar cada componenete
  - componente mensajeria : flask run -p 5004
  - componente alarma : flask run -p 5005
  - componente monitor : flask run -p 5006

  ### Inicio de flujo
   - Mediante postman hacer una peticion POST al enpoint http://localhost:5005/alarma
