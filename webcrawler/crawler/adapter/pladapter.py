
SORT_OUT_STRINGS_FOR_TITLE=[
    "verschiedene Modelle",
    "Pro Set"
]

START_URL = 'https://photographylife.com/lenses/page/1'

LINK_TAG_TO_LENS_IN_OVERVIEW_PAGE = '//a[@class = "productlist__link"]'
LINK_TAG_TO_NEXT_OVERVIEW_PAGE_IN_OVERVIEW_PAGE = '//a[@class = "gh_pag_i only--desktop gh_pag_i_last gh_pag_next_active"]'

LENS_INFO_TAG = '//div[@id="gh_proddesc"]'
LENS_NAME_TAG = '//title'

def clear_string(string_to_clear):

    if(string_to_clear is None):
        return ""

    forbidden_strings = [
        "\x95",
        "\u200b",
        "\n"
    ]
    replacement_letter = " "
    cleared_string = string_to_clear
    for current_forbidden_string in forbidden_strings:
        cleared_string = cleared_string.replace(current_forbidden_string,replacement_letter)
    
    return cleared_string

def create_next_gh_overview_page(next_page_raw_url):
    tmpResult = __get_attribute_value('href="',next_page_raw_url,'"')
    result = tmpResult.replace(".","https://geizhals.de",1)
    return result

def __get_attribute_value(key,string,valueTillKey):
    key_length = len(key)
    key_start_pos = string.find(key)

    if(key_start_pos >= 0):
        value_start_pos = key_start_pos + key_length
        raw_value = string[value_start_pos:]
        value_end_pos = raw_value.find(valueTillKey)
        value = raw_value[:value_end_pos]
        result = value
    else:
        result = ""

    if("<p>" in result):
        result = result.split("<p>")[0]

    return result

