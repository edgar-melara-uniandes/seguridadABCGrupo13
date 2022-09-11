from monitor import create_app
from flask_restful import Resource, Api

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)


class VistaMonitor(Resource):

    def get(self):
        return 'Monitor is working', 200
            

api.add_resource(VistaMonitor, '/monitor')