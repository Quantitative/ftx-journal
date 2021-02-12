import plotly.graph_objects as go
import psycopg2 as s3
import time
1

#For environment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class visualize():

    def __init__(self):
        self.table_name         = os.getenv("table_name")
        self.db                 = os.getenv("db")
        self.host               = os.getenv("host")
        self.user               = os.getenv("user")
        self.password           = os.getenv("password")
        self.lookback           = time.time() - (float(input("How many days data do you want to show? (you can input partial days i.e 0.5 days=12 hours)")) * 24 * 3600)

        self.plot()

    def grab_data(self):
        with s3.connect(host=self.host, database=self.db, user=self.user, password=self.password) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM {} WHERE timestamp > {}".format(self.table_name, self.lookback))
            data = cursor.fetchall()
            self.timestamps = [d[0] for d in data]
            self.balance    = [d[1] for d in data]

    def plot(self):

        self.grab_data()
        
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=self.timestamps, 
            y=self.balance, 
            marker_color="black", 
            mode="lines"))

        fig.show()

visualize()
