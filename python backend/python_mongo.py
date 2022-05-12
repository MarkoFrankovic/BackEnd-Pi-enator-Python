import pymongo
import json
from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app,resources = {r"/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

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
Stock = mydb["Pjesme_Stock"]


@app.route('/jaeger')
def jaeger():
   return jsonify(list(Jaeger.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

@app.route('/bambus')
def bambus():
   return jsonify(list(Bambus.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

@app.route('/voda')
def voda():
   return jsonify(list(Voda.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

@app.route('/gin')
def gin():
   return jsonify(list(Gin.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

@app.route('/travarica')
def travarica():
   return jsonify(list(Travarica.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

@app.route('/vodka')
def vodka():
   return jsonify(list(Vodka.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

@app.route('/jack')
def jack():
   return jsonify(list(Jack.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

@app.route('/merlot')
def merlot():
   return jsonify(list(Merlot.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

@app.route('/stock')
def stock():
   return jsonify(list(Stock.find({},{ "_id": 0, "ime": 0, "ocjena": 0 }).sort("ocjena",-1)))

if __name__ == '__main__':
   app.run()

