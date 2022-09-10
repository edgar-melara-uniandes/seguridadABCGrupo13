from marshmallow import Schema, fields

class BotonAlarmaSchema(Schema):

    fecha_accionado = fields.DateTime(required=True)
    lugar = fields.String(required=True)
    usuario = fields.String(required=True)
    fecha_recepcion = fields.DateTime(required=True)

    '''def __init__(self,fecha_accionado, lugar, usuario, fecha_recepcion):

        self.fecha_accionado = fecha_accionado
        self.lugar = lugar
        self.usuario = usuario
        self.fecha_recepcion = fecha_recepcion'''
    
    def __repr__(self):
        return '<BotonAlarma(name={self.fecha_accionado!r})>'.format(self=self)

    