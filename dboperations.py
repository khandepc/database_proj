import mysql.connector as conn

mydb=conn.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="learningDB"
)
#print(mydb)
mycursor=mydb.cursor()

#create table
# sql="""create table Employee
#         (
#             name char(30) not null,
#             qualification char(40),
#             age int null,
#             salary float null
#
#         )
#         """
# mycursor.execute(sql)

#insert
sql="""insert into Employee 
            (name,qualification,age,salary)
            values
            ('Rashmi','BAMS',23,35000)"""

sql="""insert into Employee 
            (name,qualification,age,salary)
            values
            (%s,%s,%s,%s)"""
name=input("Enter name: ")
qualification=input("Enter qualification: ")
age=input("Enter age: ")
salary=input("Enter salary: ")
qattr=(name,qualification,age,salary)
mycursor.execute(sql,qattr)
mydb.commit()
count=mycursor.rowcount
if count>0:
    print("record inserted successfully")
else:
    print("no record inserted")