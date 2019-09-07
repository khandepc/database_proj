import mysql.connector as conn

mydb=conn.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="learningDB"
)

mycurser=mydb.cursor()

sql="delete from Employee where name=%s "
q=input("Enter a name to delete: ")
qattr=(q,)
mycurser.execute(sql,qattr)
mydb.commit()
if mycurser.rowcount>0:
    print("record is deleted")
else:
    print("no record found to delete")