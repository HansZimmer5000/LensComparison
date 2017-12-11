
from webcrawler.spiders.baselensspider import BaseLensSpider
from webcrawler.spiders import spiderpladapter

class PlLensSpider(BaseLensSpider):

    name = "PlLensSpider"
    start_urls = [spiderpladapter.START_URL]
    custom_settings = {
        'ITEM_PIPELINES' : {
            'webcrawler.itempipelines.plitempipeline.PlItemPipeline': 300
        }
    }

    @property
    def adapter(self):
        return spiderpladapter

    def parse_lens_page(self, response):
        data_dict = self.get_dict_from_table(response)
        name_dict = self.get_lens_name(response)
        data_dict.update(name_dict)
        yield data_dict
        
    
    def get_lens_name(self, response):
        elems = response.xpath("//h3")
        h3 = elems.extract_first()
        pos_of_spec = h3.find("Spec")
        return {"Name": h3[4:pos_of_spec]}
    

    def get_dict_from_table(self, response):
        table = response.xpath("//table").extract_first()
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

    def create_lens_page_requests(self, response):
        for lens_page in self.get_list_of_lenses_from_ov_page(response):
            yield response.follow(lens_page, self.parse_lens_page)

    def create_overview_page_request(self, response):
        next_overview_page = self.get_next_overview_page(response)
        yield response.follow(next_overview_page, self.parse_overview_page)

    def get_href_value(self, link):
            pos_of_href = link.find('href="')
            tmp_res = link[pos_of_href+ len('href="'):]
            pos_end = tmp_res.find('"')
            return tmp_res[:pos_end]

    def get_list_of_lenses_from_ov_page(self, response):
        akku = 0
        found_links = set()
        for elem in response.xpath("//a"):
            current_link = elem.extract()
            if("/lenses/" in current_link and "title=" in current_link):
                cleaned_link = self.get_href_value(current_link)
                if(not(cleaned_link in found_links)):
                    akku = akku + 1
                    found_links.add(cleaned_link)

        return found_links

    def get_next_overview_page(self, response):
        first = True
        for elem in response.xpath("//link"):
            current_link = elem.extract()
            if("next" in current_link):
                return current_link
