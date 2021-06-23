"""SQLAlchemy models (schema) for twitoff"""
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import numpy as np
import json

DB = SQLAlchemy()

class Record(DB.Model):
    """Campaign  data"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    backers_count = DB.Column(DB.Integer)
    category = DB.Column(DB.UnicodeText())
    goal = DB.Column(DB.Integer)
    pledged = DB.Column(DB.Integer)
    spotlight = DB.Column(DB.Integer)
    state = DB.Column(DB.Integer)
    blurb_length = DB.Column(DB.Integer)
    goal_in_usd = DB.Column(DB.Integer)
    campaign_duration = DB.Column(DB.Integer)
    sub_category = DB.Column(DB.UnicodeText())
    
    def __repr__(self):
        return f"<User: {self.text}>"
# A special parser for the jason column named category in many datasets
# def CustomParser(data):
#     if data is not np.NaN:
#         try:
#             j1 = json.loads(data)
#             return j1['name']
#         except:
#             return data.split(":",1)[1].replace('"',"")

# Creates Table
# Similar to saying `CREATE TABLE tweet ...` in SQL


# Look up SQLite connection
df = pd.read_csv("KickstarterCleanedv4.csv")
# conn = 
# df.to_sql('Kickstarter', )

# Local Key and Connection
conn = sqlite3.connect('db.sqlite3')
df.to_sql('record', con=conn, if_exists="replace")
curs = conn.cursor()
result = curs.fetchall()


# Iterate Over Dataframe and Create a List of Tuple
list_tuple= []

for row in df.itertuples(index=False, name = None):
    list_tuple.append(row)

# print(list_tuple)



