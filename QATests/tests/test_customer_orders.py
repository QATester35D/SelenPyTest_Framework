import pytest
import mysql.connector
from QATests.tests.base_test import BaseTest
from QATests.db.db_config import DB_CONFIG_SAKILA
from QATests.db.db_connection import DatabaseOperations

class TestSakilaDatabaseOperations(BaseTest):
    def __init__(self):
        self.mydb = mysql.connector.connect(**DB_CONFIG_SAKILA)
        self.cur = self.mydb.cursor()

    def execute_query(self, query, params=None):
        cursor=self.cur
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result

    def test_customer_shipping_address(self, setup_database: DatabaseOperations):
        db_helpers = setup_database
        cursor = db_helpers.cur
        query = "select first_name from customer where city_id = 463;"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        print(result)