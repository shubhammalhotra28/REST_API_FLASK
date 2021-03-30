from flask_restful import Resource
from db import example

class list_details(Resource):

    def get(self):
        return example.list_details()