from apitest.src.configs.host_config import API_HOSTS
from apitest.src.utilities.credentialsUtility import CredentialsUtility

import requests
import os
import json
from requests_oauthlib import OAuth1
import logging as logger


class RequestUtility(object):
    def __init__(self) -> None:
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        # self.base_url = "http://localhost:10000/wp-json/wc/v3"
        self.base_url = API_HOSTS[self.env]
        
        # self.auth = OAuth1("", "")
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])
    
    def assert_status_code(self):
        assert self.res_status_code == self.expected_status_code, f"Bad status code : " \
            f"Expected status code {self.expected_status_code} but actual {self.res_status_code}, " \
                f"URL: {self.url}, Response Json: {self.res_json}"
        
    def post(self, endpoint, payload=None, headers=None, expected_status_code =200):
        if not headers:
            headers = {"Content-Type": "application/json"}
            
        self.url = self.base_url + endpoint
        
        # import pdb; pdb.set_trace()
        res_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        
        self.res_status_code = res_api.status_code
        self.expected_status_code = expected_status_code
        self.res_json = res_api.json()
        
        # import pdb; pdb.set_trace()
        self.assert_status_code()
        
        logger.debug(f"POST API Response : {self.res_json}")
        return res_api.json()
        
    def get(self, endpoint, payload=None, headers=None, expected_status_code =200):
        if not headers:
            headers = {"Content-Type": "application/json"}
            
        self.url = self.base_url + endpoint
        
        res_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.res_status_code = res_api.status_code
        self.expected_status_code = expected_status_code
        self.res_json = res_api.json()
        
        # import pdb; pdb.set_trace()
        self.assert_status_code()
        
        logger.debug(f"GET API Response : {self.res_json}")
        return res_api.json()