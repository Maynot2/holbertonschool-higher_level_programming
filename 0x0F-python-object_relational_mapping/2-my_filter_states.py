#!/usr/bin/python3

"""
    Lists matching given state from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY {}".format(state))
    rows = cur.fetchall()
    for row in rows:
        print('{}'.format(row))
    cur.close()
    db.close()
