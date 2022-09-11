from marshmallow import Schema, fields

class MicroserviceBotonAlarmaSchema(Schema):

    fecha_accionada = fields.DateTime(format="%d-%m-%Y %H:%M:%S",required=True)
    lugar = fields.String(required=True)
    usuario = fields.String(required=True)