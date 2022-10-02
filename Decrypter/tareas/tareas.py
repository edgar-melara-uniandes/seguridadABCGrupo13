from datetime import datetime
from Decrypter.modelos.modelos import db, BotonPanicoSchema, RegistroIntegridad
import jwt
from celery import Celery
import json

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task(name='monitor.integrity')
def desencriptarMensaje(args):
    jsonHeaders = json.loads(args['headers'])
    token = str(jsonHeaders['Authorization']).split("Bearer ")[-1]
    validarTokenAutorizacion(token)

@celery_app.task(name="monitor.security")
def publicar_mensaje(args):
    pass

def validarTokenAutorizacion(token):
    descripcion = "Error de autorización"
    try:
        decodedToken = jwt.decode(token, key='LzhYpdKwoNOKwPMxLbsxsHL8x63YkQ54', algorithms=['HS256', ])
    except:
        publicar_mensaje.apply_async((dict(token=token, error=descripcion),))

def validarMensaje(mensaje, token):
    descripcion = ""
    """ publicar_mensaje((descripcion,)) """
    error = BotonPanicoSchema.validate(mensaje)
    if error:
        descripcion = "Error validando la estructura de la informacion"
        registrarEnDB(mensaje, token, descripcion)
        publicar_mensaje((dict(token, descripcion),))
        
def registrarEnDB(mensaje, token, descripcion):
    nueva_accion = RegistroIntegridad(frcha_validacion = datetime.datetime.now(), \
    descripcion = descripcion, \
    token = token)
    db.session.add(nueva_accion)
    db.session.commit()