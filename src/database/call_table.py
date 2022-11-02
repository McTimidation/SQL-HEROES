import psycopg
from psycopg import sql
from connection import create_connection, execute_query

def table_query():
        print('Enter Table Name:')
        table_name = input()
        query = sql.SQL("""
                SELECT * FROM {}
                """).format(sql.Identifier(table_name))
        item_list = execute_query(query).fetchall()
        for record in item_list:
                print(record)

table_query()




