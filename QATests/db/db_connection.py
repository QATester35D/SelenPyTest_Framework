import mysql.connector
from QATests.db.db_config import DB_CONFIG

class DatabaseOperations:
    def __init__(self):
        self.mydb = mysql.connector.connect(**DB_CONFIG)
        self.cur = self.mydb.cursor()

    def execute_query(self, query, params=None):
        cursor=self.cur
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result

    def execute_sql_from_file(self, filepath):
        cursor=self.cur
        with open(filepath, "r") as file:
            sql_statements = file.read()
        for statement in sql_statements.split(";"):
            if statement.strip():
                cursor.execute(statement)

    def db_check_count(self, table_name):
        cursor=self.cur
        query = f"SELECT COUNT(*) FROM {table_name};"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result

    def db_get_users_name_email(self):
        cursor=self.cur
        query = "select customer_name, email from users ORDER BY RAND() LIMIT 1;"
        cursor.execute(query)
        result = cursor.fetchall()
        return result