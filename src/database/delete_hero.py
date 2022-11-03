from connection import execute_query

def delete_hero():
    remove_name = input('Enter name of Hero to Delete: ')
    query = """DELETE FROM HEROES
            WHERE name = %s"""
    execute_query(query, (remove_name,))
    print("'"+remove_name+"'"+' deleted from existence')

delete_hero()
