from typing import Counter
from tabulate import tabulate
import psycopg2
class Postgres:
    con=psycopg2.connect(
            host = "localhost",
            database = "guvi",
            user = "postgres",
            password="admin"
        )
    def Connection(self):
        
        if self.con:
            return True
        else:
            return False
        
    def create_table(self):
        cur=self.con.cursor()
        if self.Connection:
            name=input("Enter table name : ")
            sql=f'''CREATE TABLE {name} (id INT PRIMARY KEY,food_name TEXT,location TEXT)'''
            cur=self.con.cursor()
            cur.execute(sql)
            self.con.commit()
            self.con.close()
            print(f"table {name} created with id,food_name,location columns")
        else:
            print("not created")
    
    def delete_table(self):
        cur=self.con.cursor()
        if self.Connection:
            name=input("Enter table name to be deleted :")
            sql=f'''DROP TABLE {name}'''
            cur.execute(sql)
            self.con.commit()
            self.con.close()
            print(f"Table {name} is deleted")
        else:
            print("Table cannot be deleted")


    def insert_data(self):
        cur=self.con.cursor() 
        table=input("Enter table name:")
        id=int(input("enter id of item:"))
        food_name=input("Enter food name:")
        location=input("Enter Origin of food:")
        sql_1=f"INSERT INTO {table}(id, food_name, location)VALUES(%s,%s,%s)"
        cur.execute(sql_1,(id,food_name,location)) 
        print(f"data inserted successfully! into {table}")
        self.con.commit()
        self.con.close()
    
    def update_data(self):
        cur=self.con.cursor()
        id=int(input("enter id of item:"))
        food_name=input("Enter food name to be updated:")
        location=input("Enter Origin of food to be updated:")
        sql="update food_for_life set food_name=%s,location=%s where id=%s" 
        cur.execute(sql,(food_name,location,id))
        self.con.commit()
        print("Sucessfully updated")

    def delete_by_id(self):
        
        cur=self.con.cursor() 
        id=int(input())
        sql_1=f"DELETE FROM food_for_life WHERE id={id};"
        cur.execute(sql_1) 
        self.con.commit()
        print("data deleted successfully!")

    def view_data(self): 
        cur=self.con.cursor() 
        i=input("Enter 'all' to display all data or 'id' to certain row")
        if i=='all':
            qu="select * from hello;"
            cur.execute(qu)
            fetch=cur.fetchall()
            print(tabulate(fetch,headers=['id','food_name','location']))
        else:
            q="select * from food_for_life where id=%s"
            cur.execute(q,[i])
            fetch=cur.fetchall()
            print(fetch)
            print(tabulate(fetch,headers=['id','food_name','location']))

s=Postgres()
if s.Connection:

    while True:
        print("--------------------Choices:-----------------")
        print("1.Create table")
        print("2.Insert data")
        print("3.Update data By Id")
        print("4.Delete data By Id")
        print("5.Display data")
        print("6.Delete Table")
        print("7.Exit")

        choice = int(input("Enter your choice:"))

        if choice==1:
            
            s.create_table()
            print("*"*100)
        
        elif choice==2:
            s.insert_data()
            
            print("*"*100)

        elif choice==3:
            
            s.update_data()
            print("*"*100)

        elif choice==4:
            s.delete_by_id()
            print("*"*100)
        
        elif choice==5:
            s.view_data()
            
            print("*"*100)
            
        elif choice==7:

            print("\t\t\t\t\t\tThank You!")
            break
        elif choice==6:
            s.delete_table()
            print("*"*100)

        else:
            print("Invalid Input!")

else:
    print("Connection Error try again!")

    

