#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
    query = """SELECT name
            FROM cities
            WHERE cities.state_id = (
                SELECT id
                FROM states
                WHERE states.name = %s
            )
            ORDER BY cities.id"""

    cursor.execute(query, (argument,))
    query_rows = cursor.fetchall()

    for index, row in enumerate(query_rows):
        if index:
            print(", ", end="")
        print(row[0], end="")
    print()

    cursor.close()
    connection.close()
