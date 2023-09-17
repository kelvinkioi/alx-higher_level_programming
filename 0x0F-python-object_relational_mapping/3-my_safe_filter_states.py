#!/usr/bin/python3
"""
script that takes in arguments and displays all values inthe
states table of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit()
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    except Exception:
        exit()

    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE BINARY \
              states.name = %s""", (sys.argv[4],))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
