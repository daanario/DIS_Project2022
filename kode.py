#DATABASE CONFIG#######################################
import json
from psycopg2 import sql, connect
import pandas as pd
from flask import Flask, request, render_template, session, flash




with open('config.json') as jsonfile:
    CONFIG = json.load(jsonfile)


conn = connect(dbname=CONFIG["DATABASE"]["dbname"],
        user=CONFIG["DATABASE"]["user"],
        host=CONFIG["DATABASE"]["host"],
        password=CONFIG["DATABASE"]["password"])
cur = conn.cursor()




### OPENS A SQL FILE AND EXECUTES IT 
with open("schema.sql") as init_db: 
    sql_init = init_db.read()
    cur.execute(sql.SQL(sql_init))
    # print(sql_init)

### INSERT CSV INTO SQL DB 
df = pd.read_csv(CONFIG["PATHS"]["PASSWORD_DATA"], delimiter=';')
df = df.fillna(0)
df = df.to_numpy()


# # Inserting in Database 
for x in df: 
    vals = tuple(x)
    sql_string = f"""INSERT INTO public.Country (Password_key,
                                                country_code, 
                                                Country,  
                                                Rank,
                                                Password,
                                                User_count, 
                                                Time_to_crack, 
                                                Global_rank, 
                                                Time_to_crack_in_seconds
                    ) VALUES {vals};"""
    cur.execute(sql.SQL(sql_string))


    


