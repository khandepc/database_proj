import mysql.connector as conn

mydb=conn.connect(
    host="localhost",
    user="root",
    passwd="root"
)
print(mydb)

mycursor=mydb.cursor()
# sql="create database learningDB"
# mycursor.execute(sql)
sql="show databases"
mycursor.execute(sql)
for i in mycursor:
    print(i)
