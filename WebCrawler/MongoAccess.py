
import pymongo
import subprocess
import DataKeys

class MongoAccess:

    __DB_PATH = "C:/Users/Michael/AppData/Local/MongoDB/LensComparison"
    __MONGO_BIN = "C://Program Files//MongoDB//Server//3.4//bin//mongod"

    __KEY_LENSNAME = DataKeys.key_lensname_as_title

    def __init__(self, collection_name):
        self.__collection_name = collection_name
        self.__mongod_process = None

    def start_mongo_server(self):
        start_command = self.__MONGO_BIN + " --dbpath " + self.__DB_PATH
        #self.__mongod_process = subprocess.Popen(start_command)
        self.client = pymongo.MongoClient()
        self.collection = self.client["lens_db"][self.__collection_name]

    def stop_mongo_server(self):
        if(self.__mongod_process != None):
            self.__mongod_process.terminate()
            self.__mongod_process = None

    def add_lens(self, lens_name, lens_dict):
        lens_name = lens_name.replace(".",",")
        lens = {lens_name: lens_dict}
        print("lens_name: " + lens_name)
        print("lens_dict: " + str(lens_dict))
        self.collection.insert_one(lens)

    def update_lens(self, lens):
        lensname = lens[self.__KEY_LENSNAME]
        return self.collection.update_one({self.__KEY_LENSNAME: lensname}, {'$set': lens}) 

    def find_all_lenses(self):
        result = {}
        for elem in self.collection.find({}):
            result.update(elem)

        return result

    def delete_all_lenses(self):
        self.collection.delete_many({})

    def get_lens_count(self):
        return self.collection.count()