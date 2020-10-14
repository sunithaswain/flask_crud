from pymongo import MongoClient 
#client = MongoClient()
client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017')
db = client.admin
print (db)
#db = client['admin']
#mycol = db["customers"]
#print (mycol,":::::::::::::::::::::::")