import pandas as pd
import json
import numpy as np
doctor_df = pd.read_csv('data/doctor.csv')


class Doctors():
    def __init__(self):
        self.NameQuantity = self.DrugNameQuantity()
    
    def DrugNameQuantity(self):
        meds = doctor_df.pivot_table(index = ['drugName'],aggfunc=np.sum)
        meds = meds.reset_index()

        x = meds['drugName'].to_list()
        y = meds['quantity'].to_list()

        data = {'x': x, 'y': y}
        return json.dumps(data)
            