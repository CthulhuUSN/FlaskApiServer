from marshmallow_jsonapi import Schema, fields

class Post:
    def __init__(self, id, name, current_time, message):
        self.id = id
        self.name = name
        self.current_time = current_time
        self.message = message

class EndPointSchema(Schema):
    class Meta:
        type_ = 'heartbeat'
        self_view = 'device'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'devices'

    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    current_time = fields.Integer()
    message = fields.Str()

post = Post(id="1", name="Test Device", current_time=1700, message="Thump")
print(EndPointSchema().dump(post))