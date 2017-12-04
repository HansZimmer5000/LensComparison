
#Own Module since this could get very complicated.

def integrate(lenses):
    #TODO: Make better!
    default_lens = lenses.pop(0)
    keys = lenses[0].keys()

    if(len(lenses) != 0):
        for key in keys:
            value = default_lens[key]
            if(value == ""):
                    for lens in lenses:
                        value_other = lens[key]
                        if(value != ""):
                            default_lens[key] = value_other

    result_lens = default_lens
    return result_lens