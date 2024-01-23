import mysql.connector
import jwt
from flask import Flask, make_response, jsonify, request
from flask_cors import CORS, cross_origin
from functools import wraps


db = mysql.connector.connect(
  host='localhost',
  user='verzel',
  password='verzel',
  database='verzel'
)

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)
app.config['SECRET_KEY'] = '\x1d\xc9\x0b$h\x8c\x83\xa1\x16\xd9C\xb2'

def token_required(func):
  @wraps(func)
  def decorated(*args, **kwargs):
    token = request.args.get('token')
    if not token:
      return make_response(
        jsonify({'Alert': 'Token is missing!'}),
        403
        )
    payload = jwt.decode(token, app.config['SECRET_KEY'], ['HS256'])
    func()
    
  return decorated

from api.routes.vehicles import vehicle_api
from api.routes.users import user_api

app.register_blueprint(vehicle_api, url_prefix='/api/vehicles')
app.register_blueprint(user_api, url_prefix='/api/users')

if __name__ == '__main__':
  app.run()
