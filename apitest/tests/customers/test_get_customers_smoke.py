import logging as logger
import pytest
from apitest.src.utilities.requestsUtility import RequestUtility

@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtility()
    res_api = req_helper.get('customers')
    logger.debug(f"Response of list all: {res_api}")
    
    assert res_api, f"Response of list all customers is empty"
    # import pdb; pdb.set_trace()