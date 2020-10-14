from pymongo import MongoClient 
#client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')
db = client.admin
#db = client['admin']
mycol = db["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
print (db,":::::::::::::::::::::::")
