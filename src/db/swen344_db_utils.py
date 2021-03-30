import psycopg2
import yaml
import os

def connect():
    config = {
        'database': 'swen344',
        'user': 'swen344',
        'password': 'Shubham@1413',
        'host': 'localhost',
        'port': '5432'
    }
    yml_path = os.path.join(os.path.dirname(__file__), '../../config/db.yml')
    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])

def exec_sql_file(path):
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()

def exec_get_one(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

def exec_get_all(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    # https://www.psycopg.org/docs/cursor.html#cursor.fetchall
    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples

def exec_commit(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result


def insert_test_data1(path):
    import csv
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')

    con = connect()
    cur = con.cursor()

    files = []


    with open(full_path, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            files.append(row)
    files = files[1:]
    for i in range(len(files)):
        competitorname = files[i][0]
        chocolate = files[i][1]
        fruity = files[i][2]
        caramel = files[i][3]
        peanutyalmondy = files[i][4]
        nougat = files[i][5]
        crispedricewafer = files[i][6]
        hard = files[i][7]
        bar = files[i][8]
        pluribus = files[i][9]
        sugarpercent = files[i][10]
        pricepercent = files[i][11]
        winpercent = files[i][12]

        try:
            cur.execute("INSERT INTO candy (competitorname,chocolate,fruity,caramel,peanutyalmondy,nougat,crispedricewafer,hard,bar,pluribus,sugarpercent,pricepercent,winpercent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (competitorname,chocolate,fruity,caramel,peanutyalmondy,nougat,crispedricewafer,hard,bar,pluribus,sugarpercent,pricepercent,winpercent))
        except Exception as e:
            con = connect()
            cur = con.cursor()
            cur.execute("INSERT INTO candy (competitorname,chocolate,fruity,caramel,peanutyalmondy,nougat,crispedricewafer,hard,bar,pluribus,sugarpercent,pricepercent,winpercent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (competitorname,chocolate,fruity,caramel,peanutyalmondy,nougat,crispedricewafer,hard,bar,pluribus,sugarpercent,pricepercent,winpercent))

        con.commit()
        con.close()
