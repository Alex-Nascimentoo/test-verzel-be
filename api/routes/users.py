from flask import Blueprint, request, make_response, session, jsonify
import jwt
from datetime import datetime, timedelta
from main import app

user_api = Blueprint('user_api', __name__)

@user_api.route('/login', methods=['POST'])
def login():
  if request.json['username'] and request.json['password'] == 'bolinho':
    session['logged_in'] = True

    token = jwt.encode({
      'user': request.json['username'],
      'expiration': str(datetime.utcnow() + timedelta(minutes=10))
    },
    app.config['SECRET_KEY'])

    return make_response(jsonify(
      message = 'Logged in successfully',
      token = token
    ), 200)
  else:
    return make_response('Unable to verify', 403, {
      'WWW-Authenticate': 'Basic realm: "Authentication Failed!"'
    })