from flask import Flask, render_template, request
from plots import manufacturer

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/manufacturer/NameQuantity')
def nameQuantity():
    manufacturer_obj = manufacturer.Manufacturers()
    return manufacturer_obj.NameQuantity

@app.route('/manufacturer/DailyData')
def dailyData():
    manufacturer_obj = manufacturer.Manufacturers()
    return manufacturer_obj.DailyData


if __name__ == "__main__":
    app.run(debug=True)