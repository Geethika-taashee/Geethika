import sqlite3
conn=sqlite3.connect("sql.db")
cursor=conn.cursor()

# print("Data in the table:")
# cursor.execute("SELECT * FROM emp WHERE emp_name='Buchibabu'")

print("Data in the table:")
cursor.execute("SELECT * FROM emp WHERE emp_department='Technical Manager'")

# print("Data in the table:")
# cursor.execute("SELECT * FROM emp WHERE emp_technology='python'")

data=cursor.fetchall()
for row in data:
    print(row)
conn.close()