
#Own Class since this could get very complicated.

class LensIntegration:

    def __init__(self, new_lenses):
        self.__default_lens = new_lenses.pop(0)
        self.__keys = self.__default_lens.keys()
        self.__new_lenses = new_lenses

    def integrate(self):
        #TODO: Find more ways to integrate properly.

        if(len(self.__new_lenses) != 0):
            for key in self.__keys:
                self.__set_new_value_if_existing_is_empty(key)

        result_lens = self.__default_lens
        return result_lens

    def __set_new_value_if_existing_is_empty(self, key):
        old_value = self.__default_lens[key]
        if(old_value == ""):
            self.__set_first_not_empty_new_value(key)

    def __set_first_not_empty_new_value(self, key):
        for new_lens in self.__new_lenses:
            was_set = self.__new_not_empty_data_was_set(new_lens, key)
            if(was_set):
                break

    def __new_not_empty_data_was_set(self, new_lens, key):
        value = new_lens[key]
        if(value != ""):
            self.__default_lens[key] = value
            return True
        return False
