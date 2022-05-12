import pymongo
myclient = pymongo.MongoClient(
    "mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

mydb = myclient["Pjesme"]
mycol = mydb["Pjesme.Bambus"]


myquery = {"ocjena": "4"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
