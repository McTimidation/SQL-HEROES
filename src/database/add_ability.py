from connection import create_connection, execute_query

def new_ability():
    ability_input = input('Enter New Ability: ')
    hero_input = input('Enter Hero Name: ')

    query = """
            WITH ab_id AS (
                INSERT INTO ability_types (name)
                VALUES (%s)
                RETURNING id
            ), hero_num AS (
                SELECT id FROM heroes
                WHERE name = %s
            )
            INSERT INTO abilities (hero_id, ability_type_id)
            VALUES ((SELECT id FROM hero_num), (SELECT id FROM ab_id));
            """
    try: 
        execute_query(query,(ability_input, hero_input))
        print("'"+hero_input+"'" + " given ability: "+ability_input)
    except OSError as e:
        print('Looks like that hero or ability already is assigned', e)

new_ability()
