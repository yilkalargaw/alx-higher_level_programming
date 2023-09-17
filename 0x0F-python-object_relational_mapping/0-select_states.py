#!/usr/bin/python3
"""list all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    thedb = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3]).cursor()

    thedb.execute("SELECT * FROM states ORDER BY states.id ASC;")

    states = thedb.fetchall()
    for i in states:
        print(i)
