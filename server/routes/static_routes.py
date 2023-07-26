
from config import api
from flask_restful import Resource


class Home(Resource):
    def get(self):
        return {"message": "Hello World"}, 200


api.add_resource(Home, "/api")
