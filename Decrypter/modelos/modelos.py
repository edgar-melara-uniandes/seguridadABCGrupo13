from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class RegistroIntegridad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_validacion = db.Column(db.DateTime)
    descripcion = db.Column(db.String(255))
    mensaje_encriptado = db.Column(db.String(64000))

class RegistroIntegridadSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RegistroIntegridad
        load_instance = True

class BotonPanico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_recepcion = db.Column(db.DateTime)
    lugar = db.Column(db.String(128))
    usuario = db.Column(db.String(128))

class BotonPanicoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BotonPanico
        load_instance = True