import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Ahmed9112",
  database="hospital"
)

mycursor = mydb.cursor()

sql = "UPDATE DOCTOR SET id = %s WHERE id = %s"
val = (5, 1)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 