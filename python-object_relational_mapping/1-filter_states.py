#!/usr/bin/python3
"""
Lists all states starting with uppercase 'N' from the database.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
