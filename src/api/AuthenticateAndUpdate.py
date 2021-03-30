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



class AuthenticateAndUpdate(Resource):

    def post(self,param1,param2):

        a = param1.split('%20')
        res = ''
        for i in a[:-1]:
            res = res + i
            res = res + ' '
        res = str(res) + str(a[-1])
        print(res)
        param1 = res
        print('param1 = ',param1)
        print('param2 = ',param2)
        args = parser.parse_args()
        session_key = args['session_key']
        con = connect()
        cur = con.cursor()
        cur.execute("Select session_key from users where session_key = '{}'".format(session_key))
        query_session_key = None

        query_session_key = (cur.fetchall())
        if query_session_key != None:
            # valid entry
            candy_name = param1
            win_percent = param2
            cur.execute("Update candy set winpercent = '{0}' where competitorname = '{1}'".format(win_percent, candy_name))

            cur.execute("Select id from candy where competitorname= '{}'".format(candy_name))
            # res = cur.fetchall()
            # print('res = ',res)
            pk_candy = cur.fetchall()
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
