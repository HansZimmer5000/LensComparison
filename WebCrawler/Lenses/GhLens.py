from CrawledLens import CrawledLens

class GhLens(CrawledLens):

    def __init__(self, lens_dict):
        self.lens_name = lens_dict["_id"]
        self.key_mount = "mount"
        self.lens_dict = lens_dict
        super().__init__()