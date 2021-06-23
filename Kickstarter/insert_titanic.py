import pandas as pd
import sqlite3
import psycopg2

# Query for Titanic
SELECT_ALL_TITANIC =  """SELECT * FROM record"""
CREATE_TABLE_TITANIC =  """CREATE TABLE IF NOT EXISTS titanic (
        index SERIAL PRIMARY KEY, 
        Survived INT,
        Pclass INT,
        Name VARCHAR(200),
        Sex VARCHAR(15),
        Age INT,
        Siblings_or_spouse INT,
        Parents_or_children INT,
        Fare REAL
     )
"""

# DATA FOR ONELINE DATABASE 
user = "kghxpdqj"
dbname = "kghxpdqj"
password = "KuPLbMD64zVSshZPQC2IiXcTJ6vrCCsK"
host = "queenie.db.elephantsql.com"

 
# Connection to Online Database
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()


# READ IN Titanic Dataset into Local SQL
df_titanic = pd.read_csv('titanic.csv')
df_titanic['Name'].replace("''","", inplace=True)



# Local Key and Connection
conn_titanic = sqlite3.connect('titanic.sqlite3')
df_titanic.to_sql('review', con=conn_titanic, if_exists="replace")
sql_curs_titanic = conn_titanic.cursor()
sql_result_titanic = sql_curs_titanic.fetchall()


# Iterate Over Dataframe and Create a List of Tuple
list_tuple= []

for row in df_titanic.itertuples(index=False):
    list_tuple.append(row)

print(list_tuple)


# Generic Execution Function for Queries
def execute_query(curs, query):
    table = curs.execute(query)
    return table

# Insert the 
def get_the_table(pg_curs, list_tuple):
    for character in list_tuple:
        insert_statement = """INSERT INTO titanic(
        Survived, Pclass, Name, Sex, Age, Siblings_or_spouse, Parents_or_children, Fare)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        pg_curs.execute(insert_statement, character)
    pg_conn.commit()
    return 

# SQL object of grabbing the character master table from the local sql database
# list_rpg = execute_query(sql_curs, SELECT_ALL_RPG)
# table_rpg = execute_query(sql_curs, SELECT_ALL_RPG).fetchall()

# data.replace("\",""," regex=True, inplace=True)