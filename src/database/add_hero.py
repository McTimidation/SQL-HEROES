from connection import create_connection, execute_query

def new_hero():
    hero_name = input('Enter New Hero Name: ')
    hero_ability = input('Enter Hero Superpower: ')
    hero_tagline = input('Give your hero a catch phrase: ')
    hero_bio = input('Give your hero a backstory: ')
    query = """
            INSERT INTO heroes (name, about_me, biography)
            VALUES (%s, %s, %s);
            """
    execute_query(query)
    print(hero_name + "added as new hero")

new_hero()
