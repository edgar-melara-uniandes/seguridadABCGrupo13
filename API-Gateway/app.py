from flask import Flask
from flask_restful import Api
# from flask_cors import CORS

from vistas import VistaBotonPanico

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

# cors = CORS(app)

api = Api(app)
api.add_resource(VistaBotonPanico,'/apigatewaybase/boton-panico/disparar/<string:id_boton>')


