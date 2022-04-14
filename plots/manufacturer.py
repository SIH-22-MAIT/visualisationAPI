import pandas as pd
import json
manufacturer_df = pd.read_csv('data/manufacturer.csv')


class Manufacturers():
    def __init__(self):
        self.NameQuantity = self.DrugNameQuantity()
        self.DailyData = self.dailyPlot()
    
    def DrugNameQuantity(self):
        meds = manufacturer_df.pivot_table(index = ['drugName'], aggfunc ='size')
        meds = meds.reset_index()

        x = meds['drugName'].to_list()
        y = meds[0].to_list()

        data = {'x': x, 'y': y}
        return json.dumps(data)
    
    def dailyPlot(self):
        daily = manufacturer_df[manufacturer_df.prescription == True] 
        daily['outTime'] = pd.to_datetime(daily['outTime'],unit='s')
        daily = daily.pivot_table(index = daily.outTime.dt.date, aggfunc ='size')
        daily = daily.to_frame()
        daily = daily.reset_index()

        x = daily['outTime'].to_list()
        x = [date_obj.strftime('%Y-%m-%d') for date_obj in x]
        y = daily[0].to_list()
        daily_data = {'x': x, 'y': y}

        return json.dumps(daily_data)
            