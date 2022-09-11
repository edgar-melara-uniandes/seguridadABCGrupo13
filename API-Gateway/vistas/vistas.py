from datetime import datetime
import json, requests
from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from entidades.entidades import BotonAlarmaSchema
from entidades.externos.boton_panico import MicroserviceBotonAlarmaSchema

class VistaBotonPanico(Resource):

    path_boton_panico = "http://127.0.0.1:5001/botonpanico/accionar"

    def post(self):
        
        request_body = request.json

        input_schema_validation = BotonAlarmaSchema()
        try:
            validate_body = input_schema_validation.load(request_body)
        except ValidationError as err:
            return 'Error validando mensaje. Intente de nuevo', 400

        routed_schema_validation = MicroserviceBotonAlarmaSchema()

        boton_panico_body = {
            "fecha_accionado": str(datetime.now().isoformat()),
            "lugar": request_body["lugar"],
            "usuario": request_body["usuario"],
        }

        headers = {'Content-Type': 'application/json'}
        ruta_recepcionBotonPanico = self.path_boton_panico
        request_boton_panico_body = json.dumps(boton_panico_body) # ajustar a body David

        """  validate_salida = routed_schema_validation.load(boton_panico_body) """

        boton_panico_body["fecha_accionado"] = str(boton_panico_body["fecha_accionado"])
        
        try:
            post_boton_panico = requests.post(ruta_recepcionBotonPanico,
                                                   data=request_boton_panico_body,
                                                   headers=headers,timeout=10.000)
        except requests.exceptions.ConnectTimeout as err:
            return 'Panico no responde. Intente de nuevo', 500
        
        response_boton_panico = json.loads(post_boton_panico.content)

        if post_boton_panico.status_code != "201":
            return "Hubo un error al comunicarse con servicio de pánico, reintente de nuevo", 500
        
        return "Señal del botón de pánico recibida exitosamente", 201
        