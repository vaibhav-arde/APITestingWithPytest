import pymysql
import pymysql.cursors
from apitest.src.utilities.credentialsUtility import CredentialsUtility

class DBUtility(object):
    
    def __init__(self):
        self.creds = CredentialsUtility.get_db_credentials()
        self.host = 'localhost'
        self.socket = "/Users/vaibhavarde/Library/Application Support/Local/run/PvtyQB0Kk/mysql/mysqld.sock"
    
    def create_connection(self):
        # connection = pymysql.connect(host=self.host, user=self.creds['db_user'], password=self.creds['db_password'], port=3306)
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'], 
                                     password=self.creds['db_password'],
                                     unix_socket=self.socket)
        
        return connection
    
    def execute_select(self, sql):
        conn =  self.create_connection()
        
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()
    
    def execute_sql(self, sql):
        pass