import mysql.connector


conn = mysql.connector.connect (
    user="root",
    password="pratyushch@20",
    host="localhost",
    port=3306,
    database="giet_db"
)

print("connected")

if conn.is_connected():
    print("Connection successful")

cur = conn.cursor()
cur.execute("SELECT * FROM giet")

for db in cur:
    print(db)


cur.close()
conn.close()    