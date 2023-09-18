#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    def select_states():
        """Fetches and returns all states from the database"""
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        with db.cursor() as cursor:
            cursor.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
            return cursor.fetchall()

    states = select_states()
    for state in states:
        print(state)
