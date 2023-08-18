#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
