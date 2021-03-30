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


class loginController(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        # hashlib.new('ripemd160')
        hash_object = hashlib.sha256(str(password).encode('utf-8'))

        # hashing = hashlib.sha256(str(password)).encode('utf-8')
        hashedPassword = hash_object.hexdigest()
        # print('username : ',username,'password :',hashedPassword)
        con = connect()
        cur = con.cursor()
        # print(hashedPassword)
        # if present:
        cur.execute("Select username,password from users where username = '{}'".format(username))
        result = cur.fetchall()
        if result == None:
            sess = hashlib.sha256(str(hashedPassword).encode('utf-8'))
            sessionKey = sess.hexdigest()
            cur.execute(
                "INSERT INTO users(username,password,session_key) VALUES (%s,%s,%s)",
                (username, hashedPassword, sessionKey))
            con.commit()
            json_ans = {
                'status': 200,
                'session_key': sessionKey
            }
            return json_ans
        else:

            print(result)
            if result != [(str(username), str(hashedPassword))]:
                # [(str(username), str(hashedPassword))]
                print(result)
                return {"error_message":"invalid login data"}
            else:
                sess = hashlib.sha256(str(hashedPassword).encode('utf-8'))
                sessionKey = sess.hexdigest()
                cur.execute("Update users Set session_key = '{0}' where username = '{1}'".format(sessionKey,username))
                con.commit()

        json_ans = {
            'status' : 200,
            'session_key': sessionKey
        }
        cur.execute('select * from users')
        a = cur.fetchall()
        print(a)
        cur.close()
        return json_ans



