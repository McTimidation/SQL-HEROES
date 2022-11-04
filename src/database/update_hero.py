from connection import execute_query
from psycopg import sql

def update_hero_bio():
    up_name = input('Enter name of hero to update their value: ')
    cat_name = input('Which attribute would you like to update? ')
    new_cat_val = input('Enter new attribute value: ')
    query = ("""
    UPDATE heroes
    SET {} = %s
    WHERE name = %s
    """).format(cat_name)
    try:
        execute_query(query, (new_cat_val, up_name))
        print(up_name+ ' updated successfully')
    except OSError as e:
        print('An error occured updating the hero')

update_hero_bio()

