#!/usr/bin/python3
""" script to list all states with letter 'N' from database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user_name, password, database = argv[1], argv[2], argv[3]

    # establish connection to database
    db = MySqldb.connect(
        host="localhost",
        user=user_name,
        passwd=password,
        db=database,
        port=3306
    )

    # create working environment with cursor object for operations
    cursor_object = db.cursor()

    query = """
    SELECT * FROM states
    WHERE BINARY name LIKE 'N%'
    ORDER BY states.id ASC
    """

    cursor_object.execute(query)
    rows = cursor_object.fetchall()
    for row in rows:
        print("{}".format(row))

    cursor_object.close()
    db.close()
