from monitor import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import json

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)


class VistaMonitor(Resource):

    def post(self):
        print('Monitor is working')
            

api.add_resource(VistaMonitor, '/monitor')