import pymongo
from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import bson.json_util as json_util
import os
app = Flask(__name__)
cors = CORS(app,resources = {r"/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

#spajanje na bazu
#myclient = pymongo.MongoClient("mongodb", 27017, maxPoolSize=50)
myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

#izbor databaze
mydb = myclient["Playlista"]
mydb2 = myclient["Komentari_za_ocjenu"]

#izbor kolekcija
Pjesme = mydb["Pjesme"]
Komentari = mydb2["Komentari"]

#READ CRUD - Getanje pića
@app.route('/getanje', methods=['GET'])
def dohvacanje():
   return jsonify(list(Pjesme.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1,"pice":1}).sort("ocjena",-1)))

#CREATE CRUD - Upis pjesama u databazu
@app.route('/upis', methods=['PUT'])
def upis_u_bazu():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   data["ocjena"] = int(data["ocjena"])
   Pjesme.insert_one(data)
   return data

#UPDATE CRUD - Izmjena ocjene
@app.route('/izmjena', methods=['PATCH'])
def izmjena_ocjene():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Pjesme.update_many(myquery, newvalues)
   return data

#DELETE CRUD - Brisanje pjesama iz databaze
@app.route('/delete', methods=['DELETE'])
def brisanje_pjesme():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "ime":  data["ime"]}
   Pjesme.delete_many(myquery)
   return data

#Upis komentara u databazu
@app.route('/upis_komentara', methods=['POST'])
def dodavanje_komentara_u_bazu():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   Komentari.insert_one(data)
   return data

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
   
