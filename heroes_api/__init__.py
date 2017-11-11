from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('heroes_api.settings.DevelopmentConfig')
api = Api(app)
db = SQLAlchemy(app)

from heroes_api.resources.heroes_list import HeroesListApi

api.add_resource(HeroesListApi, '/api/heroes')
