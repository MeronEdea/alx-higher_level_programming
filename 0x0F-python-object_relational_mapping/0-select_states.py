#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                        user= MY_USER,
                        passwd=MY_PASS,
                        db=MY_DB)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    table = cur.fetchall()

for row in table
    print(row)

cur.close()
db.close()
