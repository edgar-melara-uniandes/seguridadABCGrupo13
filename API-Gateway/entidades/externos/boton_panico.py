from marshmallow import Schema, fields

class MicroserviceBotonAlarmaSchema(Schema):

    fecha_accionado = fields.DateTime(required=True)
    lugar = fields.String(required=True)
    usuario = fields.String(required=True)