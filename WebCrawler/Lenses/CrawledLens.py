from abc import ABC
from abc import abstractmethod
from .. import DataKeys

class CrawledLens(ABC):

    def __init__(self):
        self.keys_with_missing_value = self.__gather_keys_with_missing_value(self.lens_dict)
        self.key_lens_name = DataKeys.key_name_as_title
        self.key_focal_length = DataKeys.key_focal_length_as_title
        self.key_aperture = DataKeys.key_aperture_as_title
        self.key_filter = DataKeys.key_filter_as_title
        self.key_magnification = DataKeys.key_magnification_as_title
        self.key_minimalfocus = DataKeys.key_minimalfocus_as_title
        self.key_mount = DataKeys.key_mount_as_title
        self.key_sensor = DataKeys.key_sensor_as_title
        self.key_weight = DataKeys.key_weight_as_title
        self.key_size = DataKeys.key_size_as_title

    @property
    def get_lens_name(self):
        return self.lens_name
    @get_lens_name.setter
    def set_lens_name(self, new_lens_name):
        self.lens_name = new_lens_name

    @property
    def get_lens_dict(self):
        return self.lens_dict
    @get_lens_dict.setter
    def set_lens_dict(self, new_lens_dict):
        self.lens_dict = new_lens_dict


    def __gather_keys_with_missing_value(self, lens_dict):
        result = []
        for key in lens_dict:
            value = lens_dict[key]
            if(value == ""):
                result.append(key)
        return result

    def update(self, new_lens_dict):
        self.__add_new_mount(new_lens_dict)

        if(len(self.keys_with_missing_value) > 0):
            self.__add_new_value(new_lens_dict)

    def __add_new_mount(self, new_lens_dict):
        new_mount = new_lens_dict[self.key_mount]
        old_mounts = self.lens_dict[self.key_mount]
        if((new_mount != "") and not(new_mount in old_mounts)):
            self.lens_dict.update({self.key_mount: old_mounts + ", " + new_mount})

    def __add_new_value(self, new_lens_dict):
        #keys have to be copied, otherwise deletion in if makes problems! Like running (for) but then the floor gets pulled away (remove in if)
        old_keys_with_missing_value = self.keys_with_missing_value.copy()

        for current_missing_key in old_keys_with_missing_value:
            current_new_value = new_lens_dict[current_missing_key]
            if(current_new_value != ""):
                self.keys_with_missing_value.remove(current_missing_key)
                self.lens_dict.update({current_missing_key: current_new_value})        

    def equals(self, other):
        try:
            issubclass_of_crawledlens = issubclass(other, CrawledLens)
        except TypeError:
            return False

        if(issubclass_of_crawledlens):
            return self.lens_dict == other.lens_dict and \
                self.keys_with_missing_value == other.keys_with_missing_value
        else:
            return False

