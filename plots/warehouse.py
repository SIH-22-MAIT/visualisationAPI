import pandas as pd
import numpy as np
import json
warehouse_df = pd.read_csv('data/warehouseForm.csv')


class Warehouses():
    def __init__(self):
        self.DailyData = self.dailyPlot()
        self.DailyInData = self.dailyINplots()
        self.warehouseVsID = self.WarehouseVsQuantity()
    
    def WarehouseVsQuantity(self):
        warehouse_byID = pd.pivot_table(warehouse_df, values='quantity', index=['warehouseID'], aggfunc=np.sum)
        warehouse_byID = warehouse_byID.reset_index()
        y = warehouse_byID['quantity'].to_list()
        x = warehouse_byID['warehouseID'].to_list()
        data = {'x': x, 'y': y}
        return json.dumps(data)
    
    def dailyPlot(self):
        daily = warehouse_df
        daily['outTime'] = pd.to_datetime(daily['outTime'],unit='s')
        daily = daily.pivot_table(index = daily.outTime.dt.date, aggfunc = np.sum)
        #daily = daily.to_frame()
        daily = daily.reset_index()

        x = daily['outTime'].to_list()
        x = [date_obj.strftime('%Y-%m-%d') for date_obj in x]
        y = daily['quantity'].to_list()
        daily_data = {'x': x, 'y': y}

        return json.dumps(daily_data)

    def dailyINplots(self):
        daily = warehouse_df
        daily['inTime'] = pd.to_datetime(daily['inTime'],unit='s')
        daily = daily.pivot_table(index = daily.inTime.dt.date, aggfunc = np.sum)
        #daily = daily.to_frame()
        daily = daily.reset_index()

        x = daily['inTime'].to_list()
        x = [date_obj.strftime('%Y-%m-%d') for date_obj in x]
        y = daily['quantity'].to_list()
        daily_data = {'x': x, 'y': y}

        return json.dumps(daily_data)
            