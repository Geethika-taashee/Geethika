import sqlite3
conn=sqlite3.connect("sql.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE emp(emp_name Text Not null,emp_technology Text Not null,emp_department Text Not null)")
conn.commit()
print("table created")
conn.close()