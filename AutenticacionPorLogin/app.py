# import flask_monitoringdashboard as dashboard
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from Entidades import db
from Vistas import VistaAutenticacionPorLogin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///access.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'LzhYpdKwoNOKwPMxLbsxsHL8x63YkQ54'
app.config['PROPAGATE_EXCEPTIONS'] = True
#dashboard.config.init_from(file='/api_gateway_config.cfg')

#dashboard.bind(app)

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaAutenticacionPorLogin,'/autenticacionporlogin/login')

#jwt = JWTManager(app) using pure JWT actions with PyJWT!

