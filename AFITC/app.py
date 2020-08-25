from flask import Flask, render_template
#from bson import ObjectId
from pymongo import MongoClient
#import os

DOMAIN = "localhost"
MONGO_PORT = 27017
FLASK_PORT = 5000

mongo_app = Flask(__name__)

def get_connect(arg=''):
   # documents = {}

    try:
        client = MongoClient(host = [str(DOMAIN) + ":" + str(MONGO_PORT)])

     #   print("\nserver_info():", client.server_info()["versionArray"])

    except Exception as err:
        client = None

        print("MongoClient error:", err)

    if client != None:
        db = client.flaskDb
      #  col = db.sample

       # for doc in col.find():
        #    print("\n", doc)

         #   print(type(doc))

          #  documents["id"] = doc

   # return documents

@mongo_app.route('/')
def home_page():
    return render_template("index.html")

#@mongo_app.route("/api/v1/docs/", methods=['GET'])
#def get_docs():
 #   new_html = "<h2>Results returned:</h2><br>"

  #  docs = get_mongo_docs()

   # for k, doc in docs.items():
    #    for key, values in doc.items():
     #       new_html += "<h3>Key: " + str(key) + "</h3>"
      #      new_html += "<h4>Values: " + str(values) + "</h4><br>"

   # html = get_app_html(new_html)

   # return html

#title = "Available Cleaning Products"
#heading = "Product Map"

#client = MongoClient("mongodb://127.0.0.1:27017")
#db = client.mymongodb
#items = db.items

if __name__ == '__main__':
    mongo_app.run(host = DOMAIN, port = FLASK_PORT)
