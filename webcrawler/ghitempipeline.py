
#from .baseitempipeline import BaseItemPipeline
import DataKeys
from CrawledLenses import CrawledLenses


class GhItemPipeline(object):
    
    KEY_LENSNAME = DataKeys.key_name_as_gh
    KEY_FOCAL_LENGTH = DataKeys.key_focal_length_as_gh
    KEY_APERTURE = DataKeys.key_aperture_as_gh
    KEY_FILTER = DataKeys.key_filter_as_gh
    KEY_MAGNIFICATION = DataKeys.key_magnification_as_gh
    KEY_MINIMALFOCUS = DataKeys.key_minimalfocus_as_gh
    KEY_MOUNT = DataKeys.key_mount_as_gh
    KEY_SENSORKOMPATIBILITÄT = DataKeys.key_sensor_compatibility_as_gh
    KEY_WEIGHT = DataKeys.key_weight_as_gh
    KEY_SIZE = DataKeys.key_size_as_gh

    ALL_KEYS = list(DataKeys.gh_keys_dict.values())

    SORT_OUT_STRINGS_FOR_TITLE=[
        "verschiedene Modelle",
        "Pro Set"
    ]

    def open_spider(self, spider):
        self.crawled_lenses = CrawledLenses("lens_db","geizhals_lens_coll")

    def process_item(self, item, spider):
        raw_lens_name = item["name"]
        raw_lens_info = item["info"]

        clean_lens_info = self.__clear_string(raw_lens_info)
        clean_lens_name = self.__clear_string(raw_lens_name)

        new_gh_lens_dict = self.__get_all_attributes(clean_lens_info,clean_lens_name)
        new_lens_dict = self.__transform_gh_dict_to_general_dict(new_gh_lens_dict)
		
        self.crawled_lenses.new_lens_dict(new_lens_dict)


    def __transform_gh_dict_to_general_dict(self, gh_lens_dict):
        new_lens_dict = {}
        for key_as_title in DataKeys.gh_keys_dict:
            key_as_gh = DataKeys.gh_keys_dict[key_as_title]
            gh_value = gh_lens_dict[key_as_gh]
            new_lens_dict.update({key_as_title: gh_value})
        return new_lens_dict

    def __clear_string(self, string_to_clear):

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

    def __get_all_attributes(self, prodDesc,prodImg):
        
        result_dict = {
            self.KEY_LENSNAME: self.__get_lens_name(prodImg)
        }
        result_dict.update(
            self.__get_all_proddesc_attributes(prodDesc)
        )

        return result_dict

    def __get_all_proddesc_attributes(self, prodDesc):
        return {
            self.KEY_FOCAL_LENGTH: self.__get_focal_length(prodDesc), 
            self.KEY_APERTURE: self.__get_aperture(prodDesc),
            self.KEY_FILTER: self.__get_filter(prodDesc), 
            self.KEY_MAGNIFICATION: self.__get_magnification(prodDesc),
            self.KEY_MINIMALFOCUS: self.__get_minimalfocus(prodDesc),
            self.KEY_MOUNT: self.__get_mount(prodDesc),
            self.KEY_SENSORKOMPATIBILITÄT: self.__get_sensor(prodDesc),
            self.KEY_WEIGHT: self.__get_weight(prodDesc),
            self.KEY_SIZE: self.__get_size(prodDesc)
        }

    def __get_lens_name(self, raw_lensname):
        if("<title>" in raw_lensname):
            lens_name = self.__get_lens_name_from_title(raw_lensname)
        else:
            lens_name = self.__get_lens_name_from_prodimg(raw_lensname)
        if(" für" in lens_name):
            #Cut all after "für", plus cut also the empty space before "für", so thats why " für".
            lens_name = lens_name[:lens_name.find(" für")]
        elif(lens_name != ""):
            #Cut of the color
            if("(" in lens_name.rsplit(' ', 1)[1] and ")" in lens_name.rsplit(' ', 1)[1]):
                lens_name = lens_name.rsplit(" ", 2)[0]
            else:
                lens_name = lens_name.rsplit(" ", 1)[0]
        return lens_name

    def __get_lens_name_from_title(self, title):
        return self.__get_attribute_value("<title>",title," Preisvergleich")

    def __get_lens_name_from_prodimg(self, prodImg):
        return self.__get_attribute_value(self.KEY_LENSNAME,prodImg,'"">')

    def __get_focal_length(self, prodDesc):
        focalLength = self.__get_attribute_value(self.KEY_FOCAL_LENGTH,prodDesc," ")
        focalLength = focalLength.replace(" ", "")
        return focalLength

    def __get_aperture(self, prodDesc):
        result = self.__get_attribute_value(self.KEY_APERTURE,prodDesc," ")
        result = result.replace(" ", "")
        return result

    def __get_filter(self, prodDesc):
        filterSize = self.__get_attribute_value(self.KEY_FILTER,prodDesc," ")
        if("mm" not in filterSize):
            filterSize = ""
        else:
            filterSize = filterSize

        return filterSize

    def __get_magnification(self, prodDesc):
        result = self.__get_attribute_value(self.KEY_MAGNIFICATION,prodDesc," ")
        if("." not in result and result != ""):
            result = result + ".00"
        result = result.replace(" ","")
        return result

    def __get_minimalfocus(self, prodDesc):
        return self.__get_attribute_value(self.KEY_MINIMALFOCUS, prodDesc, " ")
        
    def __get_mount(self, prodDesc):
        return self.__get_attribute_value(self.KEY_MOUNT,prodDesc,"  ")
        
    def __get_sensor(self, prodDesc):
        return self.__get_attribute_value(self.KEY_SENSORKOMPATIBILITÄT,prodDesc,"  ")

    def __get_weight(self, prodDesc):
        weight_without_letter_g = self.__get_attribute_value(self.KEY_WEIGHT,prodDesc,"g")
        correctedWeight = self.__correct_weight_without_letter_g(weight_without_letter_g)
        return correctedWeight

    def __get_size(self, prodDesc):
        size = self.__get_attribute_value(self.KEY_SIZE,prodDesc,"mm")
        size = size.replace("/","x")
        size = size.replace(" ","")
        if(size != ""):
            size = size + "mm"
        return size

    def __get_attribute_value(self, key,string,valueTillKey):
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

    def __correct_weight_without_letter_g(self, weight_without_letter_g):
        if(weight_without_letter_g == ""):
            return ""
        else:
            if("k" in weight_without_letter_g):
                string_length = len(weight_without_letter_g)
                weight_without_letters = weight_without_letter_g[:string_length-1]
                weight_without_letters_as_float = float(weight_without_letters)
                corrected_gramm_weight_as_float = weight_without_letters_as_float * 1000
                corrected_gramm_weight_as_long = int(corrected_gramm_weight_as_float) #So we have a round number
                return str(corrected_gramm_weight_as_long)+"g"
            else:
                return weight_without_letter_g + "g"