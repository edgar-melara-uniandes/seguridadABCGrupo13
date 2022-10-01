
import datetime
import random
from RecepcionBotonPanico import create_app
from flask_restful import Resource, Api
from flask import request
from flask_cors import CORS
from celery import Celery
from .modelos import db, BotonPanico
import json


celerity_app = Celery(__name__, broker="redis://localhost:6379/0")

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
cors = CORS(app) 

@celerity_app.task(name="monitor.logger")
def enviar_mensaje(mensaje):
    pass

@celerity_app.task(name="decrypter.integrity-check")
def integrity_check(mensaje):
    pass

class VistaAccionBotonPanico(Resource):

    def post(self):
        response = dict()

        comportamiento = random.randint(0, 99)
        if comportamiento < 90:
            code = 201
        else:
            code = 503

        try:
            nueva_accion = BotonPanico(fecha_accionada = datetime.datetime.strptime(request.json['fecha_accionada'], "%d-%m-%Y %H:%M:%S"), \
            fecha_recepcion = datetime.datetime.now(), \
            lugar = request.json['lugar'], \
            usuario = request.json['usuario'])
            db.session.add(nueva_accion)
            db.session.commit()
        except:
            response["mensaje"] = "No logramos recibir alarma"
            response["status"] = "error"
            code = 400
        
        if code == 201:
            response["mensaje"] = "Recibimos la alarma con exito"
            response["status"] = "success"
        else:
            response["mensaje"] = "FATAL_ERROR"
            response["status"] = "error"
        
        args = dict(
            solicitud = request.json,
            response = response,
            code = code
        )
        print(args)
        db.session.remove()
        enviar_mensaje.apply_async((args,))

        args_for_integrity_check = dict(
            headers = json.dumps({k:v for k, v in request.headers.items()}),
            solicitud = request.json,
            response = response,
            code = code
        )
        integrity_check.apply_async((args_for_integrity_check,))
        return response, code

api = Api(app)
api.add_resource(VistaAccionBotonPanico, "/botonpanico/accionar")

