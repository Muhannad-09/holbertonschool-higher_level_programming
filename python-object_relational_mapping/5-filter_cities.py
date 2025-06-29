#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql_user> <mysql_pass> <db_name> <state_name>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user, passwd=password, db=db_name, port=3306)
    cursor = db.cursor()

    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    if rows:
        print(", ".join(city[0] for city in rows))

    cursor.close()
    db.close()
