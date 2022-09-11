from monitor import create_app
from flask_restful import Resource, Api
from flask import Flask, request, make_response, jsonify
import redis
import datetime
import json
import time

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)


class VistaMonitor(Resource):

    def post(self):
        print('Monitor is working')
            
class VistaMonitorSub(Resource):

    def get(self):
        red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
        sub = red.pubsub()
        sub.subscribe('pub')
        while True:
            message = sub.get_message()
            if message:
                print(message)
            time.sleep(0.01)    

api.add_resource(VistaMonitor, '/monitor')
api.add_resource(VistaMonitorSub, '/monitor-sub')