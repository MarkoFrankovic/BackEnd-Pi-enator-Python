import pymongo
import json
from flask import Flask,jsonify
app = Flask(__name__)

myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

mydb = myclient["Pjesme"]

Jaeger = mydb["Pjesme_Jaeger"]
Bambus = mydb["Pjesme_Bambus"]
Voda = mydb["Pjesme_Voda"]
Gin = mydb["Pjesme_Gin"]
Travarica = mydb["Pjesme_Travarica"]
Vodka = mydb["Pjesme_Vodka"]
Jack = mydb["Pjesme_Jack"]
Merlot = mydb["Pjesme_Merlot"]
Stock = mydb["Pjesme_Bambus"]

mydoc1 = Jaeger.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)
mydoc2 = Bambus.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)
mydoc3 = Voda.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)
mydoc4 = Gin.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)
mydoc5 = Travarica.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)
mydoc6 = Vodka.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)
mydoc7 = Jack.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)
mydoc8 = Merlot.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)
mydoc9 = Stock.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)

@app.route('/jaeger')
def jaeger():
   return jsonify(list(mydoc1))

@app.route('/bambus')
def bambus():
   return jsonify(list(mydoc2))

@app.route('/voda')
def voda():
   return jsonify(list(mydoc3))

@app.route('/gin')
def gin():
   return jsonify(list(mydoc4))

@app.route('/travarica')
def travarica():
   return jsonify(list(mydoc5))

@app.route('/vodka')
def vodka():
   return jsonify(list(mydoc6))

@app.route('/jack')
def jack():
   return jsonify(list(mydoc7))

@app.route('/merlot')
def merlot():
   return jsonify(list(mydoc8))

@app.route('/stock')
def stock():
   return jsonify(list(mydoc9))

if __name__ == '__main__':
   app.run()

