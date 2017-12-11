
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
#-----------------------------

def get_href_value(link):
        pos_of_href = link.find('href="')
        tmp_res = link[pos_of_href+ len('href="'):]
        pos_end = tmp_res.find('"')
        return tmp_res[:pos_end]

def get_list_of_lenses_from_ov_page(ov_code):
    akku = 0
    found_links = set()
    for elem in Selector(text=site_code).xpath("//a"):
        current_link = elem.extract()
        if("/lenses/" in current_link and "title=" in current_link):
            cleaned_link = get_href_value(current_link)
            if(not(cleaned_link in found_links)):
                akku = akku + 1
                found_links.add(cleaned_link)
    print(str(akku) + " links found in get_list_of_lenses_from_ov_page.")
    return found_links

def get_next_overview_page(site_code):
    first = True
    for elem in Selector(text=site_code).xpath("//link"):
        current_link = elem.extract()
        if("next" in current_link):
            return current_link

#--------------------

def get_lens_name(site_code):
    elems = Selector(text=site_code).xpath("//h3")
    h3 = elems.extract_first()
    pos_of_spec = h3.find("Spec")
    return h3[4:pos_of_spec]

def get_dict_from_table(site_code):
    table = Selector(text=site_code).xpath("//table").extract_first()
    #<tr> -> <td> <td>
    #print(table)
    pos_first_td = table.find("<td>")
    pos_last_end_td = table.rfind("</td>")
    table = table[pos_first_td:pos_last_end_td]
    rows = table.split("<tr>")

    result_dict = {}
    for row in rows:
        if("</td><td>" in row):
            row = row.replace("</tr>","")
            head = row.split("</td><td>")[0].replace("</td>","").replace("<td>", "")
            data = row.split("</td><td>")[1].replace("</td>","").replace("<td>", "")
            result_dict.update({head: data})
    return result_dict

if __name__ == "__main__":
    from scrapy.selector import Selector
    #testov = open("plovsite.txt","r")
    #site_code = testov.read()
    #for elem in get_list_of_lenses_from_ov_page(site_code):
    #    print(elem)
    #print(get_next_overview_page(site_code)) 

    #testlens = open("pllenssite.txt", "r")
    #site_code = testlens.read()
    #get_lens_name(site_code)
    #print(get_dict_from_table(site_code))
    