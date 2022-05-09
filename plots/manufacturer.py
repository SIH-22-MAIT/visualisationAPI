import pandas as pd
import json
import numpy as np

manufacturer_df = pd.read_csv('data/manufacturerForm.csv')


class Manufacturers():
    def __init__(self):
        self.NameQuantity = self.DrugNameQuantity()
        self.DailyData = self.dailyPlot()
        self.ManufacturerVsQuantity = self.ManufacturerVsQuantity()

    def ManufacturerVsQuantity(self):
        manufacturer_byID = pd.pivot_table(manufacturer_df, values='quantity', index=['manufacturerID'], aggfunc=np.sum)
        manufacturer_byID = manufacturer_byID.reset_index()
        y = manufacturer_byID['quantity'].to_list()
        x = manufacturer_byID['manufacturerID'].to_list()
        data = {'x': x, 'y': y}
        return json.dumps(data)
    
    def DrugNameQuantity(self):
        meds = manufacturer_df.pivot_table(index = ['drugName'],aggfunc=np.sum)
        meds = meds.reset_index()

        x = meds['drugName'].to_list()
        y = meds['quantity'].to_list()

        data = {'x': x, 'y': y}
        return json.dumps(data)
    
    def dailyPlot(self):
        daily = manufacturer_df
        daily['outTime'] = pd.to_datetime(daily['outTime'],unit='s')
        daily = daily.pivot_table(index = daily.outTime.dt.date, aggfunc =np.sum)
        #daily = daily.to_frame()
        daily = daily.reset_index()

        x = daily['outTime'].to_list()
        x = [date_obj.strftime('%Y-%m-%d') for date_obj in x]
        y = daily['quantity'].to_list()
        daily_data = {'x': x, 'y': y}

        return json.dumps(daily_data)
            