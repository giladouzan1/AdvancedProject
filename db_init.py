import mysql.connector
import pymysql


connection = pymysql.connect(host='127.0.0.1', user='root', password='pythoncourse', database='my_db')

#create the table
cursor = connection.cursor()
cursor.execute("""CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    creation_date VARCHAR(50)
);
""")
connection.commit()
cursor.close()
connection.close()
