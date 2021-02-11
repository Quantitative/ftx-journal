import hmac
import requests
import time
from client import FtxClient
import psycopg2 as s3

#For environment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class ftx_tracker():

    def __init__(self):

        #FTX API details
        self.key                = os.getenv("KEY")
        self.secret             = os.getenv("SECRET")

        #Database details
        self.db                 = os.getenv("db")
        self.host               = os.getenv("host")
        self.user               = os.getenv("user")
        self.password           = os.getenv("password")
        self.table_name         = "balance"

        #Client/API connection
        self.client             = FtxClient(api_key=self.key, api_secret=self.secret)
        
        #Getting total usd and adding to database
        self.create_table()

        total_usd = self.get_account()
        self.add_data(total_usd)
        # self.show_data()


    def get_account(self):
        data = self.client.get_balances()
        usd  = sum([balance["usdValue"] for balance in data])
        
        return usd

    def create_table(self):
        with s3.connect(host=self.host, database=self.db, user=self.user, password=self.password) as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS {} (timestamp INTEGER, balance INTEGER)".format(self.table_name))
            conn.commit()

    def add_data(self, usd):
        with s3.connect(host=self.host, database=self.db, user=self.user, password=self.password) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO {} VALUES({}, {})".format(self.table_name, int(time.time()), usd))
            conn.commit()

    # def show_data(self):
    #     with s3.connect(host=self.host, database=self.db, user=self.user, password=self.password) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT * FROM {}".format(self.table_name))
    #         print(cursor.fetchall())


ftx_tracker()
