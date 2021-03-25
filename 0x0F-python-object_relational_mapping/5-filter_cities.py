#!/usr/bin/python3

"""
    Lists all cities from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == '__main__':
    creds = sys.argv[1:5]
    state = sys.argv[-1]

    db = MySQLdb.connect(
            host='localhost',
            user=creds[0],
            passwd=creds[1],
            db=creds[2]
    )
    cur = db.cursor()
    cur.execute("""
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                """, (state, ))
    output = ''
    rows = cur.fetchall()
    for row in rows:
        output += row[0] + ', '
    print('{}'.format(output[0:-2]))
    cur.close()
    db.close()
