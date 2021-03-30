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


class AuthenticateAndAdd(Resource):

    def post(self,param1):
        args = parser.parse_args()
        session_key = args['session_key']
        print(session_key)
        con = connect()
        cur = con.cursor()
        cur.execute("Select session_key from users where session_key = '{}'".format(session_key))
        query_session_key = None
        query_session_key = (cur.fetchall())
        if query_session_key != None:
            # valid entry
            candy_name = param1
            cur.execute(
                "INSERT INTO candy(competitorname) VALUES ('{}')".format(candy_name))
            cur.execute("Select id from candy where competitorname= '{}'".format(candy_name))

            pk_candy = cur.fetchall()[0][0]
            cur.close()
            return {
                "status":200,
                "message": 'added successfully',
                "candy_primary_key":pk_candy
            }


        else:
            cur.close()
            return {
                "error_message":"session_key is invalid"
            }

