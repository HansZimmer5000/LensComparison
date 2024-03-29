

from webcrawler.persistency.mongoaccess import MongoAccess
from webcrawler.persistency.lensintegration import LensIntegration
from webcrawler.persistency import rawdataaccess


class MongoToCsv():

    def __init__(self, mongo_db_name):
        self.__mongo_db_name = mongo_db_name
        self.__mongo_access = MongoAccess()
        self.__get_all_collection_names()

    def gather_integrate_export_all_lenses(self):
        for name in self.collection_names:
            print("Collection: " + name)

        self.__gather_all_lens_dicts_of_each_domain()
        for tmp_dict in self.__list_wich_all_domain_lens_dicts:
            print("Size: " + str(len(tmp_dict)) + " Items")

        self.__combine_all_lens_dicts_of_each_domain()
        print("end size: " + str(len(self.__all_integrated_lenses)))
        self.__write_to_csv()

    def __get_all_collection_names(self):
        self.collection_names = self.__mongo_access.get_collection_names_of_db("lens_db")

    def __gather_all_lens_dicts_of_each_domain(self): 
        #__list_wich_all_domain_lens_dicts has each index a list, one per domain
        # In these lists are all the lenses we got from a certain domain.
        # the dicts are: Lensname(Key) to Lensdict (Value). 
        #TODO: Map / Reduce in MongoAccess?
        self.__list_wich_all_domain_lens_dicts = []
        for collection_name in self.collection_names:
            print("Collecting from: " + collection_name)
            self.__mongo_access.connect_to_db_and_collection("lens_db", collection_name)
            domain_dict = self.__mongo_access.find_all_lenses_into_one_dict()
            self.__list_wich_all_domain_lens_dicts.append(domain_dict)

    def __combine_all_lens_dicts_of_each_domain(self):
        self.__gather_all_domain_lens_dict_keys()
        self.__gather_and_integrate_sources_per_lens()

    def __write_to_csv(self):
        rawdataaccess.clean_rawdata_file_and_write_titles()

        print("Writing Data: ")
        for lens_dict in self.__all_integrated_lenses:
            rawdataaccess.append_clean_lensdata_dict_to_rawdata(lens_dict)
            print(".", end="")
        print("")
         

    def __gather_all_domain_lens_dict_keys(self):
        self.key_set = set()

        for domain_lens_dict in self.__list_wich_all_domain_lens_dicts:
            self.key_set.update(domain_lens_dict.keys()) 

    def __gather_and_integrate_sources_per_lens(self):
        self.__all_integrated_lenses = []
        
        print("Gather and Integrate Lenses:")
        for key in self.key_set:
            self.__gather_and_integrate_sources_for_key(key)
        print("") 

    def __gather_and_integrate_sources_for_key(self, key):
        dataset = self.__gather_all_lens_dicts_of_all_domains_with_key(key)
        integrated_lens = self.__integrate_dataset(dataset)
        self.__all_integrated_lenses.append(integrated_lens)

    def __gather_all_lens_dicts_of_all_domains_with_key(self, key):
        dataset = []
        for domain_lens_dict in self.__list_wich_all_domain_lens_dicts:
            print(".", end="")
            try:
                dataset.append(domain_lens_dict[key])
            except KeyError:
                print("Unknown Key: " + key + " in: " + str(domain_lens_dict))
        return dataset

    def __integrate_dataset(self, dataset):
        lens_integration = LensIntegration(dataset)
        return lens_integration.integrate()
