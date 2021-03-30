from flask_restful import Resource
from db import example

class HelloWorld(Resource):
    def get(self):
        # return {200}
        return (example.list_examples()).json()