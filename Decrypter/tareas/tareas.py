from datetime import datetime
from Decrypter.modelos.modelos import db, BotonPanicoSchema, RegistroIntegridad
import jwt
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task(name='monitor.integrity')
def desencriptarMensaje(args):
    print(args)
    mensaje = jwt.decode(args, "secret", algorithms=["HS256"])
    print(mensaje)
    validarMensaje(mensaje, args)

@celery_app.task(name="monitor.security")
def publicar_mensaje(args):
    pass

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