from MongoAccess import MongoAccess
import pymongo
import GhAdapter
import DataKeys
from LensIntegration import LensIntegration

class MongoToCsv():

    def __init__(self, mongo_db_name):
        self.mongo_db_name = mongo_db_name

    def __get_all_collection_names(self):
        client = pymongo.MongoClient()
        self.collection_names = client[self.mongo_db_name].collection_names()

    def __gather_all_lens_dicts_of_each_domain(self): 
        self.domain_lens_dicts_list = []
        for collection_name in self.collection_names:
            print("Collecting from: " + collection_name)
            self.domain_lens_dicts_list.append(MongoAccess("lens_db", collection_name).find_all_lenses())

    def __combine_all_lens_dicts_of_each_domain(self):
        # new result dict
        # new key set
        # get all keys of all dicts -> add to key set
        #   for each key get dataset of each dict
        #   try to intergrate datasets -> add to result dict
        # If all keys are done -> return result dict
        self.all_integrated_lenses = []
        key_set = set()

        for domain_lens_dict in self.domain_lens_dicts_list:
            for key in domain_lens_dict.keys():
                key_set.add(key)
        
        print("Gathering Data:")
        for key in key_set:
            datasets = []
            for domain_lens_dict in self.domain_lens_dicts_list:
                print(".", end="")
                try:
                    datasets.append(domain_lens_dict[key].lens_dict)
                except KeyError:
                    print("Unknown Key: " + key + " in: " + str(domain_lens_dict))
            lens_integration = LensIntegration(datasets)
            tmp_result = lens_integration.integrate()
            self.all_integrated_lenses.append(tmp_result)
        print("")      

    def __write_to_csv(self):
        file_name = "mongoRawData.csv"
        file = open(file_name, "w")
        print("Writing Data: ")
        for lens_dict in self.all_integrated_lenses:
            string = GhAdapter.convert_dict_to_csv_value_string(lens_dict)
            print(".", end="")
            file.write(string + "\n")
        print("")
        file.close()


    def export_all_lenses(self):
        self.__get_all_collection_names()
        for name in self.collection_names:
            print("Collection: " + name)

        self.__gather_all_lens_dicts_of_each_domain()
        for tmp_dict in self.domain_lens_dicts_list:
            print("Size: " + str(len(tmp_dict)) + " Items")

        self.__combine_all_lens_dicts_of_each_domain()
        print("end size: " + str(len(self.all_integrated_lenses)))
        self.__write_to_csv()