from apitest.src.utilities.dbUtility import DBUtility

class CustomersDAO(object):
    
    def __init__(self) -> None:
        self.db_helper = DBUtility()
    
    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        # import pdb; pdb.set_trace()
        return rs_sql