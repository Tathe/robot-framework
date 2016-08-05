import mysql.connector
from mysql.connector import errorcode
cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='employee')
cr= cnx.cursor()

try:
   sql="""create table empl(
   empid INT NOT NULL,
   empname varchar(100),
   adress varchar(200))"""
   cr.execute(sql)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("already exists.")
    else:
        print(err.msg)
else:
    print("OK")
'''query = ("INSERT INTO temp"
        "(name, adress) "
        "VALUES (%s, %s)")
arg= ('xyz','7070707070')'''


'''query="""insert into temp values(
'zsss','1234567890')"""
cr.execute(query)'''

print('last insert id', cr.lastrowid)

cr.execute("select * from temp where name='abc'")
data=cr.fetchone()

for row in data:
    print row

cnx.commit()
cr.close()
cnx.close()
