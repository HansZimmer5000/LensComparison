
SORT_OUT_STRINGS_FOR_TITLE=[
"verschiedene Modelle",
"Pro Set"
]

START_URL = 'https://photographylife.com/lenses/page/1'


def get_href_value(link):
        pos_of_href = link.find('href="')
        tmp_res = link[pos_of_href+ len('href="'):]
        pos_end = tmp_res.find('"')
        return tmp_res[:pos_end]

def get_list_of_lenses_from_ov_page(response):
    found_links = set()
    for elem in response.xpath("//a"):
        current_link = elem.extract()
        if("/lenses/" in current_link and "title=" in current_link):
            cleaned_link = get_href_value(current_link)
            if(not(cleaned_link in found_links)):
                found_links.add(cleaned_link)

    return found_links

def get_next_overview_page(response):
    for elem in response.xpath("//link"):
        current_link = elem.extract()
        if("next" in current_link):
            return current_link
