import pymongo
from flask import Flask,request
from flask_cors import CORS, cross_origin
import bson.json_util as json_util
import os
from bson.objectid import ObjectId
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
@app.route('/api/pjesme/<pice>', methods=['GET'])
def dohvacanje(pice):
   myquery = {"pice": pice}
   option = { "_id": 1, "ime": 1, "ocjena": 1 , "url": 1,"pice":1}
   return json_util.dumps((list(Pjesme.find(myquery,option).sort("ocjena",-1))))


#READ CRUD - Getanje pića
@app.route('/api/pjesme/<pice>/<id>', methods=['GET'])
def dohvati_posebno(pice,id):
   print("Ovaj je id:" + id)
   myquery = {"_id": ObjectId(id),"pice": pice}
   return json_util.dumps(list(Pjesme.find(myquery)))


#CREATE CRUD - Upis pjesama u databazu
@app.route('/api/pjesme', methods=['POST'])
def upis_u_bazu():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   data["ocjena"] = int(data["ocjena"])
   Pjesme.insert_one(data)
   return data

#UPDATE CRUD - Izmjena ocjene
@app.route('/api/pjesme/<id>', methods=['PATCH'])
def izmjena_ocjene(id):
   data = request.get_json()
   mydict = data
   print(json_util.dumps(data))
   id = ObjectId(data['_id']['$oid'])
   myquery = { "_id":id}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Pjesme.update_one(myquery, newvalues)
   return data

#DELETE CRUD - Brisanje pjesama iz databaze
@app.route('/api/pjesme/<id>', methods=['DELETE'])
def brisanje_pjesme(id):
   data = request.get_json()
   mydict = data
   print(json_util.dumps(data))
   id = ObjectId(data['_id'])
   myquery = { "_id":id}
   Pjesme.delete_one(myquery)
   return data

#Upis komentara u databazu
@app.route('/api/pjesme', methods=['POST'])
def dodavanje_komentara_u_bazu():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   Komentari.insert_one(data)
   return data

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
   
