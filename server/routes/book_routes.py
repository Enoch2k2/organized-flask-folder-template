
from config import api
from flask_restful import Resource
from flask import make_response
import ipdb


class Books(Resource):
    def get(self):
        ipdb.set_trace()
        return {"books": "alot of them"}, 200


api.add_resource(Books, "/api/books")
