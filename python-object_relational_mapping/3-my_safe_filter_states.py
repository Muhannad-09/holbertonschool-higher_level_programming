#!/usr/bin/python3
"""
Displays all states that match the provided name (safe from SQL injection).
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
