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


class LogoutController(Resource):

    def post(self):
        args = parser.parse_args()
        print(args)
        if 'session_key' not in args:
            return {
                "status":500,
                "error_message": "not logged in"
            }
        session_key = args['session_key']

        print('session_key = ',session_key)
        con = connect()
        cur = con.cursor()
        cur.execute("select session_key from users where session_key = '{}'".format(session_key))
        query_session_key = ''
        query_session_key = (cur.fetchall())

        print(query_session_key)
        if query_session_key == [(session_key,)]:
            cur.execute("Update users set session_key = '{0}' where session_key = '{1}'".format(None, session_key))
            cur.close()
            return {
                "status": 200,
                "message": "user logged out"
            }
        else:
            cur.close()
            return {
                "error_message": "error"
            }
