from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class BotonPanico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_accionada = db.Column(db.DateTime)
    fecha_recepcion = db.Column(db.DateTime)
    lugar = db.Column(db.String(128))
    usuario = db.Column(db.String(128))

class BotonPanicoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BotonPanico
        load_instance = True