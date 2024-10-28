from apitest.src.configs.host_config import API_HOSTS
import requests
import os
import json
from requests_oauthlib import OAuth1


class RequestUtility(object):
    def __init__(self) -> None:
        self.env = os.environ.get('ENV', 'test')
        # self.base_url = "http://localhost:10000/wp-json/wc/v3"
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1("", "")
    
    def post(self, endpoint, payload=None, headers=None, expected_status_code =200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        
        import pdb; pdb.set_trace()
        res_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        
        self.status_code = res_api.status_code
        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code} but actual {self.status_code}'
        # import pdb; pdb.set_trace()
        return res_api.json()
        
    def get(self):
        pass