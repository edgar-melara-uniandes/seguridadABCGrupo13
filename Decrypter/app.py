from Decrypter import create_app
from flask_restful import Resource, Api
from celery import Celery
from .modelos import db


app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()


class VistaDecrypter(Resource):

    def get(self):
        return 'Monitor is working', 200
            
api = Api(app)
api.add_resource(VistaDecrypter, '/monitor')