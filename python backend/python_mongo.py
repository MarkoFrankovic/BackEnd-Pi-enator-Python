import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

mydb = myclient["Pjesme"]
Bambus = mydb["Pjesme_Bambus"]

print(mydb.list_collection_names())

for x in Bambus.find():
  print(x)
