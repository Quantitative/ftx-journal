import hmac
import requests
import time
from dateutil.parser import parse
from client import FtxClient


class ftx_tracker():

    def __init__(self):
        self.key                = "M5cZ4pgbCutRKT5UbLXQdmfxEpGAWt_P8a4d3u4W"
        self.secret             = "2P8weUIPJiH8CTKg6FLdfiEmZTsfqd-udsNTkZTg"
        self.client             = FtxClient(api_key=self.key, api_secret=self.secret)
        self.base_url           = "https://ftx.com/api"
        self.endpoint_account   = "/account"

        self.headers            = {}

        self.get_account()


    def get_account(self):
        data = self.client.get_balances()


        print(data)

ftx_tracker()


    
