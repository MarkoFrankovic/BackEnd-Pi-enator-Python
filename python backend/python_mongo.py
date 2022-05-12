import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

mydb = myclient["Pjesme"]
mycol = mydb["Pjesme_Bambus"]

print(mydb.list_collection_names())

for x in mycol.find():
  print(x)
