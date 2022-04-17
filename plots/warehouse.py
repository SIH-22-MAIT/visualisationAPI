import pandas as pd
import json
warehouse_df = pd.read_csv('data/warehouseForm.csv')


class Warehouses():
    def __init__(self):
        self.DailyData = self.dailyPlot()
    
    def dailyPlot(self):
        daily = warehouse_df
        daily['outTime'] = pd.to_datetime(daily['outTime'],unit='s')
        daily = daily.pivot_table(index = daily.outTime.dt.date, aggfunc ='size')
        daily = daily.to_frame()
        daily = daily.reset_index()

        x = daily['outTime'].to_list()
        x = [date_obj.strftime('%Y-%m-%d') for date_obj in x]
        y = daily[0].to_list()
        daily_data = {'x': x, 'y': y}

        return json.dumps(daily_data)
            