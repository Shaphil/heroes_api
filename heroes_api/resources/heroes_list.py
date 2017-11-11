from flask_restful import Resource, fields, marshal_with

from heroes_api.models.hero import Hero

hero_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'url': fields.Url(endpoint='hero_api')
}


class HeroApi(Resource):
    @marshal_with(hero_fields)
    def get(self, id):
        hero = Hero.query.filter_by(id=id).first()
        return hero


class HeroesListApi(Resource):
    @marshal_with(hero_fields)
    def get(self):
        heroes = Hero.query.all()
        return heroes
