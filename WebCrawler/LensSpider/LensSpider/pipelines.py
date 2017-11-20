# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class LensspiderPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.csv', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = self.__convert_dict_values_to_csv_string(dict(item)) + "\n"
        self.file.write(line)
        return item

    def __convert_dict_values_to_csv_string(self, dict):
        csv_string = ""
        for key in dict.keys():
            csv_string = csv_string + str(dict[key]) + ";"
        return csv_string