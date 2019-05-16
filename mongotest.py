import pymongo

mongo_url='mongodb+srv://wnstjrdlrj:dkagh1025!@cluster0-7nxpj.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client, 'Cluster0')
users = pymongo.collection.Collection(db, 'Users')
users.insert_one({"userEmail":"wnstjrdlrj@gmail.com","userPassword":"1234"})
