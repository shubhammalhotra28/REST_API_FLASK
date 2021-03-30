from flask import Flask
from flask_restful import Resource, Api
# from api.hello_world import HelloWorld
from api.check import check
from api.getPrimaryKeys import getPrimaryKeys
from api.list_details import list_details
from api.get_details import get_details
from api.get_singular import get_details_singular
from api.LoginController import loginController
from api.LogoutController import LogoutController
from api.AuthenticateAndAdd import AuthenticateAndAdd
from api.AuthenticateAndDelete import AuthenticateAndDelete
from api.AuthenticateAndUpdate import AuthenticateAndUpdate


app = Flask(__name__)
api = Api(app)

# api.add_resource(HelloWorld, '/')
api.add_resource(check,'/')
api.add_resource(getPrimaryKeys,'/list_all_keys')
api.add_resource(list_details,'/list_details')
api.add_resource(get_details_singular,'/get_details/<string:param1>')
api.add_resource(get_details,'/get_details/<string:param1>&<string:param2>')

# REST -2
api.add_resource(loginController,'/login')
api.add_resource(LogoutController,'/logout')
api.add_resource(AuthenticateAndAdd,'/addCandy/<string:param1>')
# api.add_resource(AuthenticateAndAdd,'/addCandy/<string:param1>')
api.add_resource(AuthenticateAndDelete,'/deleteCandy/<string:param1>')
api.add_resource(AuthenticateAndUpdate,'/update/<string:param1>&<string:param2>')


if __name__ == '__main__':
    app.run(debug=True)