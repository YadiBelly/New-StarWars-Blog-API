"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def get_user():
    user = User.query.all()
    user_list = list(map(lambda x: x.serialize(), user))
    return jsonify(user_list), 200


@app.route('/users/favorites', methods=['GET'])
def get_favoriteUser():
    favorite = Favorites.query.all()
    favorite_list = list(map(lambda x: x.serialize(), favorite))
    return jsonify(favorite_list), 200


@app.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    people_list = list(map(lambda x: x.serialize(), people))
    return jsonify(people_list), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def get_single(people_id):
    people = People.query.get(people_id)
    return jsonify(people.serialize()), 200


@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    planets_list = list(map(lambda x: x.serialize(), planets))
    return jsonify(planets_list), 200


@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planet(planets_id):
    planets = Planets.query.get(planets_id)
    return jsonify(planets.serialize()), 200

@app.route('/favorites/planet/<int:planet_id>', methods=['POST'])
def get_Singleplanet(planet_id):
    data = request.get_json()
    id = planet_id
    add_planet = Planets(id=data["id"], orbit=data["orbit"])
    return jsonify(add_planet.serialize()), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
