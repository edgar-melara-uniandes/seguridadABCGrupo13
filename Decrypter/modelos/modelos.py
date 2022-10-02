from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class RegistroIntegridad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_validacion = db.Column(db.DateTime)
    descripcion = db.Column(db.String(255))
    token_enviado = db.Column(db.String(64000))
    mensaje = db.Column(db.String(64000))

class RegistroIntegridadSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RegistroIntegridad
        load_instance = True     
class BotonAlarmaSchema(Schema):
    fecha_accionada = fields.DateTime(required=True)
    lugar = fields.String(required=True)
    usuario = fields.String(required=True)
    
    def __repr__(self):
        return '<BotonAlarma(name={self.fecha_accionado!r})>'.format(self=self)