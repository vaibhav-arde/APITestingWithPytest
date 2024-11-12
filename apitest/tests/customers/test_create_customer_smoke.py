import pytest
import logging as logger
from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.helpers.customers_helper import CustomerHelper
from apitest.src.dao.customers_dao import CustomersDAO
from apitest.src.utilities.requestsUtility import RequestUtility


@pytest.mark.customers
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
    
    # Verify email in the response
    assert cust_api_info['email'] == email, f"Create Customer api returned wrong email. Email should be : {email}"
    assert cust_api_info['first_name'] == '', f"Create Customer api returned wrong first_name. First name should be : ''"
    
    # Verify customer is created in database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    
    id_in_api = cust_api_info['id']
    id_ib_db = cust_info[0]['ID']
    assert id_in_api == id_ib_db, f"Create customer response 'id' is not same as 'ID' in database." \
                                    f"Email: {email}"
    
    # import pdb; pdb.set_trace()
    
    
@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    
    # Get existing email from DB
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']
    
    req_utility = RequestUtility()
    payload = {"email": existing_email, "password": "Password1"}
    cust_api_info = req_utility.post(endpoint='customers', payload=payload, expected_status_code=400)
    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with "\
        f"Existing user error 'code' is not correct. Expected: 'registration-error-email-exists', Actual:{cust_api_info['code']}"
    
    assert 'An account is already registered with your email address.' in cust_api_info['message'], f"Create customer with "\
        f"Existing user error 'code' is not correct. Expected: 'An account is already registered with your email address.', Actual:{cust_api_info['message']}"
    # import pdb; pdb.set_trace()