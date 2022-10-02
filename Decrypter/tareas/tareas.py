import datetime
from Decrypter.modelos.modelos import BotonAlarmaSchema, db, RegistroIntegridad
import jwt
from celery import Celery
import json

celery_app_decrypter = Celery("tasks", broker="redis://localhost:6379/0")

celery_app_monitor = Celery("tasks", broker="redis://localhost:6379/1")

@celery_app_decrypter.task(name='decrypter.integrity')
def desencriptarMensaje(args):
    token=None
    jsonHeaders = json.loads(args['headers'])
    jsonSolicitud = args['solicitud']
    try:
        token = str(jsonHeaders['Authorization']).split("Bearer ")[-1]
    except: 
        publicar_mensaje.apply_async((dict(token=token, error="No se encontro header"),))
    print(token)
    if token is not None:
        validarTokenAutorizacion(token)
        validarMensaje(jsonSolicitud, token)
    else:
        publicar_mensaje.apply_async((dict(token=token, error="No se encontro token"),))

@celery_app_monitor.task(name="monitor.logger.security")
def publicar_mensaje(args):
    pass

def validarTokenAutorizacion(token):
    descripcion = "Error de autorización"
    tokenValidar=token
    try:
        decodedToken = jwt.decode(tokenValidar, "LzhYpdKwoNOKwPMxLbsxsHL8x63YkQ54", algorithms=["HS256"])
    except:
        """ registrarEnDB("", token, descripcion) """
        publicar_mensaje.apply_async((dict(token=token, error=descripcion),))
        

def validarMensaje(mensaje, token):
    print(mensaje)
    descripcion = "Error en estructura del payload"
    mensajeSchema = BotonAlarmaSchema()
    try:
        validate_body = mensajeSchema.load(mensaje)
    except: 
        """ registrarEnDB(mensaje, token, descripcion) """
        publicar_mensaje.apply_async((dict(token=token, error=descripcion),))
        
def registrarEnDB(mensaje="", token="", descripcion=""):
    nueva_accion = RegistroIntegridad(fecha_validacion = datetime.datetime.now(), descripcion = descripcion, token_enviado = str(token), mensaje=str(mensaje))
    db.session.add(nueva_accion)
    db.session.commit()
    db.session.remove()