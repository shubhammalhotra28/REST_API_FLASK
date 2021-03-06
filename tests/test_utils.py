import requests
from src.db.swen344_db_utils import connect, exec_sql_file, insert_test_data1
import csv

def insert_test_data():
    insert_test_data1('tests/candy.csv')
    # exec_sql_file('tests/test_data.sql')

def assert_sql_count(test, sql, n,
                     msg = 'Expected row count did not match query'):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    test.assertEqual(n, cur.rowcount, msg)
    conn.close()

def get_rest_call(test, url, params = {}, expected_code = 200):
    response = requests.get(url, params)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def post_rest_call(test, url, params = {}, expected_code = 200):
    response = requests.post(url, params)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

