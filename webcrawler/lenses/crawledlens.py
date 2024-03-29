
from webcrawler.lenses import datakeys

class CrawledLens:

    KEY_MOUNT = datakeys.key_mount_as_title

    def __init__(self, lens_dict):
        self.lens_dict = lens_dict
        self.keys_with_missing_value = self.__get_keys_with_missing_value(lens_dict)    

    def __get_keys_with_missing_value(self, lens_dict):
        result = []
        for key in lens_dict:
            value = lens_dict[key]
            if(value == ""):
                result.append(key)
        return result


    def __add_new_mount(self, new_lens_dict):
        new_mount = new_lens_dict[self.KEY_MOUNT]
        old_mounts = self.lens_dict[self.KEY_MOUNT]
        if((new_mount != "") and not(new_mount in old_mounts)):
            self.lens_dict.update({self.KEY_MOUNT: old_mounts + ", " + new_mount})

    def __add_new_value(self, new_lens_dict):
        #keys have to be copied, otherwise deletion in if makes problems! Like running (for) but then the floor gets pulled away (remove in if)
        old_keys_with_missing_value = self.keys_with_missing_value.copy()

        for current_missing_key in old_keys_with_missing_value:
            current_new_value = new_lens_dict[current_missing_key]
            if(current_new_value != ""):
                self.keys_with_missing_value.remove(current_missing_key)
                self.lens_dict.update({current_missing_key: current_new_value})        

    def update(self, new_lens_dict):
        self.__add_new_mount(new_lens_dict)

        if(len(self.keys_with_missing_value) > 0):
            self.__add_new_value(new_lens_dict)


    def equals(self, other):
        if(type(self) == type(other)):
            return self.lens_dict == other.lens_dict and \
                    self.keys_with_missing_value == other.keys_with_missing_value
        else:
            return False
