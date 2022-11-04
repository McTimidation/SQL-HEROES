from connection import execute_query

def show_relationships():
    hero = input('Enter hero name to show their connections: ')
    query = """
            SELECT h1.name, h2.name, rlt.name FROM relationships r
            INNER JOIN heroes h1
            ON h1.id=r.hero1_id
            RIGHT JOIN heroes h2
            ON h2.id=r.hero2_id
            INNER JOIN relationship_types rlt
            ON rlt.id=r.relationship_type_id
            WHERE h1.name = %s
            """
    relationship_list = execute_query(query, (hero,))
    for record in relationship_list:
        print(record)


show_relationships()

