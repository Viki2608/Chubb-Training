
import pandas as pd
from pandas.core.frame import DataFrame


class Viki:
    def read(self,file):
       df = pd.read_csv('governors_county_candidate.csv')
       return df
    def party_won(self,file):
        df = pd.read_csv('governors_county_candidate.csv')
        new_df = df[df['won']==True]
        new_df[['state','party']]
    def total_votes_by_each_parties_statewise(self,file):
        df=pd.read_csv('governors_county_candidate.csv')
        print("***************************************")
        return df.groupby(by=["state",'party'])["votes"].sum()
    def total_votes_statewise(self,file):
        df=pd.read_csv('governors_county_candidate.csv')
        print("***************************************")
        return df.groupby(by=["state"])["votes"].sum()
        
    
        
                

file='governors_county_candidate.csv'
a=Viki()
#print(a.party_won(file))
print(a.total_votes_by_each_parties_statewise(file))
print(a.total_votes_statewise(file))
