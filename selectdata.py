import mysql.connector as conn

mybd=conn.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="learningDB"
)
mycursor=mybd.cursor(dictionary=True)



sql="select name,qualification,age,salary from Employee"
#sql="select name,qualification,age,salary from Employee where name like'%ra%'"
# sql="select name,qualification,age,salary from Employee where qualification=%s"
# q=input("Enter your Qualification to search: ")
# qattr=(q,)
# mycursor.execute(sql,qattr)
mycursor.execute(sql)
result=mycursor.fetchall()
# print(result[0])
for i in result:
    print(i)