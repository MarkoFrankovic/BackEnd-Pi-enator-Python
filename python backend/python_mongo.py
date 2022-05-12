import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

mydb = myclient["Pjesme"]
print(mydb.list_collection_names())

Jaeger = mydb["Pjesme_Jaeger"]
Bambus = mydb["Pjesme_Bambus"]
Voda = mydb["Pjesme_Voda"]
Gin = mydb["Pjesme_Gin"]
Travarica = mydb["Pjesme_Travarica"]
Vodka = mydb["Pjesme_Vodka"]
Jack = mydb["Pjesme_Jack"]
Merlot = mydb["Pjesme_Merlot"]
Stock = mydb["Pjesme_Bambus"]

mydoc1 = Jaeger.find().sort("ocjena",-1)
mydoc2 = Bambus.find().sort("ocjena",-1)
mydoc3 = Voda.find().sort("ocjena",-1)
mydoc4 = Gin.find().sort("ocjena",-1)
mydoc5 = Travarica.find().sort("ocjena",-1)
mydoc6 = Vodka.find().sort("ocjena",-1)
mydoc7 = Jack.find().sort("ocjena",-1)
mydoc8 = Merlot.find().sort("ocjena",-1)
mydoc9 = Stock.find().sort("ocjena",-1)

for x in mydoc1:
  print(x)
