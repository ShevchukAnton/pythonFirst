import mysql.connector

dbconfig = {
    "host": "127.0.0.1",
    "user": "websearch",
    "password": "search",
    "database": "vsearchlogdb"
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_sql = """show tables"""
cursor.execute(_sql)
print(cursor.fetchall())
