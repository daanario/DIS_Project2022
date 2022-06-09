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
    sql_string = f"""SELECT Password, User_count, Time_to_crack
                        FROM Country c
                        WHERE c.country='{country}'
                        ;"""
    print(sql_string)

    cur.execute(sql.SQL(sql_string))

    data = cur.fetchall()
    Passwordlst = []
    UserCountlst = []
    CrackTimelst = []
    for i in range(len(data)): 
        Passwordlst.append(data[i][0])
    for i in range(len(data)): 
        UserCountlst.append(data[i][1])
    for i in range(len(data)): 
        CrackTimelst.append(data[i][2])
    return Passwordlst, UserCountlst, CrackTimelst




def CountriesWithPassword(password):
    print(password)
    sql_string = f"""SELECT DISTINCT Country
                        FROM Country c
                        WHERE Password='{password}'
                        ;"""
    print(sql_string)

    cur.execute(sql.SQL(sql_string))

    data = cur.fetchall()
    lst = []
    for i in range(len(data)): 
        lst.append(data[i][0])
    return lst
