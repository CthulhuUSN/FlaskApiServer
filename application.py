from flask import Flask, json

heartbeat_json = [{'data': {'type': 'heartbeat', 'attributes': {'message': 'Thump', 'name': 'Test Device', 'current_time': 1700}, 'id': 1}}]

api = Flask(__name__)

@api.route('/heartbeat', methods=['GET'])
def get_companies():
  return json.dumps(heartbeat_json)

@api.route('/heartbeat', methods=['POST'])
def post_companies():
  return json.dumps({"success": True}), 201

if __name__ == '__main__':
    api.run()