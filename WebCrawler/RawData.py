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

def append_clean_lensdata_dict_to_rawdata(lensDataDict):
    rawdata_file = open(__full_path_of_rawdata_file,"a")
    for current_key in lensDataDict.keys():
        rawdata_file.write(lensDataDict[current_key]+";")

    rawdata_file.write("\n")
    rawdata_file.close()

def append_raw_desc_raw_lensname_to_rawdata(proddesc, raw_lensname):
    rawdata_file = open(__full_path_of_rawdata_file, "a")
    cleared_proddesc = clear_string(proddesc)
    cleared_raw_lensname = clear_string(raw_lensname)
    rawdata_file.write(cleared_proddesc + ";" + cleared_raw_lensname + "\n")
    rawdata_file.close()

def append_raw_lens_page_to_rawdata(raw_lenspage):
    rawdata_file = open(__full_path_of_rawdata_file, "a")
    cleared_raw_lenspage = clear_string(raw_lenspage)
    rawdata_file.write(cleared_raw_lenspage+"\n")
    rawdata_file.close()

def clear_string(string_to_clear):

    if(string_to_clear is None):
        return ""

    forbidden_strings = [
        "\x95",
        "\u200b",
        "\n",
        ";"
    ]
    replacement_letter = " "
    cleared_string = string_to_clear
    for current_forbidden_string in forbidden_strings:
        cleared_string = cleared_string.replace(current_forbidden_string,replacement_letter)
    
    return cleared_string