from connection import create_connection, execute_query

def new_hero():
    hero_name = input('Enter New Hero Name: ')
    hero_tagline = input('Give your hero a catch phrase: ')
    hero_bio = input('Give your hero a backstory: ')
    query = """
            INSERT INTO heroes (name, about_me, biography)
            VALUES (%s, %s, %s);
            """
    execute_query(query,(hero_name, hero_tagline, hero_bio))
    print("'"+hero_name+"'" + " added as new hero")

new_hero()
