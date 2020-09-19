import mysql.connector

mydb = mysql.connector.connect(
  host="0.0.0.0",
  port="6604",
  user="root",
  password="pass2",
  database="db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tab")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)