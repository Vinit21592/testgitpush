import pymongo

client = pymongo.MongoClient("mongodb+srv://Vinit21592:Vinit21592#@cluster0.dl9uoq9.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database["vins"]

#record = collection.find()
#for i in record:
    #print(i)

#data = collection.find({"companyName" : "iNeuron"})
data = collection.find({"courseOffered" : {"$gt" :"E"}})     #$gt means greater than
for i in data:
    print(i)
