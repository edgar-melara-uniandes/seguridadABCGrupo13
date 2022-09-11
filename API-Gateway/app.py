import flask_monitoringdashboard as dashboard
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from vistas import VistaBotonPanico

app = Flask(__name__)
dashboard.config.init_from(file='/api_gateway_config.cfg')

dashboard.bind(app)

app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaBotonPanico,'/apigatewaybase/boton-panico/disparar')


