from CrawledLens import CrawledLens
from MongoAccess import MongoAccess
import DataKeys

#Data looks like:
# {lensname: CrawledLens, lensname2: CrawledLens2, ...}

class CrawledLenses:
    
    def __init__(self, db_name, collection_name):
        self.mongo_access = MongoAccess()
        self.mongo_access.connect_to_db_and_collection(db_name, collection_name)
        self.lenses = self.mongo_access.find_all_lenses()

    def new_lens_dict(self, lens_dict):
        lens_name = lens_dict[DataKeys.key_lensname_as_title]
        if(self.__lens_exists(lens_name)):
            old_crawled_lens = self.lenses[lens_name]
            old_crawled_lens.update(lens_dict) #TODO: Does this really also update our crawledlens in dict?
            self.mongo_access.update_lens(old_crawled_lens.lens_dict)
        else:
            crawled_lens = CrawledLens(lens_dict)
            self.lenses.update({lens_name: crawled_lens})
            self.mongo_access.add_lens(lens_dict)

    def __lens_exists(self, lens_name):
        try:
            self.lenses[lens_name]
            return True
        except:
            return False
