from abc import ABC
from abc import abstractmethod

class CrawledLens(ABC):

    def __init__(self):
        self.keys_with_missing_value = self.__gather_keys_with_missing_value(self.lens_dict)

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

    @property
    def __get_key_mount(self):
        return self.key_mount

    @__get_key_mount.setter
    def __set_key_mount(self, new_key_mount):
        self.key_mount = new_key_mount

    @property
    def __get_keys_with_missing_value(self):
        return self.keys_with_missing_value

    @__get_keys_with_missing_value.setter
    def __set_keys_with_missing_value(self, new_keys_with_missing_value):
        self.keys_with_missing_value = new_keys_with_missing_value


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

