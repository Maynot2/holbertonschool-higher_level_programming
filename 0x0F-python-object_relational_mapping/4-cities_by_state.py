#!/usr/bin/python3

"""
    Lists all cities from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == '__main__':
    creds = sys.argv[1:]

    db = MySQLdb.connect(
            host='localhost',
            user=creds[0],
            passwd=creds[1],
            db=creds[2]
    )
    cur = db.cursor()
    cur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                """)
    rows = cur.fetchall()
    for row in rows:
        print('{}'.format(row))
    cur.close()
    db.close()
