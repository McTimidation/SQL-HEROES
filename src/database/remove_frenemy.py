from connection import execute_query

def remove_connection():
    query1 = """
            SELECT id, name FROM heroes
            """
    hero_id_list = execute_query(query1).fetchall()
    for record in hero_id_list:
        print(record)
    execute_query(query1)
    print('Pick two heros to destroy their relationship')
    hero_input1 = input('Enter ID of first hero: ')
    hero_input2 = input('Enter ID of second hero: ')

    query2 = """
            DELETE FROM relationships
            WHERE (hero1_id = %(hero1)s) OR (hero1_id = %(hero2)s)
            AND (hero2_id = %(hero2)s) OR (hero2_id =%(hero1)s);
            """
    try:
        execute_query(query2, {'hero1':hero_input1, 'hero2':hero_input2})
        print('relationship eradicated')
    except OSError as e:
        print('Error: ', e)

remove_connection()
