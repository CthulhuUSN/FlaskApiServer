from flask import Flask, json, request

api = Flask(__name__)

data = {"initial_data": True}

@api.route('/heartbeat', methods=['GET'])
def get_request():
  return json.dumps(data)

@api.route('/heartbeat', methods=['POST', 'PATCH'])
def post_request():
  return json.dumps({"success": True}), 201

if __name__ == '__main__':
    api.run()
