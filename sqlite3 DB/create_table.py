import sqlite3
conn=sqlite3.connect("sql.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE student1(id INTEGER,NAME Text,Section Text)")
conn.commit()
print("table created")
conn.close()
