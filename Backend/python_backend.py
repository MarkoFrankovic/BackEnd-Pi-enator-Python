import pymongo
from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import bson.json_util as json_util
app = Flask(__name__)
cors = CORS(app,resources = {r"/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

#spajanje na bazu
#myclient = pymongo.MongoClient("mongodb", 27017, maxPoolSize=50)
myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

#izbor databaze
mydb = myclient["Pjesme"]
mydb2 = myclient["Komentari_za_ocjenu"]

#izbor kolekcija
Jaeger = mydb["Pjesme_Jaeger"]
Bambus = mydb["Pjesme_Bambus"]
Voda = mydb["Pjesme_Voda"]
Gin = mydb["Pjesme_Gin"]
Travarica = mydb["Pjesme_Travarica"]
Vodka = mydb["Pjesme_Vodka"]
Jack = mydb["Pjesme_Jack"]
Merlot = mydb["Pjesme_Merlot"]
Stock = mydb["Pjesme_Stock"]

Komentari = mydb2["Komentari"]

#READ CRUD - Getanje pića
@app.route('/getanje/<pice>')
def getanje(pice):
      if pice == "bambus":
         return jsonify(list(Bambus.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))
      elif pice == "jaeger":
         return jsonify(list(Jaeger.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))
      elif pice == "voda":
         return jsonify(list(Voda.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))
      elif pice == "gin":
         return jsonify(list(Gin.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))
      elif pice == "travarica":
         return jsonify(list(Travarica.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))
      elif pice == "vodka":
         return jsonify(list(Vodka.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))
      elif pice == "jack":
         return jsonify(list(Jack.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))
      elif pice == "merlot":
         return jsonify(list(Merlot.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))
      elif pice == "stock":
         return jsonify(list(Stock.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

#CREATE CRUD - Upis pjesama u databazu
@app.route('/upis', methods=['POST'])
def upis():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   pice = data.pop("pice")
   data["ocjena"] = int(data["ocjena"])
   
   if pice == "Jaeger":
      Jaeger.insert_one(data)
   elif pice == "Bambus":
      Bambus.insert_one(data)
   elif pice == "Voda":
      Voda.insert_one(data)
   elif pice == "Gin":
      Gin.insert_one(data)
   elif pice == "Travarica":
      Travarica.insert_one(data)
   elif pice == "Vodka":
      Vodka.insert_one(data)
   elif pice == "Jack":
      Jack.insert_one(data)
   elif pice == "Merlot":
      Merlot.insert_one(data)
   elif pice == "Stock":
      Stock.insert_one(data)
   return data

#UPDATE CRUD - Izmjena ocjene
@app.route('/izmjena', methods=['PATCH'])
def izmjena_pica():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   pice = data.pop("pice")
   
   if (pice == "Bambus"):
      Bambus.update_many(myquery, newvalues)
   elif (pice == "Jaeger"):
      Jaeger.update_many(myquery, newvalues)
   elif (pice == "Voda"):
      Voda.update_many(myquery, newvalues)
   elif (pice == "Vodka"):
      Vodka.update_many(myquery, newvalues)
   elif (pice == "Stock"):
      Stock.update_many(myquery, newvalues)
   elif (pice == "Gin"):
      Gin.update_many(myquery, newvalues)
   elif (pice == "Travarica"):
      Travarica.update_many(myquery, newvalues)
   elif (pice == "Jack"):
      Jack.update_many(myquery, newvalues)
   elif (pice == "Merlot"):
      Merlot.update_many(myquery, newvalues)
   return data

#DELETE CRUD - Brisanje pjesama iz databaze
@app.route('/delete', methods=['DELETE'])
def delete_pjesme():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "ime":  data["ime"]}
   pice = data.pop("pice")
   
   if (pice == "Bambus"):
      Bambus.delete_many(myquery)
   elif (pice == "Jaeger"):
      Jaeger.delete_many(myquery)
   elif (pice == "Voda"):
      Voda.delete_many(myquery)
   elif (pice == "Vodka"):
      Vodka.delete_many(myquery)
   elif (pice == "Stock"):
      Stock.delete_many(myquery)
   elif (pice == "Gin"):
      Gin.delete_many(myquery)
   elif (pice == "Travarica"):
      Travarica.delete_many(myquery)
   elif (pice == "Jack"):
      Jack.delete_many(myquery)
   elif (pice == "Merlot"):
      Merlot.delete_many(myquery)
   return data

#Upis komentara u databazu
@app.route('/upis_komentara', methods=['POST'])
def dodavanje_komentara():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   Komentari.insert_one(data)
   return data

if __name__ == '__main__':
   app.run(host="0.0.0.0")
   
