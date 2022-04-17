import pandas as pd
import json
medical_df = pd.read_csv('data/medicalStoreIncoming.csv')


class medicalStore():
    def __init__(self):
        self.DailyData = self.dailyPlot()
    
    def dailyPlot(self):
        daily = medical_df
        daily['exhaustTime'] = pd.to_datetime(daily['exhaustTime'],unit='s')
        daily = daily.pivot_table(index = daily.exhaustTime.dt.date, aggfunc ='size')
        daily = daily.to_frame()
        daily = daily.reset_index()

        x = daily['exhaustTime'].to_list()
        x = [date_obj.strftime('%Y-%m-%d') for date_obj in x]
        y = daily[0].to_list()
        daily_data = {'x': x, 'y': y}

        return json.dumps(daily_data)
            