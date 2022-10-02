import datetime
from Decrypter.app import publicar_mensaje
from Decrypter.modelos.modelos import BotonAlarmaSchema, db, RegistroIntegridad
import jwt
from celery import Celery
import json

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task(name='monitor.integrity')
def desencriptarMensaje(args):
    jsonHeaders = json.loads(args['headers'])
    jsonSolicitud = args['solicitud']
    token = str(jsonHeaders['Authorization']).split("Bearer ")[-1]
    if token is not None:
        validarTokenAutorizacion(token)
        validarMensaje(jsonSolicitud, token)
    else:
        publicar_mensaje.apply_async((dict(token=token, error="No se encontro token"),))


def validarTokenAutorizacion(token):
    descripcion = "Error de autorización"
    try:
        decodedToken = jwt.decode(token, key='LzhYpdKwoNOKwPMxLbsxsHL8x63YkQ54', algorithms=['HS256', ])
    except:
        registrarEnDB("", token, descripcion)
        publicar_mensaje.apply_async((dict(token=token, error=descripcion),))
        

def validarMensaje(mensaje, token):
    print(mensaje)
    descripcion = "Error en estructura del payload"
    mensajeSchema = BotonAlarmaSchema()
    try:
        validate_body = mensajeSchema.load(mensaje)
    except: 
        registrarEnDB(mensaje, token, descripcion)
        publicar_mensaje.apply_async((dict(token=token, error=descripcion),))
        
def registrarEnDB(mensaje="", token="", descripcion=""):
    nueva_accion = RegistroIntegridad(frcha_validacion = datetime.datetime.now(), descripcion = descripcion, token = token)
    db.session.add(nueva_accion)
    db.session.commit()