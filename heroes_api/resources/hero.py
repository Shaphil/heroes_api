from flask_restful import Resource


class Hero(Resource):
    def get(self):
        return {'message': 'Welcome to the tour of heroes'}
