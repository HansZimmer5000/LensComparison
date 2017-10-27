# RawData is about the access to the same called file.
# Its here to unclutter the other files and sperate the concerns

import DataKeys

__full_path_of_rawdata_file = "C:/Users/Michael/IdeaProjects/NikonLensComparison/WebCrawler/rawData.csv"

def clean_rawdata_file_and_write_titles():
    #clean
    rawdata_file = open(__full_path_of_rawdata_file, 'w') 
    #write titles
    for current_key in DataKeys.all_keys_as_titles_in_order:
        rawdata_file.write(current_key+";")
    rawdata_file.write("\n")
    rawdata_file.close()

def append_lensdata_dict_to_rawdata(lensDataDict):
    rawdata_file = open(__full_path_of_rawdata_file,"a")
    for current_key in lensDataDict.keys():
        rawdata_file.write(lensDataDict[current_key]+";")

    rawdata_file.write("\n")
    rawdata_file.close()

def append_raw_desc_title_to_rawdata(proddesc, prodimg_or_title):
	rawdata_file = open(__full_path_of_rawdata_file, "a")
	cleared_proddesc = __clear_proddesc_string(proddesc)
	cleared_prodimg_or_title = __clear_prodImg_or_title_string(prodimg_or_title)
	rawdata_file.write(cleared_proddesc + ";" + cleared_prodimg_or_title + "\n")
	rawdata_file.close()

def __clear_proddesc_string(string):
    return __clear_string(string)

def __clear_prodImg_or_title_string(string):
    if(string is None):
        return ""
    else:
        return __clear_string(string)

def __clear_string(string):
    forbidden_strings = [
        "\x95",
        "\u200b",
        "\n"
    ]
    replacement_letter = " "
	
    for current_forbidden_string in forbidden_strings:
        string.replace(current_forbidden_string,replacement_letter)
    
    return string