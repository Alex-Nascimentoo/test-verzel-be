import mysql.connector
import jwt
from flask import Flask, make_response, jsonify, request, session
from flask_cors import CORS, cross_origin
from functools import wraps
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename

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
    
    # try:
    #   payload = jwt.decode(token, app.config['SECRET_KEY'], ['HS256'])
    #   func()
    # except:
    #   return make_response(
    #     jsonify({'Alert': 'Invalid token!'}),
    #     403
    #   )
  return decorated

@app.route('/login', methods=['POST'])
def login():
  if request.json['username'] and request.json['password'] == 'bolinho':
    session['logged_in'] = True

    token = jwt.encode({
      'user': request.json['username'],
      'expiration': str(datetime.utcnow() + timedelta(minutes=5))
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

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
  cursor = db.cursor()
  cursor.execute('SELECT * FROM vehicles')

  db_vehicles = cursor.fetchall()
  vehicle_list = list()

  for v in db_vehicles:
    vehicle_list.append({
      'id': v[0],
      'brand': v[1],
      'model': v[2],
      'version': v[3],
      'price': v[4],
      'color': v[5],
      'category': v[6],
      'engine': v[7],
      'transmission': v[8],
      'year': v[9],
      'km_old': v[10],
      'photo': v[11]
    })

  return make_response(
    jsonify(vehicle_list)
  )

@app.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicle_by_id(id):
  query = f"SELECT * FROM vehicles WHERE id = {id}"
  cursor = db.cursor()
  cursor.execute(query)
  
  vehicle = cursor.fetchone()

  return make_response(
    jsonify({
      'id': vehicle[0],
      'brand': vehicle[1],
      'model': vehicle[2],
      'version': vehicle[3],
      'price': vehicle[4],
      'color': vehicle[5],
      'category': vehicle[6],
      'engine': vehicle[7],
      'transmission': vehicle[8],
      'year': vehicle[9],
      'km_old': vehicle[10],
      'photo': vehicle[11]
    })
  )

@app.route('/vehicles', methods=['POST'])
@token_required
def create_vehicle():
  vehicle = request.json

  cursor = db.cursor()

  query = f"""INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old, photo) VALUES (
    '{vehicle['brand']}',
    '{vehicle['model']}',
    '{vehicle['version']}',
    '{vehicle['price']}',
    '{vehicle['color']}',
    '{vehicle['category']}',
    '{vehicle['engine']}',
    '{vehicle['transmission']}',
    '{vehicle['year']}',
    '{vehicle['km_old']}',
    '{vehicle['photo']}'
    )"""

  cursor.execute(query)
  db.commit()

  return make_response(
    jsonify(
      message = "Vehicle created successfully",
      vehicle = vehicle
    ), 201
  )

@app.route('/vehicles/<int:id>', methods=['PUT'])
@token_required
def update_vehicle(id):
  new_vehicle = request.json

  # query = f"UPDATE vehicles SET brand = '{new_vehicle['brand']}', model = '{new_vehicle['model']}', v_year = '{new_vehicle['year']}' WHERE id = {id}"
  query = f"""UPDATE vehicles 
  SET brand = '{new_vehicle['brand']}',
  model = '{new_vehicle['model']}',
  v_version = '{new_vehicle['version']}',
  price = {new_vehicle['price']},
  color = '{new_vehicle['color']}',
  category = '{new_vehicle['category']}',
  engine = '{new_vehicle['engine']}',
  transmission = '{new_vehicle['transmission']}',
  v_year = {new_vehicle['year']},
  km_old = {new_vehicle['km_old']},
  photo = '{new_vehicle['photo']}'
  WHERE id = {id}"""

  cursor = db.cursor()
  cursor.execute(query)
  db.commit()

  cursor.execute(f"SELECT * FROM vehicles WHERE id = {id}")
  updated_vehicle = cursor.fetchone()

  return make_response(
    jsonify(
      message = "Vehicle updated successfully",
      data = {
      'id': updated_vehicle[0],
      'brand': updated_vehicle[1],
      'model': updated_vehicle[2],
      'version': updated_vehicle[3],
      'price': updated_vehicle[4],
      'color': updated_vehicle[5],
      'category': updated_vehicle[6],
      'engine': updated_vehicle[7],
      'transmission': updated_vehicle[8],
      'year': updated_vehicle[9],
      'km_old': updated_vehicle[10],
      'photo': updated_vehicle[11]
    })
  )

@app.route('/vehicles/<int:id>', methods = ['DELETE'])
def delete_vehicle(id):
  cursor = db.cursor()
  cursor.execute(f"DELETE FROM vehicles WHERE id = {id}")
  db.commit()

  return make_response(
    jsonify("Vehicle deleted successfully"), 204
  )

if __name__ == '__main__':
  app.run()
