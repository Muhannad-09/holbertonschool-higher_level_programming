#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a connection to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query with a LIMIT clause to fetch the first 5 states
    cursor.execute("SELECT * FROM states ORDER BY id LIMIT 5")

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print each row in the desired format
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
