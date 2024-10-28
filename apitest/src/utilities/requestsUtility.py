from apitest.src.configs.host_config import API_HOSTS
import requests
import os

class RequestUtility(object):
    def __init__(self) -> None:
        self.env = os.environ.get('ENV', 'test')
        # self.base_url = "http://localhost:10000/wp-json/wc/v3"
        self.base_url = API_HOSTS[self.env]
    
    def post(self, endpoint, payload=None, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        import json
        import pdb; pdb.set_trace()
        res_api = requests.post(url=url, data=json.dumps(payload), headers=headers)
        
    
    def get(self):
        pass