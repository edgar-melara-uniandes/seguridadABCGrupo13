from alarma import create_app
from flask_restful import Resource, Api
import json
from celery import Celery

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task(name = 'sub.estado')
def enviar_estado_salud(estado_salud):
    pass


class VistaAlarma(Resource):

    def post(self):
        data = {    
                    "solicitud": { "fecha_accionada": "12-11-2018 09:15:32asda", "lugar": "Casa", "usuario": "Orlando" },
                    "response": { "mensaje": "No logramos recibir alarma", "status": "error" },
                    "code": 404,
                    "service": "botonAlerta"
                }
        #dataJson = json.dumps(data)
        args = (data,)
        enviar_estado_salud.apply_async(args)
        print()
            

api.add_resource(VistaAlarma, '/alarma')