
#from .baseitempipeline import BaseItemPipeline
from webcrawler.lenses import datakeys
from webcrawler.lenses.crawledlenses import CrawledLenses


class PlItemPipeline(object):
    
    KEY_LENSNAME = datakeys.key_name_as_pl
    KEY_FOCAL_LENGTH = datakeys.key_focal_length_as_pl
    KEY_APERTURE = datakeys.key_aperture_as_pl
    KEY_FILTER = datakeys.key_filter_as_pl
    KEY_MAGNIFICATION = datakeys.key_magnification_as_pl
    KEY_MINIMALFOCUS = datakeys.key_minimalfocus_as_pl
    KEY_MOUNT = datakeys.key_mount_as_pl
    KEY_SENSOR_COMPATIBILITY = datakeys.key_sensor_compatibility_as_pl
    KEY_WEIGHT = datakeys.key_weight_as_pl
    KEY_SIZE = datakeys.key_size_as_pl

    ALL_KEYS = list(datakeys.pl_keys_dict.values())

    SORT_OUT_STRINGS_FOR_TITLE=[
        "verschiedene Modelle",
        "Pro Set"
    ]

    def open_spider(self, spider):
        pass
        #self.crawled_lenses = CrawledLenses("lens_db","photolife_lens_coll")

    def process_item(self, item, spider):
        new_pl_lens_dict = self.clean_dict(item)
        new_lens_dict = self.transform_pl_dict_to_general_dict(new_pl_lens_dict)
        return new_lens_dict
        #self.crawled_lenses.new_lens_dict(new_lens_dict)


    def transform_pl_dict_to_general_dict(self, pl_lens_dict):
        new_lens_dict = {}
        for key_as_title in datakeys.pl_keys_dict:
            key_as_pl = datakeys.pl_keys_dict[key_as_title]
            pl_value = pl_lens_dict[key_as_pl]
            new_lens_dict.update({key_as_title: pl_value})
        return new_lens_dict

    
    def clean_dict(self, lens_dict):
        return {
            self.KEY_LENSNAME: lens_dict[self.KEY_LENSNAME],
            self.KEY_FOCAL_LENGTH: self.__clean_focal_length(lens_dict[self.KEY_FOCAL_LENGTH]),
            self.KEY_APERTURE: self.__clean_aperture(lens_dict[self.KEY_APERTURE]),
            self.KEY_FILTER: self.__clean_filtersize(lens_dict[self.KEY_FILTER]),
            self.KEY_MAGNIFICATION: lens_dict[self.KEY_MAGNIFICATION],
            self.KEY_MINIMALFOCUS: self.__clean_minimal_focus(lens_dict[self.KEY_MINIMALFOCUS]),
            self.KEY_MOUNT: lens_dict[self.KEY_MOUNT],
            self.KEY_SENSOR_COMPATIBILITY: self.__clean_sensor_compatibility(lens_dict[self.KEY_SENSOR_COMPATIBILITY]),
            self.KEY_WEIGHT: self.__clean_weight(lens_dict[self.KEY_WEIGHT]),
            self.KEY_SIZE: self.__clean_size(lens_dict[self.KEY_SIZE])
        }


    def __clean_focal_length(self, value):
        return value.replace("mm", "")

    def __clean_aperture(self, value):
        return value.replace("f/", "")

    def __clean_filtersize(self, value):
        return value.replace("mm", "")

    def __clean_minimal_focus(self, value):
        open_bracket_pos = value.find("(")
        cm_pos = value.find(" cm")
        value_in_cm = float(value[open_bracket_pos+1:cm_pos])
        value_in_m = value_in_cm / 100
        return str(value_in_m)

    def __clean_sensor_compatibility(self, value):
        #TODO: Mittleformat, Four-Thirds, Nikon CX
        if("full" in value):
            return "APS-C/ Kleinbild"
        elif("APS-C" in value):
            return "APS-C"
        else:
            return value

    def __clean_weight(self, value):
        open_bracket_pos = value.find("(")
        kg_pos = value.find(" kg")
        value_in_kg = float(value[open_bracket_pos+1:kg_pos])
        value_in_g = value_in_kg * 1000
        return str(value_in_g)

    def __clean_size(self, value):
        #Mögliche Values:
        #'3.0 in. (77 mm) x 2.8 in. (73 mm)'
        #'Approx. 3.46 x 7.5'
        return value

    
