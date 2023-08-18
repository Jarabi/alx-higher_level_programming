#!/usr/bin/python3
'''
Lists all states with a name starting with 'N'
'''

from sys import argv
import MySQLdb


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("SELECT *\
        FROM states\
        WHERE name LIKE %s\
        ORDER BY id ASC", ('N%',))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
