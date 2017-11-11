from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('heroes_api.settings.DevelopmentConfig')
CORS(app)
api = Api(app)
db = SQLAlchemy(app)

from heroes_api.resources.hero import HeroApi, HeroesListApi

api.add_resource(HeroApi, '/api/heroes/<id>', endpoint='hero_api')
api.add_resource(HeroesListApi, '/api/heroes')
