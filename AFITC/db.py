######################################################################
#   need these libriaries to run, and mongodb needs to be installed...

import json
import pymongo
import pandas

##############################################
#   fills the database using the given json file...
def populate_database(fileName):#fileName is a string.
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["AFITC"]

    mycol = mydb["retailers"]

    mycol.drop()

    data = dict()

    with open(fileName, 'r') as infile:
        data = json.load(infile)

    for i in data:
        data[i]["_id"] = i
        insert = mycol.insert_one(data[i])




##############################################
#   appends the database using the given json file.
#   Becareful of duplicate _id #'s...
def append_database(fileName):#fileName is a string.
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["AFITC"]

    mycol = mydb["retailers"]

    data = dict()

    with open(fileName, 'r') as infile:
        data = json.load(infile)

    for i in data:
        data[i]["_id"] = i
        insert = mycol.insert_one(data[i])




############################################
############################################
#   exports a json file matching the logical layout of the database...
def export_database(fileName):#fileName is a string.
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["AFITC"]

    mycol = mydb["retailers"]

    cursor = mycol.find()

    mongo_docs = list(cursor)

    docs = pandas.DataFrame(columns=[])

    for num, doc in enumerate(mongo_docs):
        doc["_id"] = str(doc["_id"])
        doc_id = doc["_id"]
        series_obj = pandas.Series( doc, name=doc_id )
        docs = docs.append(series_obj)

    #docs.to_json("object_rocket.json")
    json_export = docs.to_json() # return JSON data
    with open(fileName,'w') as outfile:
        outfile.write(json_export)




####################################################
#   returns a json file containing the results to a full
#   query.  Queries in mongodb are dictionaries where
#   the key and value matches whats in the database...
def query_database(query):#query is a dictionary.
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["AFITC"]

    mycol = mydb["retailers"]

    mydoc = mycol.find(query)

    replies = []

    for x in mydoc:
        replies.append(x)

    with open("response.json", 'w') as outfile:
        json.dump(replies,outfile)





##################################################
#   Returns a json file of all results where the 
#   item is available...
def available_item_query(item):#item is a string.
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["AFITC"]

    mycol = mydb["retailers"]

    mydoc = mycol.find({item : "Available"})

    replies = []

    for x in mydoc:
        replies.append(x)

    with open("response.json", 'w') as outfile:
        json.dump(replies,outfile)




##################################################
#   Returns a json file of all results where the 
#   item is unavailable...
def unavailable_item_query(item):#item is a string.
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["AFITC"]

    mycol = mydb["retailers"]

    mydoc = mycol.find({item : "Unavailable"})

    replies = []

    for x in mydoc:
        replies.append(x)

    with open("response.json", 'w') as outfile:
        json.dump(replies,outfile)




####################EXAMPLES#############################

#to fill the database...
populate_database("outifle.json")
append_database("outifle2.json")

#to export the database...
export_database("database.json")

##########QUERIES################

query_database({"brand":"Target"})
#available_item_query("cannedFood")
#available_item_query("paperTowels")
#unavailable_item_query("sanitizer")




