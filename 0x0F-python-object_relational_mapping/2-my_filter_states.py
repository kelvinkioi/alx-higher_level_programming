#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit()
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    s = 'SELECT * FROM states WHERE name LIKE "{}"'.format(sys.argv[4])
    c.execute(s)
    rows = c.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    db.close()
