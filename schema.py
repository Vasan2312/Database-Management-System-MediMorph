import mysql.connector
from mysql.connector import Error
from mysql.connector import connect

config = {
    'user': 'root',
    'password': 'Utkarsh@28505',
    'host': 'localhost',
    'database': 'mydb',
    'auth_plugin': 'mysql_native_password'
}
try:
    connection = connect(**config)
    print("Connection established")
except Error as e:
    print("An error occured in establishing connection :()", e) 
c = connection.cursor()
    

with open('schema.sql', 'r') as f:
    script = f.read()
for result in c.execute(script, multi=True):
    if result.with_rows:
        result.fetchall()
connection.commit()
with open('data.sql', 'r') as f:
    script = f.read()
for result in c.execute(script, multi=True):
    if result.with_rows:
        result.fetchall()
connection.commit()

query = "delete from lab_cart"
c.execute(query)

query = "delete from medicine_id"
c.execute(query)

query = "delete from doctor_cart"
c.execute(query)

connection.commit();
c.execute("drop table if exists order_summary")
query = "create table if not exists order_summary (customer_id int, medicine_price double, doctor_price double, lab_price double)"
c.execute(query)
connection.commit()


c.close()
