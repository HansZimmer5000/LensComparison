
import pymongo
import DataKeys

#Data looks like:
# {lensname: CrawledLens, lensname2: CrawledLens2, ...}

class MongoAccess:

    __KEY_LENSNAME = DataKeys.key_lensname_as_title
    __KEY_LENSDICT = "lens_dict"

    def __init__(self):
        self.client = pymongo.MongoClient()

    def get_collection_names_of_db(self, db_name):
        return self.client[db_name].collection_names()

    def connect_to_db_and_collection(self, db_name, collection_name):
        self.collection = self.client[db_name][collection_name]

    def add_lens(self, lens_dict):
        lens_name = lens_dict[self.__KEY_LENSNAME]
        lens_name = lens_name.replace(".","aAa")
        lens = {self.__KEY_LENSNAME: lens_name, self.__KEY_LENSDICT: lens_dict}
        return self.collection.insert_one(lens)

    def update_lens(self, lens_dict):
        lens_name = lens_dict[self.__KEY_LENSNAME]
        lens_name = lens_name.replace(".","aAa")
        return self.collection.update_one({self.__KEY_LENSNAME: lens_name}, {'$set': {self.__KEY_LENSDICT: lens_dict}}) 

    def find_all_lenses_into_one_dict(self):
        result = {}
        for elem in self.collection.find({}):
            lens_name = elem[self.__KEY_LENSNAME]
            lens_name = lens_name.replace("aAa",".")
            lens_dict = elem[self.__KEY_LENSDICT]
            result.update({lens_name: lens_dict})

        return result

    def delete_all_lenses(self):
        self.collection.delete_many({})

    def get_lens_count(self):
        return self.collection.count()