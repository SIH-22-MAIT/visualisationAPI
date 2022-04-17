import pandas as pd
import json
doctor_df = pd.read_csv('data/doctor.csv')


class Doctors():
    def __init__(self):
        self.NameQuantity = self.DrugNameQuantity()
    
    def DrugNameQuantity(self):
        meds = doctor_df.pivot_table(index = ['drugName'], aggfunc ='size')
        meds = meds.reset_index()

        x = meds['drugName'].to_list()
        y = meds[0].to_list()

        data = {'x': x, 'y': y}
        return json.dumps(data)
            