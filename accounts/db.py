import pymongo
connectionString ="mongodb+srv://sameepyogi:IutbM4HMd6b5SnoB@cluster0.j6xxjxf.mongodb.net/"
myclient = pymongo.MongoClient(connectionString)
# myclient.drop_database("CoCDB")