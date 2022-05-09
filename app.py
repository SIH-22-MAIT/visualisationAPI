from tkinter import W
from flask import Flask, render_template, request
from plots import doctor, manufacturer, medical, warehouse

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/manufacturer/IdQuantity')
def IDQuantity():
    manufacturer_obj = manufacturer.Manufacturers()
    return manufacturer_obj.ManufacturerVsQuantity

@app.route('/manufacturer/NameQuantity')
def nameQuantity():
    manufacturer_obj = manufacturer.Manufacturers()
    return manufacturer_obj.NameQuantity

@app.route('/manufacturer/DailyData')
def dailyData():
    manufacturer_obj = manufacturer.Manufacturers()
    return manufacturer_obj.DailyData

@app.route('/warehouse/IdQuantity')
def WarehouseIDQuantity():
    warehouse_obj = warehouse.Warehouses()
    return warehouse_obj.warehouseVsID

@app.route('/warehouse/DailyData')
def warehouseDailyData():
    warehouse_obj = warehouse.Warehouses()
    return warehouse_obj.DailyData

@app.route('/medicalStore/DailyData')
def medicalStoreDailyData():
    medical_obj = medical.medicalStore()
    return medical_obj.DailyData

@app.route('/doctor/NameQuantity')
def doctorNameQuantity():
    doctor_obj = doctor.Doctors()
    return doctor_obj.NameQuantity

if __name__ == "__main__":
    app.run(debug=True)