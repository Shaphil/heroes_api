from flask_restful import Resource, fields, marshal_with

from heroes_api.models.hero import Hero

hero_fields = {
    'id': fields.Integer,
    'name': fields.String
}


class HeroesListApi(Resource):
    @marshal_with(hero_fields)
    def get(self):
        heroes = Hero.query.all()
        return heroes
