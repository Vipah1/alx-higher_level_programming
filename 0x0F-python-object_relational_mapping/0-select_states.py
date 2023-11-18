#!/usr/bin/python3
""" Thiis is a script to list all states from a database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    user_name, password, database = argv[1], argv[2], argv[3]

    # establishing connection to database using MySQLdb module

    db = MySQLdb.connect(
        host="localhost",
        user=user_name,
        passwd=password,
        db=database,
        port=3306
    )
    # create a working env using cursor object
    # to perform operations
    cursor_object = db.cursor()

    cursor_object.execute("SELECT * from states ORDER id ASC")
    rows = cursor_object.fetchall()
    for row in rows:
        print("{}".format(row))

    cursor_object.close()
    db.close()
