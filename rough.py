import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    password = '1137',
    database = 'fbs'
)

# sql = 'drop database fbs'
# cursor = conn.cursor()
# cursor.execute(sql)
print(conn)

#pip install mysql-connector-python