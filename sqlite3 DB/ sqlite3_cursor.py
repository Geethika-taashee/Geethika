import sqlite3
connection=sqlite3.connect("sql.db")
cursor=connection.cursor()
print('DB Init')
query='select sqlite_version();'
cursor.execute(query)
result=cursor.fetchall()
print('SQLlite version is {}'.format(result))
print('SQLite Connection closed')