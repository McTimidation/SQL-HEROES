from connection import execute_query

def make_connection():
    query1 = """
            SELECT id, name FROM heroes
            """
    hero_id_list = execute_query(query1).fetchall()
    for record in hero_id_list:
        print(record)
    execute_query(query1)
    hero_input1 = input('Enter ID of first hero: ')
    hero_input2 = input('Enter ID of second hero: ')
    frenimy = input('Enter 1 for friend or 2 for Enemy: ')

    query2 = """
            INSERT INTO relationships (hero1_id, hero2_id, relationship_type_id)
            VALUES (%s, %s, %s)
            """
    execute_query(query2, (hero_input1, hero_input2, frenimy))

make_connection()
