#!/usr/bin/python3
"""
This script lists all states from the 'hbtn_0e_0_usa' database.
Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish a connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results from the executed query
    states = cursor.fetchall()

    # Iterate over the results and print each state
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
