import subprocess
import pymongo
import time

DB_PATH = "C:/Users/Michael/AppData/Local/MongoDB/LensComparison"
MONGO_BIN = "C://Program Files//MongoDB//Server//3.4//bin//mongod"
COMMAND = MONGO_BIN + " --dbpath " + DB_PATH

def start_mongo_server():
    p = subprocess.Popen(COMMAND)
    return p

def stop_mongo_server(p):
    COMMAND = "net stop MongoDB"
    COMMAND = "taskkill /f /im mongod.exe"
    subprocess.Popen(COMMAND)
    #p.terminate()

p = start_mongo_server()
client = pymongo.MongoClient()
db = client.test_database
collection = db["test_collection"]


time.sleep(2)

new_doc = {"a": "value von A"}

def insert_doc():
    new_doc_id = collection.insert_one(new_doc).inserted_id
    print("insert: " + str(new_doc_id))

def find_doc():
    found_doc = collection.find({"a": "value von A"})
    for elem in found_doc:
        print("find: " + str(elem))

def find_all_doc():
    found_docs = collection.find({})
    for elem in found_docs:
        print("found all: " + str(elem))

def update_doc():
    result = collection.update_one({"a": "value von A"}, {'$set': {"a": "new_value"}})
    print("update: " + str(result))

insert_doc()
find_doc()
update_doc()
find_all_doc()

print(collection.count())
collection.delete_many({})
print(collection.count())
stop_mongo_server(p)