#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id")
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()
