from flask_restful import Resource
from db import example


class get_details_singular(Resource):

    def get(self,param1):
        name = param1
        return example.get_particular_candy_detail(name)