import datetime
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task(name='monitor.logger')
def registrar_log(args):
    with open('log_boton_panico.txt', '+a') as file:
        file.write('alerta boton de panico - {}\n'.format(args))

@celery_app.task(name='monitor.integrity-check')
def register_integrity_check(args):
    with open('log_integrity_check.txt', '+a') as file:
        file.write('Verificacion de integridad con monitor - {}\n'.format(args))

@celery_app.task(name='decrypter.integrity-check')
def register_integrity_check(args):
    with open('log_decrypter_integrity_check.txt', '+a') as file:
        file.write('Verificacion de integridad con decrypter - {}\n'.format(args))
