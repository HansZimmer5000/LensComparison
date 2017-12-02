
import pymongo
import subprocess
import DataKeys
from CrawledLens import CrawledLens

#Data looks like:
# {lensname: CrawledLens, lensname2: CrawledLens2, ...}

class MongoAccess:

    __DB_PATH = "C:/Users/Michael/AppData/Local/MongoDB/LensComparison"
    __MONGO_BIN = "C://Program Files//MongoDB//Server//3.4//bin//mongod"

    __KEY_LENSNAME = DataKeys.key_lensname_as_title
    __KEY_LENSDICT = "lens_dict"

    def __init__(self, collection_name):
        #print("Mongod active? Start with 'mongod --dbpath C:/Users/Michael/AppData/Local/MongoDB/LensComparison' in a seperate Shell!")
        self.__collection_name = collection_name
        self.client = pymongo.MongoClient()
        self.collection = self.client["lens_db"][self.__collection_name]

    def add_lens(self, lens_dict):
        lens_name = lens_dict[self.__KEY_LENSNAME]
        lens_name = lens_name.replace(".","aAa")
        lens = {self.__KEY_LENSNAME: lens_name, self.__KEY_LENSDICT: lens_dict}
        return self.collection.insert_one(lens)

    def update_lens(self, lens_dict):
        lens_name = lens_dict[self.__KEY_LENSNAME]
        lens_name = lens_name.replace(".","aAa")
        return self.collection.update_one({self.__KEY_LENSNAME: lens_name}, {'$set': {self.__KEY_LENSDICT: lens_dict}}) 

    def find_all_lenses(self):
        result = {}
        for elem in self.collection.find({}):
            lens_name = elem[self.__KEY_LENSNAME]
            lens_name = lens_name.replace("aAa",".")
            lens_dict = elem[self.__KEY_LENSDICT]
            crawled_lens = CrawledLens(lens_dict)
            result.update({lens_name: crawled_lens})

        return result

    def delete_all_lenses(self):
        self.collection.delete_many({})

    def get_lens_count(self):
        return self.collection.count()