from pymongo import MongoClient, results


class Suman:
    connection = MongoClient("mongodb://localhost:27017/")

    def mongo_connection(self):
        if self.connection:
            return True
        else:
            return False

    # returns all the databases in form of list
    def mongo_db_list(self):
        if self.mongo_connection() == True:
            return self.connection.list_database_names()

    # returns whether MongoDB Database exists or not
    def db_exists(self, db_name):
        if db_name in self.mongo_db_list():
            return True
        else:
            return False

    # create new collection inside a MongoDB database
    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            db_name = self.connection[db_name]
            new_collection = db_name[new_collection]
            return(new_collection)
        else:
            return("ERROR(404) : MongoDB Connection Failed !")

    # add timestamp
    def timestamp(self):
        import datetime as dt
        return dt.datetime.now()
    def get_data(self, db_name, collection_name,ids,query):
        result=[]
        if self.connection:
            for data in self.connection[db_name][collection_name].find():
                result.append(data)
            for dic in result:
                if dic["_id"]==ids:
                  return dic[query]
        else:
            return("ERROR : DB connection error !")

    # insert data into collections
    def insert_data(self ):
        print("Enter DB Name , Collection Name ,id,Name ,Email ,mobile seperated by space ")
        db_name, collection_name, id, name, email,mobile=map(str,input().split())
        

        if self.connection:
            data = {'_id': id, 'name': name, 'email': email,
                    'mobile': mobile, 'time_stamp': self.timestamp()}
            self.connection[db_name][collection_name].insert_one(data)
            print("SUCCESS : Data Inserted !")
        else:
            print("ERROR : Unable to insert data")
    # display data
    def display_data(self,):
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

    
    
    def delete_data(self):

        print("Enter DB name")
        db_name=input()
        print("Enter collection name")
        collection_name=input()
        print("Enter id")
        ids=int(input())
        myquery = { "_id": ids }
        self.connection[db_name][collection_name].delete_one(myquery)
        print("sucessfully deleted")
    
    def update_data(self,):
        print('Enter db name and collection name seperated by space')
        db_name, collection_name=map(str,input().split())
        print("enter id")
        ids=int(input())
        print("Enter current value")
        myquery = input()
        print("Enter update value")
        newvalues = input()
        newval={ "$set":  newvalues  }

        
        
        self.connection[db_name][collection_name].update_one(myquery,newval)
        
            
        
        

    

    
    def instructions(self):
        instrc="""
        1.Insert data 
        2.View all data
        3.update data by id
        4.delete data by id
        Press 1-4 or 0 to Exit:"""
        print(instrc)
        i=int(input())
        
        
        
        if(i==1):
            self.insert_data()
            self.instructions()
            
        elif(i==2):
            self.display_data()
            self.instructions()
        elif(i==3):
            self.update_data()
            self.instructions()
        elif(i==4):
            self.delete_data()
            self.instructions()
        elif(i==0):
            print("Goodbye") 
            
        
        
        
                

s = Suman()






#print(s.create_new_collection("viki","Detail"))
#print(s.timestamp())
#print(s.insert_data('viki', 'Detail', 2, 'tanushree','tanushree@example.com', '98942212345'))

#print(s.display_data('viki','Detail'))
s.instructions()
