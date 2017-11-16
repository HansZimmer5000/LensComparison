# DataKeys handles all the keys for the data at one place.
# Also it translates the different keys of the data sources to other datas keys and also the (for better readbility) titles.

key_lensname_as_title = "Lensname"
key_focal_length_as_title = "Focal Length"
key_aperture_as_title ="Aperture"
key_filter_as_title = "Filtersize"
key_magnification_as_title = "Magnification"
key_minimalfocus_as_title = "Minimal Focus"
key_mount_as_title = "Mount"
key_sensor_compatibility_as_title = "Sensor compatibility"
key_weight_as_title = "Weight"
key_size_as_title = "Size"

all_keys_as_titles_in_order = [
    key_lensname_as_title,
    key_focal_length_as_title,
    key_aperture_as_title,
    key_filter_as_title,
    key_magnification_as_title,
    key_mount_as_title,
    key_sensor_compatibility_as_title,
    key_weight_as_title,
    key_size_as_title,
]

#Translation from normal Key to Geizhals Keys
key_lensname_as_gh = 'title=""'
key_focal_length_as_gh = "Brennweite: "
key_aperture_as_gh = "Lichtstärke: "
key_filter_as_gh = "Filterdurchmesser: "
key_magnification_as_gh = "Abbildungsmaßstab: "
key_minimalfocus_as_gh = "Naheinstellgrenze: "
key_mount_as_gh = "Objektivbajonett: "
key_sensor_compatibility_as_gh = "Sensorkompatibilität: "
key_weight_as_gh = "Gewicht: "
key_size_as_gh = "Abmessungen (ØxL): "

gh_keys_dict = {
    key_lensname_as_title: key_lensname_as_gh,
    key_focal_length_as_title: key_focal_length_as_gh,
    key_aperture_as_title: key_aperture_as_gh,
    key_filter_as_title: key_filter_as_gh,
    key_magnification_as_title: key_magnification_as_gh,
    key_minimalfocus_as_title: key_minimalfocus_as_gh,
    key_mount_as_title: key_mount_as_gh,
    key_sensor_compatibility_as_title: key_sensor_compatibility_as_gh,
    key_weight_as_title: key_weight_as_gh,
    key_size_as_title: key_size_as_gh
}