from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList

# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)

# Define a class for the Artist table
#class HeartBeat(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    uname = db.Column(db.String)
#    memory_size = db.Column(db.Integer)
#    box_state = db.Column(db.String)
#    mac_addr = db.Column(db.String)
#    up_time = db.Column(db.Integer)
#    current_time = db.Column(db.Integer)

class HeartBeatTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)

# Create the table
db.create_all()

# Create data abstraction layer
class EndPointSchema(Schema):
    class Meta:
        type_ = 'endpoint'
        self_view = 'endpoint_single'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'endpoint_many'

    id = fields.Integer()
    endpoint = fields.Str(required=True)
    message = fields.Str()

# Create resource managers and endpoints
class EndpointMany(ResourceList):
    schema = EndPointSchema
    data_layer = {'session': db.session,
                  'model': HeartBeatTest}

class EndpointOne(ResourceDetail):
    schema = EndPointSchema
    data_layer = {'session': db.session,
                  'model': HeartBeatTest}

api = Api(app)
api.route(EndpointMany, 'endpoint_many', '/endpoints')
api.route(EndpointOne, 'endpoint_single', '/endpoints/<int:id>')

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)