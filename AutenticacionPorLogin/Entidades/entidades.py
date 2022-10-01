from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(50))
    services = db.relationship('Service', cascade='all, delete, delete-orphan')

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_name = db.Column(db.String(50))
    access_type = db.Column(db.String(5))



class ServiceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Service
        include_relationships = True
        load_instance = True
        #exclude = ("id",)

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        exclude = ("password",)
    services = fields.List(fields.Nested(ServiceSchema()))

class UserLoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)