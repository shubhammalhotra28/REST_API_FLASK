import json
import unittest
from tests.test_utils import *
from src.db.example import rebuild_tables
import requests

class TestCandy(unittest.TestCase):

    def setUp(self):
        rebuild_tables()
        insert_test_data()

    def test_list_all_keys(self):
        details = get_rest_call(self, 'http://localhost:5000/list_all_keys')
        self.assertEqual(len(details['all_primary_keys']),85)

    def test_list_details(self):
        details = get_rest_call(self, 'http://localhost:5000/list_details')
        self.assertEqual(len(details),85)

    def test_specific_entry(self):

        expected_result =  {'7':
                                {'competitorname': 'Baby Ruth',
                                 'chocolate': True,
                                 'fruity': False,
                                 'caramel': True,
                                 'peanutyalmondy': True,
                                 'nougat': True,
                                 'crispedricewafer': False,
                                 'hard': False,
                                 'bar': True,
                                 'pluribus': False,
                                 'sugarpercent': '0.60399997',
                                 'pricepercent': '0.76700002',
                                 'winpercent': '56.914547'
                                 }
                            }


        result = get_rest_call(self, 'http://localhost:5000/get_details/Baby&Ruth')

        self.assertEqual(result,expected_result)

    def test_login(self):
        url = 'http://localhost:5000/login'
        hdr = {
            'username': 'shubham',
            'password': 'hello'
        }
        request = requests.post(url,hdr) #invalid
        response = request.json()

        self.assertEqual('invalid login data',response['error_message'])
        url = 'http://localhost:5000/deleteCandy/Chiclets'
        payload = {'session_key': 'c4fb0455f432a7176325b89b8a2003c82e41fc27a5ab07c15a64fc036e4563a4'}
        headers = {'content-type': 'application/json'}
        response = requests.delete(url,data=json.dumps(payload),headers=headers)
        response = response.json()
        self.assertEqual(response, {'status': 200, 'message': 'record deleted sucessfully'})

        payload = {'session_key': None}
        headers = {'content-type': 'application/json'}
        response = requests.delete(url, data=json.dumps(payload), headers=headers)
        response = response.json()
        self.assertEqual(200, response['status'])

        url = 'http://localhost:5000/logout'
        content = {
            'session_key': 'c4fb0455f432a7176325b89b8a2003c82e41fc27a5ab07c15a64fc036e4563a4'
        }
        request = requests.post(url, content)  # valid
        response = request.json()
        self.assertEqual(200, response['status'])

        url = 'http://localhost:5000/logout'
        request = requests.post(url)  # invalid
        response = request.json()

        self.assertEqual(response, {'error_message': 'error'})

        data = {'session_key': 'c4fb0455f432a7176325b89b8a2003c82e41fc27a5ab07c15a64fc036e4563a4'}
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        # / addCandy / < string: param1 >
        url = "http://localhost:5000/addCandy/BertieBottsBeans"
        r = requests.post(url, headers=headers, json=data)
        r = r.json()
        self.assertEqual(r,{'status': 200, 'message': 'added successfully', 'candy_primary_key': 86})

        url = "http://localhost:5000/update/Haribo%20Twin%20Snakes&20.1"
        data = {'session_key': 'c4fb0455f432a7176325b89b8a2003c82e41fc27a5ab07c15a64fc036e4563a4'}
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        r = requests.post(url,headers=headers,json=data)
        r = r.json()
        self.assertEqual( {'status': 200, 'message': 'added successfully', 'candy_primary_key': [[22]]},r)




