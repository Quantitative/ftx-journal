import hmac
import requests
import time


#For environment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class ftx_tracker():

    def __init__(self):
        self.key                = os.getenv("KEY")
        self.secret             = os.getenv("SECRET")
        self.base_url           = "https://ftx.com/api"
        self.endpoint_all_bal   = "/wallet/all_balances"

        self.headers            = {}


    #Sets headers for authentication
    def ftx_auth(self)
        ts = int(time.time() * 1000)
        request = Request('GET', self.endpoint)
        prepared = request.prepare()
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
        signature = hmac.new(self.key.encode(), signature_payload, 'sha256').hexdigest()

        self.headers['FTX-KEY']  = self.secret
        self.headers['FTX-SIGN'] = signature
        self.headers['FTX-TS']   = str(ts)


    
