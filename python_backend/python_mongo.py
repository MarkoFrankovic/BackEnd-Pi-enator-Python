import pymongo
from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import bson.json_util as json_util
app = Flask(__name__)
cors = CORS(app,resources = {r"/*":{"origins":"*"}})
app.run(host="0.0.0.0")
app.config['CORS_HEADERS'] = 'Content-Type'

myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

myclient2 = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

mydb2 = myclient["Autentifikacija"]
Korisnici = mydb2["Korisnici"]

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
   return jsonify(list(Jaeger.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/bambus')
def bambus():
   return jsonify(list(Bambus.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/voda')
def voda():
   return jsonify(list(Voda.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/gin')
def gin():
   return jsonify(list(Gin.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/travarica')
def travarica():
   return jsonify(list(Travarica.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/vodka')
def vodka():
   return jsonify(list(Vodka.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/jack')
def jack():
   return jsonify(list(Jack.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/merlot')
def merlot():
   return jsonify(list(Merlot.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/stock')
def stock():
   return jsonify(list(Stock.find({},{ "_id": 0, "ime": 1, "ocjena": 1 , "url": 1}).sort("ocjena",-1)))

@app.route('/autentifikacija')
def autentifikacija():
   return jsonify(list(Korisnici.find({},{ "_id": 0, "username": 1, "password": 1})))

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

@app.route('/izmjena_jaeger', methods=['POST'])
def izmjena_jaeger():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Jaeger.update_many(myquery, newvalues)
   return data

@app.route('/izmjena_bambus', methods=['POST'])
def izmjena_bambus():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Bambus.update_many(myquery, newvalues)
   return data

@app.route('/izmjena_voda', methods=['POST'])
def izmjena_voda():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Voda.update_many(myquery, newvalues)
   return data

@app.route('/izmjena_gin', methods=['POST'])
def izmjena_gin():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Gin.update_many(myquery, newvalues)
   return data

@app.route('/izmjena_travarica', methods=['POST'])
def izmjena_travarica():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Travarica.update_many(myquery, newvalues)
   return data

@app.route('/izmjena_vodka', methods=['POST'])
def izmjena_vodka():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Vodka.update_many(myquery, newvalues)
   return data

@app.route('/izmjena_jack', methods=['POST'])
def izmjena_jack():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Jack.update_many(myquery, newvalues)
   return data

@app.route('/izmjena_merlot', methods=['POST'])
def izmjena_merlot():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Merlot.update_many(myquery, newvalues)
   return data

@app.route('/izmjena_stock', methods=['POST'])
def izmjena_stock():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   myquery = { "url":  data["url"]}
   newvalues = { "$set": { "ocjena": data["ocjena"] } }
   Stock.update_many(myquery, newvalues)
   return data

@app.errorhandler(400)
def bad_request(error):
   return ({"code":400, "message":error.description},400)

if __name__ == '__main__':
   app.run()
