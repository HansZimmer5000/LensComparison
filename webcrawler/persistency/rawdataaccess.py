# RawData is about the access to the same called file.
# Its here to unclutter the other files and sperate the concerns

# CSV can handle a maximum of 32759 characters in one cells
from webcrawler.lenses import datakeys

__full_path_of_rawdata_file = "C:/Users/Michael/IdeaProjects/LensComparison/WebCrawler/rawData.csv"

def clean_rawdata_file_and_write_titles():
    #clean
    rawdata_file = open(__full_path_of_rawdata_file, 'w') 
    #write titles
    for current_key in datakeys.all_keys_as_titles_in_order:
        rawdata_file.write(current_key+";")
    rawdata_file.write("\n")
    rawdata_file.close()

def append_clean_lensdata_dict_to_rawdata(lens_dict):
    rawdata_file = open(__full_path_of_rawdata_file,"a")
    for current_key in lens_dict.keys():
        rawdata_file.write(lens_dict[current_key]+";")

    rawdata_file.write("\n")
    rawdata_file.close()