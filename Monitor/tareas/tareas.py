import datetime
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task(name='monitor.logger')
def registrar_log(args):
    with open('log_boton_panico.txt', '+a') as file:
        file.write('alerta boton de panico - {}'.format(args))
