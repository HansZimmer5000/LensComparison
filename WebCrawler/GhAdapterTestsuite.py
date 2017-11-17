# Testsuite for CsvIntoRawData.py
# Decided just to test the functions with a return value.

from CsvIntoRawData import get_prodimg_from_raw_site
from CsvIntoRawData import get_proddesc_from_raw_site
import GhExamples
import GhAdapter
import unittest
import os

class GhAdapterTestsuite(unittest.TestCase):
    
    #\\\\\\\\\\\\
    # Class Variables
    #////////////

    TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1 = ""
    TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING2 = ""
    TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING3 = ""
    TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1 = ""
    TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1 = ""

    TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1 = ""
    TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES = ""

    TESTDATA_DICT_WITHOUT_VALUES = {}
    TESTDATA_DICT_WITH_EVERYTHING1 = {}
    TESTDATA_DICT_WITH_EVERYTHING2 = {}
    TESTDATA_DICT_WITH_EVERYTHING3 = {}
    TESTDATA_DICT_WITH_MISSING_INFO1 = {}
    TESTDATA_DICT_WITHOUT_PRODIMG1 = {}

    TESTDATA_TITLE_RAW1 = ""
    TESTDATA_TITLE_CLEAR1 = ""

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        
        self.__class__.TESTDATA_DICT_WITHOUT_VALUES = GhExamples.TESTDATA_DICT_WITHOUT_VALUES
        self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1 = GhExamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1
        self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING2 = GhExamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING2
        self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING3 = GhExamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING3
        self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1 = GhExamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1
        self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1 = GhExamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1

        self.__class__.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1 = GhExamples.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1
        self.__class__.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES = GhExamples.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES

        self.__class__.TESTDATA_DICT_WITH_EVERYTHING1 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING1
        self.__class__.TESTDATA_DICT_WITH_EVERYTHING2 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING2
        self.__class__.TESTDATA_DICT_WITH_EVERYTHING3 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING3
        self.__class__.TESTDATA_DICT_WITH_MISSING_INFO1 = GhExamples.TESTDATA_DICT_WITH_MISSING_INFO1
        self.__class__.TESTDATA_DICT_WITHOUT_PRODIMG1 = GhExamples.TESTDATA_DICT_WITHOUT_PRODIMG1

        self.__class__.TESTDATA_TITLE_RAW1 = GhExamples.TESTDATA_TITLE_RAW1
        self.__class__.TESTDATA_TITLE_CLEAR1 = GhExamples.TESTDATA_TITLE_CLEAR1

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_get_all_attributes_with_everything1(self):
        
        given_raw_site = self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)

        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING1,result_dict)

    def test_pos_get_all_attributes_with_everything2(self):
        
        given_raw_site = self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING2
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)
        
        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING2,result_dict)

    def test_pos_get_all_attributes_with_everything3(self):
        
        given_raw_site = self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING3
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)
        
        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING3,result_dict)

    def test_pos_get_all_attributes_with_missing_info1(self):
        given_raw_site = self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)

        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_MISSING_INFO1, result_dict)

    def test_pos_get_all_attributes_without_prodimg(self):

        given_raw_site = self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)

        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITHOUT_PRODIMG1,result_dict)

    def test_pos_get_all_attributes_no_input(self):
        given_proddesc = ""
        given_prodimgAndLinksText = ""

        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimgAndLinksText)
        self.assertEqual(self.__class__.TESTDATA_DICT_WITHOUT_VALUES,result_dict)

    def test_pos_convert_dict_to_csv_value_string_with_everything(self):
        result_string = GhAdapter.convert_dict_to_csv_value_string(self.__class__.TESTDATA_DICT_WITH_EVERYTHING1)
        self.assertEqual(self.__class__.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1,result_string)

    def test_pos_convert_dict_to_csv_value_string_no_input(self):
        result_string = GhAdapter.convert_dict_to_csv_value_string(self.__class__.TESTDATA_DICT_WITHOUT_VALUES)
        self.assertEqual(self.__class__.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES,result_string)

    def test_pos_get_lens_name_from_title(self):
        result_string = GhAdapter.get_lens_name_from_title(self.__class__.TESTDATA_TITLE_RAW1)
        self.assertEqual(self.__class__.TESTDATA_TITLE_CLEAR1,result_string)

 # -- End of GhAdapterTestsuite Class

if __name__ == "__main__":
    unittest.main()

