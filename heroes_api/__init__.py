from flask import Flask
from flask_restful import Api

from heroes_api.resources.hero import Hero

app = Flask(__name__)
api = Api(app)

api.add_resource(Hero, '/api/heroes')
