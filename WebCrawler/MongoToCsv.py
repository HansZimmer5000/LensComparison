from MongoAccess import MongoAccess
import pymongo
import GhAdapter
import DataKeys
import LensIntegration

class MongoToCsv():

    def __init__(self, mongo_db_name):
        self.mongo_db_name = mongo_db_name

    def __get_all_collection_names(self):
        client = pymongo.MongoClient()
        collection_names = client[self.mongo_db_name].collection_names()
        return collection_names

    def __gather_all_lens_dicts_of_each_domain(self, collection_names): 
        domain_lens_dicts_list = []
        for collection_name in collection_names:
            print("Collecting from: " + collection_name)
            domain_lens_dicts_list.append(MongoAccess("lens_db", collection_name).find_all_lenses())
        return domain_lens_dicts_list

    def __combine_all_lens_dicts_of_each_domain(self, domain_lens_dicts_list):
        # new result dict
        # new key set
        # get all keys of all dicts -> add to key set
        #   for each key get dataset of each dict
        #   try to intergrate datasets -> add to result dict
        # If all keys are done -> return result dict
        result_list = []
        key_set = set()

        for domain_lens_dict in domain_lens_dicts_list:
            for key in domain_lens_dict.keys():
                key_set.add(key)
        
        print("Gathering Data:")
        for key in key_set:
            datasets = []
            for domain_lens_dict in domain_lens_dicts_list:
                print(".", end="")
                try:
                    datasets.append(domain_lens_dict[key].lens_dict)
                except KeyError:
                    print("Unknown Key: " + key + " in: " + str(domain_lens_dict))
            result = LensIntegration.integrate(datasets)
            result_list.append(result)
        print("")
        return result_list        

    def __write_to_csv(self, lens_dicts):
        file_name = "mongoRawData.csv"
        file = open(file_name, "w")
        print("Writing Data: ")
        for lens_dict in lens_dicts:
            string = GhAdapter.convert_dict_to_csv_value_string(lens_dict)
            print(".", end="")
            file.write(string + "\n")
        print("")
        file.close()

def export_all_lenses(self):
    COLLECTION_NAMES = self.__get_all_collection_names()
    for name in COLLECTION_NAMES:
        print("Collection: " + name)
    ALL_LENS_DICTS = self.__gather_all_lens_dicts_of_each_domain(COLLECTION_NAMES)
    for tmp_dict in ALL_LENS_DICTS:
        print("Size: " + str(len(tmp_dict)) + " Items")
    ALL_LENSES_INTEGRATED = self.__combine_all_lens_dicts_of_each_domain(ALL_LENS_DICTS)
    print("end size: " + str(len(ALL_LENSES_INTEGRATED)))
    self.__write_to_csv(ALL_LENSES_INTEGRATED)