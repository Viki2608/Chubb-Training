import pymysql

connection = pymysql.Connect(host='127.0.0.1',
                             user='root',
                             password='admin',
                             database='python',
                             charset='utf8mb4')
cursor = connection.cursor()

try:
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print(data)
except Exception as e:
    print(e)
connection.close()