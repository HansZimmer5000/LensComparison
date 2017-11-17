import GhAdapter

class CrawledLens:

    def __init__(self, lens_dict):
        self.lens_name = lens_dict[GhAdapter.KEY_LENSNAME]
        self.lens_dict = lens_dict
        self.keys_with_missing_value = GhAdapter.get_keys_with_missing_value(lens_dict)    

    def update(self, new_lens_dict):
        new_mount = new_lens_dict[GhAdapter.KEY_MOUNT]
        old_mounts = self.lens_dict[GhAdapter.KEY_MOUNT]
        if((new_mount != "") and not(new_mount in old_mounts)):
            self.lens_dict.update({GhAdapter.KEY_MOUNT: old_mounts + ", " + new_mount})
            
        if(len(self.keys_with_missing_value) > 0):
            old_keys_with_missing_value = []

            #keys have to be copied, otherwise deletion in if makes problems! Like running (for) but then the floor gets pulled away (remove in if)
            for key in self.keys_with_missing_value:
                old_keys_with_missing_value.append(key)

            for current_missing_key in old_keys_with_missing_value:
                current_new_value = new_lens_dict[current_missing_key]
                if(current_new_value != ""):
                    self.keys_with_missing_value.remove(current_missing_key)
                    self.lens_dict.update({current_missing_key: current_new_value})


    def equals(self, other):
        if(type(self) == type(other)):
            return self.lens_name == other.lens_name and \
                    self.lens_dict == other.lens_dict and \
                    self.keys_with_missing_value == other.keys_with_missing_value
        else:
            return False
