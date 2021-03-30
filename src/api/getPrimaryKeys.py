from flask_restful import Resource
from db import example

class getPrimaryKeys(Resource):

    def get(self):
        return example.getCount()
