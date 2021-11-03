from flask_restx import Resource, Namespace
from flask import request

from conteiner import movie_service
from dao.model.movie import MovieSchema
from setup_db import db



movies_ns = Namespace('movie')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return movie_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201




@movies_ns.route('/<int:uid>')
class MoviesView(Resource):
    def get(self, uid:int):
        movie = movie_service.get_one(uid)
        if not movie:
            return 'Такого фильма нету', 404
        return movie_schema.dump(movie), 200

    def put(self,uid):
        req_json = request.json
        req_json['uid'] = uid
        movie = movie_service.update(req_json)
        return '', 204

    def delete(self, uid:int):
        movie = movie_service.delete(uid)






