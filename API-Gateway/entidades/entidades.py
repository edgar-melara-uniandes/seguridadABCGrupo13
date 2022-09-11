from marshmallow import Schema, fields

class BotonAlarmaSchema(Schema):

    fecha_accionado = fields.DateTime(required=True)
    lugar = fields.String(required=True)
    usuario = fields.String(required=True)
    fecha_recepcion = fields.DateTime(required=True)
    
    def __repr__(self):
        return '<BotonAlarma(name={self.fecha_accionado!r})>'.format(self=self)

    