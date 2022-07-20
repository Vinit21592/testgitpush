import pymongo
client = pymongo.MongoClient("mongodb+srv://Vinit21592:Vinit21592#@cluster0.dl9uoq9.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email":"sudhanshu@ineuron.ai",
    "surname":"kumar"
}

d1 = {
    "name":"vinit",
    "email":"vinit.londhe21@gmail.com",
    "surname":"londhe"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)