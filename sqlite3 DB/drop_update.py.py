# import sqlite3 
# connection = sqlite3.connect('sql.db') 
# connection.execute(''' CREATE TABLE STUDENTS 
# 		(SID INT PRIMARY KEY	 NOT NULL, 
# 		SNAME		 TEXT NOT NULL, 
# 		SAGE		 INT	 NOT NULL, 
# 		ADDRESS	 CHAR(50)); 
# 		''') 
# connection.execute( 
# 	"INSERT INTO STUDENTS VALUES (1, 'mohan pavan', 22, 'ponnur' )") 
# connection.execute( 
# 	"INSERT INTO STUDENTS VALUES (2, 'sudheer', 28, 'chebrolu' )") 
# connection.execute( 
# "INSERT INTO STUDENTS VALUES (3, 'mohan', 22, 'tenali' )") 
# cursor = connection.execute("SELECT * from STUDENTS") 
# print('\nOriginal Table:') 
# for row in cursor: 
# 	print(row) 
# connection.execute("UPDATE STUDENTS set SNAME = 'sravan' where SID = 1")  
# connection.commit()  
# cursor = connection.execute("SELECT * from STUDENTS") 
# print('\nUpdated Table:') 
# for row in cursor: 
# 	print(row) 


import sqlite3
conne=sqlite3.connect('sql.db')
cursor=conne.cursor()
conne.execute("DROP TABLE student")
print("data dropped successfully")
conne.close()