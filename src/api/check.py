from flask_restful import Resource

class check(Resource):

    def get(self):
        json = {'status':200}
        return json
