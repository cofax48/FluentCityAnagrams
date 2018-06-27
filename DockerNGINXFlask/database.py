#This script creates a postgres database hosted in docker container and uploads data from
#the dictionary text file to populate the database
####################################################################################
import os
from sqlalchemy import create_engine
import pandas as pd


#local variables stored in the os env
user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = 'db'
port = '5432'
engine = create_engine('postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db))
conn = engine.connect()

#runs once to intialize the database
def table_initialization(columns):
    conn.execute('''CREATE TABLE "Dictionary" ("Index" varchar(50) NOT NULL, PRIMARY KEY ("Index"));''')
    for column in columns:
        if column != 'Index':
            conn.execute('''ALTER TABLE "Dictionary" ADD COLUMN "{}" VARCHAR(50);'''.format(str(column)))

#runs to transfer data from csv to postgres DB
def data_insertion(df):
    #keeps track of progress
    counter = 0
    for index, row in df.iterrows():
        conn.execute('''INSERT INTO "Dictionary" VALUES ('{}', '{}','{}');'''.format(counter, row["Word"], row["word_length"]))
        counter += 1
        #Prints out occasional progress report
        if counter % 20000 == 0:
            print(row["Word"], row["word_length"])

def init_db():
    # Builds the database with init_db() on docker-compose build and initializes
    #the db fields for the flask api
    #gets data from csv
    #imports the text file as a pandas datafram object-not the fastest format-but certainly the easiest to work with later on
    df = pd.read_csv('dictionary.txt', sep=" ", dtype=str, header=None)
    #adds a column name-Word
    df.rename(columns={0:"Word"}, inplace=True)
    #Makes all items in the word column strings-initially imported as floats
    df["Word"] = df["Word"].astype(str)
    #generates a word_length column that has the length of every word in the dictionary
    df["word_length"] = df["Word"].apply(len)
    columns = df.columns.values
    #runs once to intialize the database
    table_initialization(columns)
    #runs to transfer data from csv to postgres DB
    data_insertion(df)
