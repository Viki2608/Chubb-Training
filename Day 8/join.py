import psycopg2
from tabulate import tabulate

con=psycopg2.connect( host = "localhost",database = "joins",user = "postgres",password="admin")

class viki:
    def connection(self):
        if con:
            return True
        else:
            return False
    
    def cross_join(self):
        cur=con.cursor()
        q="select * from Orders cross join Customers"
        cur.execute(q)
        f=cur.fetchall()
        print(tabulate(f,headers=['orderid','customerid','orderdate','customername','contactname','country']))
        print("*"*100)
    def left_join(self):
        cur=con.cursor()
        q="select Orders.OrderID,Orders.CustomerID from Orders left join Customers on Orders.CustomerID=Customers.CustomerID;"
        cur.execute(q)
        f=cur.fetchall()
        print(tabulate(f,headers=['orderid','customerid','orderdate','customername','contactname','country']))
        print("*"*100)

    def right_join(self):
        cur=con.cursor()
        q="select Orders.OrderID,Orders.CustomerID from Orders right join Customers on Orders.CustomerID=Customers.CustomerID;"
        cur.execute(q)
        f=cur.fetchall()
        print(tabulate(f,headers=['orderid','customerid','orderdate','customername','contactname','country']))
        print("*"*100)

    def full_join(self):
        cur=con.cursor()
        q="select Orders.OrderID,Orders.CustomerID from Orders full join Customers on Orders.CustomerID=Customers.CustomerID;"
        cur.execute(q)
        f=cur.fetchall()
        print(f)
        print("*"*100)


    

s=viki()
print(s.connection())



