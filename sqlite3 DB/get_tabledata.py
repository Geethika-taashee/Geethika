import sqlite3
conn=sqlite3.connect("sql.db")
cursor=conn.cursor()


print("Data in the table:")
# cursor.execute("SELECT * FROM student1 WHERE ID=101")

# print("Data in the table:")
# cursor.execute("SELECT * FROM student1 WHERE NAME='Ajay'")

# cursor.execute("SELECT Section from student1 ORDER BY  id DESC")

# cursor.execute("SELECT NAME from student1 ORDER BY  id ASC")

# cursor.execute("SELECT * FROM student1 LIMIT 2")

# cursor.execute("DELETE FROM student1 WHERE id=104")

cursor.execute("UPDATE student1 SET NAME='joo' WHERE id=101")


data=cursor.fetchall()
for row in data:
    print(row)
conn.close()
