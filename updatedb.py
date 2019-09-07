import mysql.connector as conn

mydb=conn.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="learningDB"
)

mycurser=mydb.cursor()


sql="update Employee set name=%s where name=%s"
new_name=input("Enter new name: ")
old_name=input("Enter to replace name: ")
qattr=(new_name,old_name)
mycurser.execute(sql,qattr)
mydb.commit()
print(mycurser.rowcount,"record updated")

sql="select name,qualification,age,salary from Employee where name=%s"
qattr=(new_name,)
mycurser.execute(sql,qattr)

result=mycurser.fetchall()

for i in result:
    print(i)