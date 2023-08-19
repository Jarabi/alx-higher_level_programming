#!/usr/bin/python3
"""
This script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
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

    cur = connection.cursor()
    query = """SELECT * FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC;
            """
    format_query = query.format(argument)
    cur.execute(format_query)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    connection.close()
