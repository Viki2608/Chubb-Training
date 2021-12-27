import requests
import json
from pymongo import MongoClient


class Connect:
    connection = MongoClient("mongodb://localhost:27017/")

    def mongo_connection(self):
        if self.connection:
            return True
        else:
            return False

    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            db_name = self.connection[db_name]
            new_collection = db_name[new_collection]
            return(new_collection)
        else:
            return("MongoDB Connection Failed !")

    def insert_data(self,db_name,collection_name):
        if self.connection:
            mydb = self.connection[db_name]
            mycol = mydb[collection_name]  
            response_API = requests.get("https://fruityvice.com/api/fruit/all")
            data = response_API.json()
            self.connection[db_name][collection_name].insert_many(data)
            
            return("insert sucess")
        else:
            return("ERROR : Unable to insert data")

    def display_data(self):
        print("enter db name and collection name")
        db_name, collection_name=map(str,input().split())
        result=[]
        if self.connection:
            for data in self.connection[db_name][collection_name].find():
                result.append(data)
            for dic in result:
                for key,value in dic.items():
                    print(value)
        else:
            print("ERROR : DB connection error !")

s=Connect()
#print(s.insert_data("fruits","fruit"))
print(s.display_data())







