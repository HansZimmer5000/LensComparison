from MongoAccess import MongoAccess
import pymongo
import GhAdapter

def get_all_collection_names():
    client = pymongo.MongoClient()
    collection_names = client["lens_db"].collection_names()
    return collection_names

def gather_all_lens_dicts_of_each_domain(collection_names): 
    domain_lens_dicts_list = []
    for collection_name in collection_names:
        print("Collecting from: " + collection_name)
        domain_lens_dicts_list.append(MongoAccess("lens_db", collection_name).find_all_lenses())
    return domain_lens_dicts_list

def __unite_different_lenses_to_one(lenses):
    result_lens = {}

    for lens in lenses:
        #TODO: Implement
        result_lens = lens

    return result_lens

def combine_all_lens_dicts_of_each_domain(domain_lens_dicts_list):
    # new result dict
    # new key set
    # get all keys of all dicts -> add to key set
    #   for each key get dataset of each dict
    #   try to unite datasets -> add to result dict
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
            except:
                pass
        result = __unite_different_lenses_to_one(datasets)
        result_list.append(result)
    print("")
    return result_list        

def write_to_csv(lens_dicts):
    file_name = "mongoRawData.csv"
    file = open(file_name, "w")
    print("Writing Data: ")
    for lens_dict in lens_dicts:
        string = GhAdapter.convert_dict_to_csv_value_string(lens_dict)
        print(".", end="")
        file.write(string + "\n")
    print("")
    file.close()

collection_names = get_all_collection_names()
for name in collection_names:
    print("Collection: " + name)
lens_dicts = gather_all_lens_dicts_of_each_domain(collection_names)
for dict in lens_dicts:
    print("Size: " + str(len(dict)) + " Items")
result = combine_all_lens_dicts_of_each_domain(lens_dicts)
print("end size: " + str(len(result)))
write_to_csv(result)