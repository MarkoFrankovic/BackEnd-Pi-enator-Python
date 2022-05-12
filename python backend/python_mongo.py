import pymongo
from flask import Flask
app = Flask(__name__)

myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

mydb = myclient["Pjesme"]
#print(mydb.list_collection_names())

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

for x in mydoc1:
    print(x)


#@app.route('/')
#def hello_world():
   #return "Hello World"

#@app.route('/jaeger')
#def jaeger():
  # return "Dobar dan"
   

#if __name__ == '__main__':
  # app.run()
