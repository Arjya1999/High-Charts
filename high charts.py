
import json
import pandas as pd

class Basic:
    
    def return_json(self,df,columns):
        
        '''
        This function takes in dataframe and column list then returns back data in json frame
        '''
        
        data={}
        for i in columns:
            d={}
            d.update({i:df[i]})
            data.update(d)
            
        return data

myClass=Basic()
dataset = pd.read_csv("homes.csv")

columns=["Sell","List"]
columns_data = myClass.return_json(dataset,columns)