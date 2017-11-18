from flask_restful import Resource, fields, marshal_with, reqparse, abort

from heroes_api import db
from heroes_api.models.hero import Hero

hero_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'url': fields.Url(endpoint='hero_api')
}

parser = reqparse.RequestParser()
parser.add_argument('name')


class HeroApi(Resource):
    @marshal_with(hero_fields)
    def get(self, id):
        hero = Hero.query.filter_by(id=id).first()
        return hero

    @marshal_with(hero_fields)
    def put(self, id):
        hero = Hero.query.get(id);
        args = parser.parse_args()
        hero.name = args['name']
        db.session.commit()
        return hero, 200

    def delete(self, id):
        hero = Hero.query.get(id)
        if hero:
            db.session.delete(hero)
            db.session.commit()
            return 200

        return abort(400)


class HeroesListApi(Resource):
    @marshal_with(hero_fields)
    def get(self):
        heroes = Hero.query.all()
        return heroes

    @marshal_with(hero_fields)
    def post(self):
        args = parser.parse_args()
        name = args['name']
        if name:
            hero = Hero(name=name)
            db.session.add(hero)
            db.session.commit()
            return hero, 201

        return abort(400)
