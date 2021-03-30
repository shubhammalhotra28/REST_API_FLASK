import os
from .swen344_db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/schema.sql')

def getCount():
    con = connect()
    cur = con.cursor()
    cur.execute('Select id from candy')
    ans = cur.fetchall()
    # print(ans)
    con.commit()
    con.close()

    return_ans = {
        "all_primary_keys":ans
    }
    return return_ans


def list_details():
    con = connect()
    cur = con.cursor()
    cur.execute('Select * from candy')

    ans = cur.fetchall()
    return_ans = {}
    for i in range(len(ans)):
        # i0 = competitorname
        val = ans[i][1:]
        return_ans[ans[i][0]] = {
            'competitorname': ans[i][1],
            'chocolate': ans[i][2],
            'fruity': ans[i][3],
            'caramel': ans[i][4] ,
            'peanutyalmondy': ans[i][5],
            'nougat': ans[i][6],
            'crispedricewafer': ans[i][7],
            'hard': ans[i][8],
            'bar': ans[i][9],
            'pluribus': ans[i][10],
            'sugarpercent': str(ans[i][11]),
            'pricepercent': str(ans[i][12]),
            'winpercent': str(ans[i][13])
        }
    con.commit()
    con.close()

    return return_ans


def get_particular_candy_detail(name):
    con = connect()
    cur = con.cursor()
    print('**************',name)
    cur.execute("Select * from candy where competitorname = '{0}'".format(name))
    # cur.execute("Select * from candy where competitorname = '{}'".format(name))
    ans = cur.fetchall()
    return_ans = {}
    return_ans[ans[0][0]] = {
        'competitorname': ans[0][1],
        'chocolate': ans[0][2],
        'fruity': ans[0][3],
        'caramel': ans[0][4],
        'peanutyalmondy': ans[0][5],
        'nougat': ans[0][6],
        'crispedricewafer': ans[0][7],
        'hard': ans[0][8],
        'bar': ans[0][9],
        'pluribus': ans[0][10],
        'sugarpercent': str(ans[0][11]),
        'pricepercent': str(ans[0][12]),
        'winpercent': str(ans[0][13])
    }

    con.commit()
    con.close()
    return return_ans

#
# def list_examples():
#     """This is an example. Please remove from your code before REST1 deadline.
#     DB layer call for listing all rows of our example.
#     """
#     return exec_get_all('SELECT id FROM candy')