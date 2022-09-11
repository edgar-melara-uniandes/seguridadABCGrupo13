import os
from celery import Celery
from ..modelos import EstadoSalud
import requests
import redis
from ..app import db
import jsonpickle

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task(name='sub.estado')
def informar_estado_salud(solicitud_alerta_json):
    #deberia este servicio informar el estado de salud?
    print(solicitud_alerta_json)
    estado_salud = EstadoSalud(codigo=solicitud_alerta_json['code'], \
                                mensaje=solicitud_alerta_json['response']['mensaje'], \
                                nombre_servicio=solicitud_alerta_json['service'])
    #enviar solicitud rest
    db.session.add(estado_salud)
    estado_salud_serializable = jsonpickle.encode(estado_salud)
    requests.post(url = 'http://127.0.0.1:5006/monitor', data = estado_salud_serializable)
    publish(estado_salud_serializable)

def publish(message):
    red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
    red.publish('pub', message)