import mysql.connector

mydb = mysql.connector.connect(
  host="0.0.0.0",
  port="6603",
  user="root",
  password="pass1",
  database="db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tab2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)