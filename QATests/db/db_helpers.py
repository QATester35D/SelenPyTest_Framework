# import mysql.connector
# from QATests.db.db_config import DB_CONFIG
# from QATests.db.db_connection import get_db_connection

# def db_check_count(table_name):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     query = f"SELECT COUNT(*) FROM {table_name};"
#     cursor.execute(query)
#     result = cursor.fetchone()[0]
#     cursor.close()
#     conn.close()
#     return result

# def db_get_users_name_email():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     query = "select customer_name, email from users ORDER BY RAND() LIMIT 1;"
#     cursor.execute(query)
#     result = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return result