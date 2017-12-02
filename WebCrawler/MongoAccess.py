
import pymongo
import subprocess
import DataKeys

class MongoAccess:

    __KEY_LENSNAME = DataKeys.key_lensname_as_title

    def __init__(self, collection_name):
        self.__collection_name = collection_name
        self.client = pymongo.MongoClient()
        self.collection = self.client["lens_db"][self.__collection_name]
        

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