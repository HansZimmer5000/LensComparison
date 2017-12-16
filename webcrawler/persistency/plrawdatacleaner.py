
def clean_dict(dict):
    return {
        "_id": clean_name(dict["_id"]),
        'Focal Length': clean_focal(dict['Focal Length']),
        'Aperture': clean_aperture(dict["Aperture"]),
        'Filtersize': clean_filter(dict["Filtersize"]),
        'Magnification': clean_magni(dict["Magnification"]),
        'Minimal Focus': clean_minimal(dict["Minimal Focus"]),
        'Mount': clean_mount(dict["Mount"]),
        'Sensor compatibility': clean_sensor(dict["Sensor compatibility"]),
        'Weight': clean_weight(dict["Weight"]),
        'Size': clean_size(dict["Size"])
    }

def clean_name(value):
    return value[:len(value) - 1]

def clean_focal(value):
    return value

def clean_aperture(value):
    value = value.replace("f/","")
    return "1:" + value

def clean_filter(value):
    if("N/A" in value):
        return ""
    else:
        return value

def clean_magni(value):
    if("x" in value):
        value = value.replace("x","")
        float_value = round(1 / float(value), 2)
        return "1:" + str(float_value)
    else:
        return value

def clean_minimal(value):
    if((not ("in" in value)) and (not ("m" in value))):
        return ""
    elif("m" in value):
        pos_of_last_m = value.rfind("m")
        pos_of_first_m = value.find("m")
        if(pos_of_first_m == pos_of_last_m or pos_of_first_m == pos_of_last_m - 1):
            value = value[: pos_of_last_m + 1]
            value = value.replace(" ", "")
            if("(" in value):
                pos_of_bracket = value.find("(")
                value = value[pos_of_bracket + 1:]

            if("cm" in value):
                value = value.replace("cm","")
                float_value = float(value) / 100
                return str(float_value)+"m"
            elif("mm" in value):
                value = value.replace("mm","")
                float_value = float(value) / 1000
                return str(float_value)+"m"
            else:
                return value
        else:
            pos_of_first_m = value.find("m")
            value = value[:pos_of_first_m + 1]
            if("cm" in value):
                value = value.replace("cm","")
                float_value = float(value) / 100
                return str(float_value)+"m"
            elif("mm" in value):
                value = value.replace("mm","")
                float_value = float(value) / 1000
                return str(float_value)+"m"
            else:
                return value

def clean_mount(value):
    return value

def clean_sensor(value):
    uppercase_value = value.upper()
    if("FULL" in uppercase_value):
        return "APS-C/ Kleinbild"
    if("APS-C" in uppercase_value):
        return "APS-C"
    else:
        return value

def clean_weight(value):
    value = value.replace(",",".")
    if("(" in value and ")" in value):
        value = value.replace(" ", "")
        pos_of_open_bracket = value.find("(")
        pos_of_close_bracket = value.find(")")
        if("kg" in value):
            value = value[pos_of_open_bracket + 1 : pos_of_close_bracket].replace("kg", "")
            float_value = float(value) * 1000
            int_value = int(float_value)
            return str(int_value) + "g"
        else:
            return value[pos_of_open_bracket + 1 : pos_of_close_bracket]
    elif("g/" in value):
        pos_of_dash = value.find("/")
        return value[:pos_of_dash]
    else:
        return value


def clean_size(value):
    value = value.replace("×", "x")
    if((not ("m" in value)) and (not ("in" in value))):
        return ""

    pos_first_unit = value.find("mm")
    pos_second_unit = value[pos_first_unit + 2:].find("mm") + pos_first_unit + 2
    if(value[pos_second_unit + 2:].find("mm") >= 0):
        value = value[:pos_second_unit + 2]
        first = value.split("x")[0]
        second = value.split("x")[1]
        first = first.replace("mm", "")
        return first + " x " + second


    value = value.replace(" m", "m")
    if("(" in value and ")" in value):
        pos_of_open_bracket = value.find("(")
        pos_of_close_bracket = value.find(")")
        pos_of_second_open_bracket = value.rfind("(")
        pos_of_second_close_bracket = value.rfind(")")
        if(pos_of_open_bracket == pos_of_second_open_bracket):
            return value[pos_of_open_bracket + 1 : pos_of_close_bracket]
        else:
            first_bracket = value[pos_of_open_bracket + 1: pos_of_close_bracket].replace("mm","")
            second_bracket = value[pos_of_second_open_bracket + 1: pos_of_second_close_bracket]
            return first_bracket + " x " + second_bracket

    elif("/" in value):
        value = value.replace("mm x", " x")
        pos_of_dash = value.find("/")
        return value[:pos_of_dash]
    else:
        return value
    