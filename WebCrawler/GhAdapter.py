# Helps to adept the system to data from the Geizhals source.

import DataKeys

KEY_LENSNAME = DataKeys.key_lensname_as_gh
KEY_FOCAL_LENGTH = DataKeys.key_focal_length_as_gh
KEY_APERTURE = DataKeys.key_aperture_as_gh
KEY_FILTER = DataKeys.key_filter_as_gh
KEY_MAGNIFICATION = DataKeys.key_magnification_as_gh
KEY_MOUNT = DataKeys.key_mount_as_gh
KEY_SENSORKOMPATIBILITÄT = DataKeys.key_sensor_compatibility_as_gh
KEY_WEIGHT = DataKeys.key_weight_as_gh
KEY_SIZE = DataKeys.key_size_as_gh

ALL_KEYS = list(DataKeys.gh_keys_dict.values())

SORT_OUT_STRINGS_FOR_TITLE=[
	"verschiedene Modelle",
	"Pro Set"
]

def get_all_attributes(prodDesc,prodImg):
	
	result_dict = {
		KEY_LENSNAME: get_lens_name(prodImg)
	}
	result_dict.update(
		get_all_proddesc_attributes(prodDesc)
	)

	return result_dict

def check_if_raw_prodsite_is_valid(rawProdSite):
	for current_sort_out_string in SORT_OUT_STRINGS_FOR_TITLE:
		if(current_sort_out_string in rawProdSite):
			return False

	return True	

def check_if_data_is_valid(prodImg):
	title = get_lens_name_from_prodimg(prodImg)
	if(title == ""):
		return True

	for current_sort_out_string in SORT_OUT_STRINGS_FOR_TITLE:
		if(current_sort_out_string in title):
			return False

	return True


def get_all_proddesc_attributes(prodDesc):
	return {
		KEY_FOCAL_LENGTH: get_focal_length(prodDesc), 
		KEY_APERTURE: get_aperture(prodDesc),
		KEY_FILTER: get_filter(prodDesc), 
		KEY_MAGNIFICATION: get_magnification(prodDesc),
		KEY_MOUNT: get_mount(prodDesc),
		KEY_SENSORKOMPATIBILITÄT: get_sensor(prodDesc),
		KEY_WEIGHT: get_weight(prodDesc),
		KEY_SIZE: get_size(prodDesc)
	}

def get_lens_name(raw_lensname):
	if("<title>" in raw_lensname):
		return get_lens_name_from_title(raw_lensname)
	else:
		return get_lens_name_from_prodimg(raw_lensname)

def get_lens_name_from_title(title):
	return get_attribute_value("<title>",title," Preisvergleich")

def get_lens_name_from_prodimg(prodImg):
	return get_attribute_value(KEY_LENSNAME,prodImg,'"">')

def get_focal_length(prodDesc):
	focalLength = get_attribute_value(KEY_FOCAL_LENGTH,prodDesc," ")
	if("-" in focalLength):
		return focalLength.replace("-", " - ")
	else:
		return focalLength

def get_aperture(prodDesc):
	return get_attribute_value(KEY_APERTURE,prodDesc," ")

def get_filter(prodDesc):
	filterSize = get_attribute_value(KEY_FILTER,prodDesc," ")
	if("mm" not in filterSize):
		return ""
	else:
		return filterSize

def get_magnification(prodDesc):
	return get_attribute_value(KEY_MAGNIFICATION,prodDesc," ")

def get_mount(prodDesc):
	return get_attribute_value(KEY_MOUNT,prodDesc,"  ")
	
def get_sensor(prodDesc):
	return get_attribute_value(KEY_SENSORKOMPATIBILITÄT,prodDesc,"  ")

def get_weight(prodDesc):
	weight_without_letter_g = get_attribute_value(KEY_WEIGHT,prodDesc,"g")
	correctedWeight = correct_weight_without_letter_g(weight_without_letter_g)
	return correctedWeight

def get_size(prodDesc):
	size = get_attribute_value(KEY_SIZE,prodDesc," ")
	if(" x  " in size):
		return size
	else:
		return size.replace("x"," x ")

def get_attribute_value(key,string,valueTillKey):
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

def create_next_gh_overview_page(next_page_raw_url):
	print("bla: " + next_page_raw_url)
	tmpResult = get_attribute_value('href="',next_page_raw_url,'"')
	result = tmpResult.replace(".","https://geizhals.de",1)
	print("bla: " + result)
	return result

def convert_dict_to_csv_value_string(dict):
	current_value = ""
	current_key = ""
	current_index = 0
	result = ""

	while(current_index < len(ALL_KEYS)):
		current_key = ALL_KEYS[current_index]
		try:
			current_value = dict[current_key]

			result += current_value
			if(current_index != len(ALL_KEYS)-1):
				result += ";"
			current_index += 1
		except KeyError:
			result = convert_dict_to_csv_value_string(create_empty_dict)
			current_index = len(ALL_KEYS)


	return result

def create_empty_dict():
	empty_dict = {}
	for current_key in ALL_KEYS:
		empty_dict.update({current_key: ""})
	return empty_dict

def correct_weight_without_letter_g(weight_without_letter_g):
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