import sqlite3 
connection = sqlite3.connect("sql.db") 
cursor = connection.cursor() 
cursor.executescript(""" 
	CREATE TABLE department( deptId INTEGER, 
	deptName VARCHAR(20), deptScore INTEGER); 
	INSERT INTO department VALUES ( 01,'IT', 850 ); 
	INSERT INTO department VALUES ( 02,'COMP', 840 ); 
	INSERT INTO department VALUES ( 03,'CIVIL', 500 ); 
	INSERT INTO department VALUES ( 04,'E&TC', 650 ); 
""") 
print("Table data :") 
cursor.execute("SELECT * FROM department") 
print(cursor.fetchall()) 
cursor.executescript(""" 
	UPDATE department set deptScore = 900 where deptId = 01; 
	UPDATE department set deptScore = 890 where deptId = 02; 
	UPDATE department set deptScore = 660 where deptId = 03; 
	UPDATE department set deptScore = 790 where deptId = 04; 
""")  
print("Table data after updation :") 
cursor.execute("SELECT * FROM department") 
print(cursor.fetchall()) 
connection.commit() 
connection.close()
