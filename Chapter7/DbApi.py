import mysql.connector

dbconfig = {
    "host": "127.0.0.1",
    "user": "websearch",
    "password": "search",
    "database": "vsearchlogdb"
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_sqlShowTables = """show tables"""
cursor.execute(_sqlShowTables)
print(cursor.fetchall())

print("======================")

_sqlDescribe = """describe logs"""
cursor.execute(_sqlDescribe)
result = cursor.fetchall()

for row in result:
    print(row)

print("======================")

_sqlInsert = """insert into logs
(phrase, letters, ip, user_agent, results)
values
(%s, %s, %s, %s, %s)"""

cursor.execute(_sqlInsert, ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}"))

conn.commit()  # force write all inserts into DB

_sqlSelect = """select * from logs"""
cursor.execute(_sqlSelect)
for row in cursor.fetchall():
    print(row)

print("======================")

cursor.close()
conn.close()
