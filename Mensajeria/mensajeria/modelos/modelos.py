import imp
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EstadoSalud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    mensaje = db.Column(db.String(128))
    nombre_servicio = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.codigo, self.mensaje, self.nombre_servicio)

