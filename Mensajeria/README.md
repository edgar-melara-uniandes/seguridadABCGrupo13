# Componente Mensajeria

- Celery
python3 -m venv venv
source venv/bin/activate

pip install flask
pip install celery
pip install redis
pip install redis-server

pip install flask_sqlalchemy

pip install requests

pip install Flask-RESTful
pip install jsonpickle

--correr el broker
celery -A mensajeria.mensajes worker -l info
