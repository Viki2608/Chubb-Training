import pandas as pd

class Viki:
    def read(self,file):
       df = pd.read_csv('data.csv')
       return df
     
    def sum_jan2021(self,file):
        df = pd.read_csv('data.csv')
        Total = df['jan_2021'].sum()
        return Total
    def sum_feb2021(self,file):
        df = pd.read_csv('data.csv')
        Total = df['feb_2021'].sum()
        return Total
    def sum_mar2021(self,file):
        df = pd.read_csv('data.csv')
        Total = df['mar_2021'].sum()
        return Total
    def sum(self,file):  
        file=pd.read_csv(file)
        for i in range(0,len(file)):
            s=file['jan_2021']+file['feb_2021']+file['mar_2021']
            return s
    def per(self,file):
        df=pd.read_csv(file)
        for i in range(0,len(file)):
            s=file['jan_2021']+file['feb_2021']+file['mar_2021']
        
        return s.pct_change(axis=1,fill_method='bfill')


       

file='data.csv'
a=Viki()
#print(a.read(file))
#print(a.sum_jan2021(file))
#print(a.sum_feb2021(file))
print(a.sum_mar2021(file))
print(a.sum(file))