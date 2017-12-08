from .crawledlens import CrawledLens


class GhLens(CrawledLens):

    key_lensname_in_title = 'title=""'
    key_focal_length_in_proddesc = "Brennweite: "
    key_aperture_in_proddesc = "Lichtstärke: "
    key_filter_in_proddesc = "Filterdurchmesser: "
    key_magnification_in_proddesc = "Abbildungsmaßstab: "
    key_minimalfocus_in_proddesc = "Naheinstellgrenze: "
    key_mount_in_proddesc = "Objektivbajonett: "
    key_sensor_compatibility_in_proddesc = "Sensorkompatibilität: "
    key_weight_in_proddesc = "Gewicht: "
    key_size_in_proddesc = "Abmessungen (ØxL): "

    def __init__(self, gh_site):
        self.lens_dict = lens_dict
        super().__init__()