# This Module is about getting the Data from the rawResponse files which are just 1:1 downloads of each product site, into the RawData csv.

# Flow
# 1. Get Fullpath + Name of rawResponse Files
# 2. Open RawData File
# 3. Take rawResponse file and extract for each lens the import data (if existent)
#   A. Get Row as one string, columns differ with ";"
#   B. Get (if existent, else just "") data from columns:
#       1. Column = proddesc ------   Always there, but may not complete
#       2. till n-1. Column = Links   Sometimes there
#       n. Column = prodimg -------   Sometimes there
#           Data            Looks like                  get from
#       - Full Lensname (Text with numbers)         prodimg // Links (href != "href=./")
#       - Focal Length  (000mm - 000mm // 000mm)    proddesc
#       - Aperture      (F/0.0 - 0.0)               proddesc
#       - Filterthread  (00mm)                      proddesc
#       - Magnification (0.26X // 1,00 // 1:3)      proddesc
#       - Mount         (Nikon F // Canon EF// ...) proddesc
#       - Sensor Compatibility (Full-Frame // APS-C) proddesc
#       - Weight        (000g)                      proddesc
#       - Size          (Diameter x Length"mm")     proddesc
#   D. Return to Step 4 with this extracted data.
# 4. Write this data to RawData file, because some files are big its may better to write directly every n rows, till last row is reached.
# 5. Close current rawResponse file, continue at 3 with the next rawResponse file.
# 6. If every rawResponse file is done, close RawData file.

from glob import glob
import GhAdapter
import RawDataAccess

# Module Variables
total_processesd_rows = 0
total_written_rows = 0

# Module Constants
EMPTY_DICT = GhAdapter.create_empty_dict()

def getall_raw_response_full_paths(directory):
    raw_response_file_name = "rawResponse*.csv"
    return glob(directory + raw_response_file_name)

def extract_raw_response_file_and_write_to_rawdata(raw_response_file):
    MAX_DICT_LIST_SIZE = 1000 #As it gets bigger it gets faster.
    global total_processesd_rows

    #Open file and go through every row, then give rowtext (rows differs by '\n') to extract_data_from_raw_response_row
    row_texts = raw_response_file.read().split("\n")
    row_text_count = len(row_texts)
    current_dict_list = []
    current_row_index = 0

    while(current_row_index < row_text_count):
        #Save each return dict in a list, if list is bigger than *n* save into rawData file.

        current_row_text = row_texts[current_row_index]
        if(GhAdapter.check_if_raw_prodsite_is_valid(current_row_text)):
            current_dict = extract_data_from_raw_response_row(current_row_text)
            current_dict_list.append(current_dict)
            if((len(current_dict_list) == MAX_DICT_LIST_SIZE) or (current_row_index == row_text_count - 1)):
                write_extracted_dicts_to_rawdata(current_dict_list)
                current_dict_list = []

        current_row_index += 1
        total_processesd_rows += 1
    

def extract_data_from_raw_response_row(row):
    #find proddesc, search for name in prodimg / links
    #return all found data in a dict.
    PROD_DESC_INDEX = 0

    proddesc = get_proddesc_from_raw_site(row)
    prodimg = get_prodimg_from_raw_site(row)

    result_dict = GhAdapter.get_all_attributes(proddesc, prodimg)
    # If there is no prodimg, the lens will have a empty lensname -> let them just aside?
    return result_dict

def write_extracted_dicts_to_rawdata(dictList):
    global total_written_rows
    
    for current_dict in dictList:
        if(current_dict != EMPTY_DICT):
            total_written_rows += 1
            RawDataAccess.append_clean_lensdata_dict_to_rawdata(current_dict)

def get_prodimg_from_raw_site(raw_site):
    index_of_prodimg_tag = raw_site.find("gh_prodImg")
    if(index_of_prodimg_tag < 0):
        return ""
    else:
        prodimg = raw_site[index_of_prodimg_tag+1:]
        return prodimg

def get_proddesc_from_raw_site(raw_site):
    index_of_prodimg_tag = raw_site.find("gh_prodImg")
    if(index_of_prodimg_tag < 0):
        return raw_site
    else:
        proddesc = raw_site[:index_of_prodimg_tag]
        return proddesc

if __name__ == "__main__":
    #If this module is not imported, do this code

    RAW_RESPONSE_DIR = "C:/Users/Michael/IdeaProjects/NikonLensComparison/WebCrawler/"

    print("Type 'clean' to clean the rawDataFile, 'import' to import new Data or 'repair' to repair the 'rawResponseData 12 - 60.csv file'.")
    user_input = input()

    if(user_input == "import"):
        all_raw_response_full_paths = getall_raw_response_full_paths(RAW_RESPONSE_DIR)

        for current_raw_response_full_path in all_raw_response_full_paths:
            print(current_raw_response_full_path)
            raw_response_file = open(current_raw_response_full_path,"r")
            extract_raw_response_file_and_write_to_rawdata(raw_response_file)
            raw_response_file.close()

        print("Total Count of Processed Rows: " + str(total_processesd_rows))
        print("Total Count of Written Rows: " + str(total_written_rows))

    elif(user_input == "clean"):
        RawDataAccess.clean_rawdata_file_and_write_titles()

    elif(user_input == "repair"):
        #Replaces "whatever characters" with the right ones (see mappingDict)
        file = open("rawResponseData 12 - 60.csv","r")
        oldLines = file.readlines()
        newLines = []
        file.close()

        oldLine = ""
        newLine = ""

        mappingDict = {
            "Ã¤": "ä",
            "Ã˜": "Ø",
            "ÃŸ": "ß",
            "Ã¼": "ü"
        }
        for oldLine in oldLines:
            newLine = oldLine
            for key in mappingDict:
                value = mappingDict[key]
                print(key + " " + value)
                newLine = newLine.replace(key,value)
                
            newLines.append(newLine)

        file = open("rawResponseData 12 - 60 repaired.csv","w")
        file.writelines(newLines)
