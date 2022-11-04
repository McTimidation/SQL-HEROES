from connection import execute_query

def show_hero_abilities():
    hero_name = input('Enter hero name to show their abilities: ')
    query = """
            SELECT h1.name, abt.name AS ability
            FROM abilities a
            INNER JOIN heroes h1
            ON a.hero_id=h1.id
            INNER JOIN ability_types abt
            ON abt.id=a.ability_type_id
            WHERE h1.name=%s
            """
    hero_abilities = execute_query(query, (hero_name,))
    for record in hero_abilities:
        print(record)

show_hero_abilities()

