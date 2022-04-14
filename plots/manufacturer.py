import pandas as pd
import json
manufacturer_df = pd.read_csv('data/manufacturer.csv')


class Manufacturers():
    def __init__(self):
        self.NameQuantity = self.DrugNameQuantity();
    
    def DrugNameQuantity(self):
        meds = manufacturer_df.pivot_table(index = ['drugName'], aggfunc ='size')
        meds = meds.reset_index()

        x = meds['drugName']
        y = meds[0]

        data = {'x': x, 'y': y}
        return json.dumps(data)
    