from mysql import connector as conn

mydb=conn.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="inportia_it_solutions"
)

#print(mydb)
query="show databases"
mycursor=mydb.cursor()
mycursor.execute(query)
#print(mycursor)

for x in mycursor:
    print(x)
#
# query2="create database inportia_it_solutions"
##mycursor.execute(query2)
# mycursor.execute(query)
#
# for x in mycursor:
#     print(x)