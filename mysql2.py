from mysql import connector as conn

mydb=conn.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="inportia_it_solutions"
)

#print(mydb)
mycursor=mydb.cursor()

query="""create table students2 (id int auto_increment primary key,name varchar(30),age int, course varchar(30))"""
#mycursor.execute(query)

queiry2='create table students '\
    '(id int auto_increment primary key,name varchar(30))'

#mycursor.execute(queiry2)


quiery3="show tables"
mycursor.execute(quiery3)