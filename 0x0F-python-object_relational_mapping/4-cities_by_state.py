#!/usr/bin/python3

"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
    )

    cursor = connection.cursor()
    query = """SELECT c.id, c.name, s.name
            FROM cities c, states s
            WHERE c.state_id = s.id
            ORDER BY c.id ASC"""

    cursor.execute(query)
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    connection.close()
