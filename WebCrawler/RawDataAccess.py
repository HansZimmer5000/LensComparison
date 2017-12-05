# RawData is about the access to the same called file.
# Its here to unclutter the other files and sperate the concerns

# CSV can handle a maximum of 32759 characters in one cells
import DataKeys

__full_path_of_rawdata_file = "C:/Users/Michael/IdeaProjects/LensComparison/WebCrawler/rawData.csv"

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

def append_raw_desc_raw_lens_name_to_rawdata(proddesc, raw_lens_name):
    rawdata_file = open(__full_path_of_rawdata_file, "a")
    cleared_proddesc = clear_string(proddesc)
    cleared_raw_lens_name = clear_string(raw_lens_name)
    rawdata_file.write(cleared_proddesc + ";" + cleared_raw_lens_name + "\n")
    rawdata_file.close()

def append_raw_lens_page_to_rawdata(raw_lenspage):
    rawdata_file = open(__full_path_of_rawdata_file, "a")
    cleared_raw_lenspage = clear_string(raw_lenspage)
    if("DOCTYPE" in cleared_raw_lenspage):
        cleared_raw_lenspage = "\n"+cleared_raw_lenspage
    rawdata_file.write(cleared_raw_lenspage)
    rawdata_file.close()

if __name__ == "__main__":
    rawdata_file = open(__full_path_of_rawdata_file,"r")
    all_lines = rawdata_file.readlines()
    print(len(all_lines))
    rawdata_file.close()

    rawdata_file = open(__full_path_of_rawdata_file,"w")
    for line in all_lines:
        clean_line = line.replace("\n","")
        rawdata_file.write(clean_line)
    rawdata_file.close()

    rawdata_file = open(__full_path_of_rawdata_file,"r")
    print(len(all_lines))
    rawdata_file.close()