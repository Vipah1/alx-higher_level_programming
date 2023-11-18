#!/usr/bin/python3
""" Script takes argument and displays value """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: ./2-my_filter_states.py root"
              "root hbtn_0e_0_usa 'state_name'")
        exit(1)

        user_name, password, database, match = argv[1], argv[2], argv[3], argv[4]
        # establish a connection to database
        db =MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=password,
            db=database,
            port=3306
        )

        # create a working environment using cursor object

        cursor_object = db.cursor()


        query = """
        SELECT * from states
        WHERE name = '{}'
        ORDER BY states.id ASC
        """.format(match)

        cursor_object.execute(query)
        rows = cursor_object.fetchall()
        for row in rows:
            print("{}".format(row))

        cursor_object.close()
        db.close()
        
