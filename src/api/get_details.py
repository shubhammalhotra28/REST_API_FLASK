from flask_restful import Resource

from db import example

class get_details(Resource):

    def get(self,param1,param2):
        # print(os.path.abspath(os.getcwd()))
        name = param1 + ' ' + param2
        return example.get_particular_candy_detail(name)