import json, requests
import jwt
from cryptography.hazmat.primitives import serialization
from datetime import datetime
from celery import Celery
from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from Entidades import UserSchema

from Entidades import db, User

user_schema = UserSchema()

celery_app = Celery(__name__, broker="redis://localhost:6379/0")
secret_key = "LzhYpdKwoNOKwPMxLbsxsHL8x63YkQ54"
mode = "HS256"
#mode = "RS256"

@celery_app.task(name="monitor.integrity_check")
def integrity_check(mensaje):
    pass

class VistaAutenticacionPorLogin(Resource):

    def post(self):
        user = User.query.filter(User.username == request.json["username"],
                                 User.password == request.json["password"]).first()
       
        db.session.commit()
        if user is None:
            return "Error during login", 404
        
        user_permissions = user_schema.dump(user)
        if mode=="HS256":
            jwt_token = jwt.encode(payload=user_permissions, key=secret_key) # default algorithm=HS256
        if mode=="RS256":
            private_key = open('.ssh/id_rsa', 'r').read()
            key = serialization.load_ssh_private_key(private_key.encode(), password=b'') # insert b'password' if encrypted with passcode
            jwt_token = jwt.encode(payload=user_permissions, key=key, algorithm='RS256')
        
        queued_message = dict(
            request = request.json,
            generated_token = jwt_token,
        )
        # REMOVER COMENTARIO EN INTEGRACION integrity_check.apply_async((queued_message,))
        return {"details": "Successful login", "token": jwt_token}, 200

        # decode symmetric/secret in required location with jwt.decode(token, key='my_secret', algorithms=['HS256', ])
        # decode asymmetric/public in required location with:
        # 1. from cryptography.hazmat.primitives import serialization
        # 2. public_key = open('.ssh/id_rsa.pub', 'r').read()
        # 3. key = serialization.load_ssh_public_key(public_key.encode())
        # jwt.decode(jwt=token, key=key, algorithms=['RS256', ]) or whatever algorithm

        # Don't know algorithm? use jwt.get_unverified_header(token)
        
