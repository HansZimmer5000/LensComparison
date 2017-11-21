
from .items import LensItem
from scrapy.loader import ItemLoader

class GeizhalsItemloader():

    __KEY_LENSNAME = 'title=""'
    __KEY_FOCAL_LENGTH = "Brennweite: "
    __KEY_APERTURE = "Lichtstärke: "
    __KEY_FILTER = "Filterdurchmesser: "
    __KEY_MAGNIFICATION = "Abbildungsmaßstab: "
    __KEY_MINIMALFOCUS = "Naheinstellgrenze: "
    __KEY_MOUNT = "Objektivbajonett: "
    __KEY_SENSORKOMPATIBILITÄT = "Sensorkompatibilität: "
    __KEY_WEIGHT = "Gewicht: "
    __KEY_SIZE = "Abmessungen (ØxL): "

    __loader = None
    __item = None

    def __init__(self):
        self.__loader = ItemLoader(LensItem())

    def populate_from_proddesc_and_title(self, proddesc, title):
        proddesc = self.__clear_string(proddesc)
        title = self.__clear_string(title)
        self.__loader.add_value("lensname", self.__get_lens_name(title))
        self.__loader.add_value("focal_length", self.__get_focal_length(proddesc))
        self.__loader.add_value("aperture", self.__get_aperture(proddesc))
        self.__loader.add_value("filter", self.__get_filter(proddesc))
        self.__loader.add_value("magnification", self.__get_magnification(proddesc))
        self.__loader.add_value("minimalfocus", self.__get_minimalfocus(proddesc))
        self.__loader.add_value("mount", self.__get_mount(proddesc))
        self.__loader.add_value("sensor_compatibility", self.__get_sensor(proddesc))
        self.__loader.add_value("weight", self.__get_weight(proddesc))
        self.__loader.add_value("size", self.__get_size(proddesc))

    def get_item(self):
        return self.__loader.load_item()

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
        return self.__get_attribute_value(self.__KEY_LENSNAME, prodImg,'"">')

    def __get_focal_length(self, prodDesc):
        focalLength = self.__get_attribute_value(self.__KEY_FOCAL_LENGTH, prodDesc," ")
        focalLength = focalLength.replace(" ", "")
        return focalLength

    def __get_aperture(self, prodDesc):
        result = self.__get_attribute_value(self.__KEY_APERTURE,prodDesc," ")
        result = result.replace(" ", "")
        return result

    def __get_filter(self, prodDesc):
        filterSize = self.__get_attribute_value(self.__KEY_FILTER,prodDesc," ")
        if("mm" not in filterSize):
            filterSize = ""
        else:
            filterSize = filterSize

        return filterSize

    def __get_magnification(self, prodDesc):
        result = self.__get_attribute_value(self.__KEY_MAGNIFICATION,prodDesc," ")
        if("." not in result and result != ""):
            result = result + ".00"
        result = result.replace(" ","")
        return result

    def __get_minimalfocus(self, prodDesc):
        return self.__get_attribute_value(self.__KEY_MINIMALFOCUS, prodDesc, " ")
        
    def __get_mount(self, prodDesc):
        return self.__get_attribute_value(self.__KEY_MOUNT,prodDesc,"  ")
        
    def __get_sensor(self, prodDesc):
        return self.__get_attribute_value(self.__KEY_SENSORKOMPATIBILITÄT,prodDesc,"  ")

    def __get_weight(self, prodDesc):
        weight_without_letter_g = self.__get_attribute_value(self.__KEY_WEIGHT,prodDesc,"g")
        correctedWeight = self.__correct_weight_without_letter_g(weight_without_letter_g)
        return correctedWeight

    def __get_size(self, prodDesc):
        size = self.__get_attribute_value(self.__KEY_SIZE,prodDesc,"mm")
        size = size.replace("/","x")
        size = size.replace(" ","")
        if(size != ""):
            size = size + "mm"
        return size

    def __get_attribute_value(self, key, string, value_till_key):
        key_length = len(key)
        key_start_pos = string.find(key)

        if(key_start_pos >= 0):
            value_start_pos = key_start_pos + key_length
            raw_value = string[value_start_pos:]
            value_end_pos = raw_value.find(value_till_key)
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
