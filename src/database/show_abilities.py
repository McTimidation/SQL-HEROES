    
    
def show_abilities():
    query = """SELECT h.name, STRING_AGG(abt.name, ', ')
            FROM abilities a
            INNER JOIN heroes h
            ON a.hero_id=h.id
            INNER JOIN ability_types abt
            ON abt.id=a.ability_type_id
            GROUP BY h.name;
            """
