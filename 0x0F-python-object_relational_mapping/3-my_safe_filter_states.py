#!/usr/bin/python3

"""
A script that takes in arguments and displays all values where name
matches the argument. The script is safe from MySQL injections!
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    argument = argv[4]

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
    )

    cursor = connection.cursor()
    query = """SELECT * FROM states
            WHERE name LIKE BINARY %s
            ORDER BY states.id"""

    cursor.execute(query, (argument,))
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    connection.close()
