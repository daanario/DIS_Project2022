from kode import cur
from psycopg2 import sql, connect
import pandas as pd


def distinct_country():
    sql_string = f"""SELECT DISTINCT country
                        FROM Country;"""

    cur.execute(sql.SQL(sql_string))

    data = cur.fetchall()
    lst = []
    for i in range(len(data)): 
        lst.append(data[i][0])
    return lst
def top200passwords(country):
    print(country)
    sql_string = f"""SELECT Password
                        FROM Country c
                        WHERE c.country='{country}'
                        ;"""
    print(sql_string)

    cur.execute(sql.SQL(sql_string))

    data = cur.fetchall()
    lst = []
    for i in range(len(data)): 
        lst.append(data[i][0])
    return lst
print(distinct_country())


