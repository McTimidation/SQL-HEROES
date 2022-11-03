import psycopg
from psycopg import sql
from connection import create_connection, execute_query

def table_query():
        query1 = """SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;"""
        table_list = execute_query(query1).fetchall()
        for record in table_list:
                print(record)
        print('Enter Table Name from List Above:')
        table_name = input()
        query2 = sql.SQL("""
                SELECT * FROM {}
                """).format(sql.Identifier(table_name))
        item_list = execute_query(query2).fetchall()
        for record in item_list:
                print(record)

table_query()




