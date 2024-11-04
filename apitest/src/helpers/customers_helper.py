
from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.utilities.requestsUtility import RequestUtility

class CustomerHelper(object):
    def __init__(self):
        self.request_utility = RequestUtility()
    
    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'
            
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
        
        create_user_json = self.request_utility.post('customers', payload=payload, expected_status_code=201)
        return create_user_json