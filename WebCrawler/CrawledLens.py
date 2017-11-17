import GhAdapter

class CrawledLens:

    def __init__(self, lens_dict):
        self.lens_name = lens_dict[GhAdapter.KEY_LENSNAME]
        self.lens_dict = lens_dict[GhAdapter.KEY_MOUNT]
        self.keys_with_missing_value = GhAdapter.get_keys_with_missing_value(lens_dict)    

    def update(self, new_lens_dict):
        if(len(self.keys_with_missing_value) > 0):
            for current_missing_key in self.keys_with_missing_value:
                current_new_value = new_lens_dict[current_missing_key]
                if(current_new_value != ""):
                    if(current_missing_key == GhAdapter.KEY_MOUNT):
                        old_mounts = self.lens_dict[current_missing_key]
                        new_mount = new_lens_dict[current_missing_key]
                        if(not new_mount in old_mounts):
                            old_mounts.append(new_mount)
                    else:
                        self.lens_dict.update({current_missing_key: current_new_value})