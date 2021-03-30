import hashlib
import secrets
from flask_restful import Resource
from flask_restful import reqparse
from db.swen344_db_utils import *
# from db.swen344_db_utils import connect
import json
from db import example



parser = reqparse.RequestParser()
parser.add_argument('password')
parser.add_argument('username')
parser.add_argument('session_key')
parser.add_argument('body')


class AuthenticateAndDelete(Resource):

    def delete(self,param1):
        args = parser.parse_args()
        print('123')
        print(args)
        if 'session_key' not in args:
            return {
                "status":500,
                "error_message": "not logged in"
            }

        session_key = args['session_key']
        con = connect()
        cur = con.cursor()
        cur.execute("Select session_key from users where session_key = '{}'".format(session_key))
        query_session_key = None
        query_session_key = (cur.fetchall())
        if query_session_key != None:
            candy_name = param1
            cur.execute("Delete from candy where competitorname = '{}'".format(candy_name))
            cur.close()
            return {
                "status":200,
                "message": 'record deleted sucessfully'
            }

        else:
            cur.close()
            return {
                "error_message" : "no user exist or the session_key is wrong"
            }