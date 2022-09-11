
import datetime
from RecepcionBotonPanico import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
from flask_cors import CORS
from celery import Celery
from .modelos import db, BotonPanico


celerity_app = Celery("task", broker="ruta") 


app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
cors = CORS(app) 

@celerity_app.task(name="nombre de la cola")
def enviar_mensaje(mensaje):
    pass
class VistaAccionBotonPanico(Resource):

    def post(self):
        response = dict()
        code = 200
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
            code = 404
        else:   
            response["mensaje"] = "Recibimos la alarma con exito"
            response["status"] = "success"
        finally:
            args = dict(
                solicitud = request.json,
                response = response,
                code = code
            )
            print(args)
            db.session.remove()
            enviar_mensaje.apply_async(args)
            return response, code

        
        
api = Api(app)
api.add_resource(VistaAccionBotonPanico, "/botonpanico/accionar")

