from mysql import connector as conn

mydb=conn.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="inportia_it_solutions"
)

#print(mydb)
mycursor=mydb.cursor()

# query="""create table students (id int auto_increment primary key,name verchar(30),age int, course varchar(30))"""
# mycursor.execute(query)


query2="show database"
mycursor.execute(query2)
for x in mycursor:
    print(x)