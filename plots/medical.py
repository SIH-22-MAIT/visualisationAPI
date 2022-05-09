import pandas as pd
import json
import numpy as np
medical_df = pd.read_csv('data/medicalStoreIncoming.csv')
medical_df_out = pd.read_csv('data/medicalStoreOutgoing.csv')

class medicalStore():
    def __init__(self):
        self.DailyData = self.dailyPlot()
        self.MedicalQuantity = self.MedicalVsQuantity()
    
    def dailyPlot(self):
        daily = medical_df
        daily['exhaustTime'] = pd.to_datetime(daily['exhaustTime'],unit='s')
        daily = daily.pivot_table(index = daily.exhaustTime.dt.date, aggfunc =np.sum)
        #daily = daily.to_frame()
        daily = daily.reset_index()

        x = daily['exhaustTime'].to_list()
        x = [date_obj.strftime('%Y-%m-%d') for date_obj in x]
        y = daily['quantity'].to_list()
        daily_data = {'x': x, 'y': y}

        return json.dumps(daily_data)

    def MedicalVsQuantity(self):
        medical_byID = pd.pivot_table(medical_df, values='quantity', index=['medicalStoreID'], aggfunc=np.sum)
        medical_byID = medical_byID.reset_index()
        y = medical_byID['quantity'].to_list()
        x = medical_byID['medicalStoreID'].to_list()
        data = {'x': x, 'y': y}
        return json.dumps(data)
            