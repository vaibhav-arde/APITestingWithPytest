import pytest
import logging as logger
from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.helpers.customers_helper import CustomerHelper

@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only.")
    rand_info = generate_random_email_and_password()
    email=rand_info['email']
    password=rand_info['password']
    print("rand_info", rand_info)
    print("email", email)
    print("password", password)
    
    # # Create Payload
    # payload = {'email': email, 'password': password}
    
    # Make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password )
    
    import pdb; pdb.set_trace()
    
    # verify status code of the call
    
    # Verify email in the response
    
    # Verify customer is created in database
    