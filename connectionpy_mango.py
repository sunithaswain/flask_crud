from pymongo import MongoClient
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')
db = client.admin
#db = client['admin']
mycol = db["customers"]
mydict = { "Age": "25", "Technology": "Python","Desgination":"senior" }
x = mycol.insert_one(mydict)
print (x,":::::::::::::::::::::::")
# mydict2=["sunitha","sunitha","antha"]
# n1=mydict2.distinct("sunitha")
print (mydict)

# mytest = db["customers_test"]
# mydict1={"name" :"sunita" , "address": "hyd"}
# y=mytest.insert_one(mydict1)
# print (y,"PPPPPPP")
#delete certain records
# d=mytest.remove({"name":"John"})
# print (d)
# d2=mycol.find({})
# print (d2)
#delete alll records
# d=mycol.remove({})
# print (d)
# d2=mycol.find({})
# print (d2)
#serachor filter records
# s=mycol.find({"name":"sunitha"})
# print (s,"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
# update the record
# u=db.Employee.update(
# {"Employeeid" : 1},
# {$set: { "EmployeeName" : "NewMartin"}});
