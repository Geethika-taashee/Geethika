import sqlite3
conn=sqlite3.connect("sql.db")
cursor=conn.cursor()
employe_details=[('Buchibabu','java','Technical Manager'),
                 ('Shyam','python','Technical Manager')
                ]
for employe in employe_details:
    emp_name,emp_technology,emp_department=employe
    cursor.execute("INSERT INTO emp(emp_name,emp_technology,emp_department)VALUES(?, ?, ?)",(emp_name,emp_technology,emp_department))
conn.commit()
print("Employee details inserted successfully")
conn.close()