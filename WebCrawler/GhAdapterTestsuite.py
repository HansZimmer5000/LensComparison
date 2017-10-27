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

    TESTDATA_PRODSITE_RAW_WITH_EVERYTHING1 = ""
    TESTDATA_PRODSITE_RAW_WITH_EVERYTHING2 = ""
    TESTDATA_PRODSITE_RAW_WITH_EVERYTHING3 = ""
    TESTDATA_PRODSITE_RAW_WITH_MISSING_INFO1 = ""
    TESTDATA_PRODSITE_RAW_WITHOUT_PRODIMG1 = ""

    TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1 = ""
    TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES = ""

    TESTDATA_DICT_WITHOUT_VALUES = {}
    TESTDATA_DICT_WITH_EVERYTHING1 = {}
    TESTDATA_DICT_WITH_EVERYTHING2 = {}
    TESTDATA_DICT_WITH_EVERYTHING3 = {}
    TESTDATA_DICT_WITH_MISSING_INFO1 = {}
    TESTDATA_DICT_RAW_WITHOUT_PRODIMG1 = {}

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        
        self.__class__.TESTDATA_DICT_WITHOUT_VALUES = GhExamples.TESTDATA_DICT_WITHOUT_VALUES
        self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING1 = GhExamples.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING1
        self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING2 = GhExamples.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING2
        self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING3 = GhExamples.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING3
        self.__class__.TESTDATA_PRODSITE_RAW_WITH_MISSING_INFO1 = GhExamples.TESTDATA_PRODSITE_RAW_WITH_MISSING_INFO1
        self.__class__.TESTDATA_PRODSITE_RAW_WITHOUT_PRODIMG1 = GhExamples.TESTDATA_PRODSITE_RAW_WITHOUT_PRODIMG1

        self.__class__.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1 = GhExamples.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1
        self.__class__.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES = GhExamples.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES

        self.__class__.TESTDATA_DICT_WITH_EVERYTHING1 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING1
        self.__class__.TESTDATA_DICT_WITH_EVERYTHING2 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING2
        self.__class__.TESTDATA_DICT_WITH_EVERYTHING3 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING3
        self.__class__.TESTDATA_DICT_WITH_MISSING_INFO1 = GhExamples.TESTDATA_DICT_WITH_MISSING_INFO1
        self.__class__.TESTDATA_DICT_RAW_WITHOUT_PRODIMG1 = GhExamples.TESTDATA_DICT_RAW_WITHOUT_PRODIMG1

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_get_all_attributes_with_everything1(self):
        
        given_raw_site = self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING1
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)

        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING1,result_dict)

    def test_pos_get_all_attributes_with_everything2(self):
        
        given_raw_site = self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING2
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)
        
        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING2,result_dict)

    def test_pos_get_all_attributes_with_everything3(self):
        
        given_raw_site = self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING3
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)
        
        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING3,result_dict)

    def test_pos_get_all_attributes_with_missing_info1(self):
        given_raw_site = self.__class__.TESTDATA_PRODSITE_RAW_WITH_MISSING_INFO1
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)

        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_MISSING_INFO1, result_dict)

    def test_pos_get_all_attributes_without_prodimg(self):

        given_raw_site = self.__class__.TESTDATA_PRODSITE_RAW_WITHOUT_PRODIMG1
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)

        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.__class__.TESTDATA_DICT_RAW_WITHOUT_PRODIMG1,result_dict)

    def test_neg_get_all_attributes_no_input(self):
        given_proddesc = ""
        given_prodimgAndLinksText = ""

        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimgAndLinksText)
        self.assertEqual(self.__class__.TESTDATA_DICT_WITHOUT_VALUES,result_dict)

    def test_pos_convert_dict_to_csv_value_string_with_everything(self):
        resultSring = GhAdapter.convert_dict_to_csv_value_string(self.__class__.TESTDATA_DICT_WITH_EVERYTHING1)
        self.assertEqual(self.__class__.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1,resultSring)

    def test_neg_convert_dict_to_csv_value_string_no_input(self):
        resultSring = GhAdapter.convert_dict_to_csv_value_string(self.__class__.TESTDATA_DICT_WITHOUT_VALUES)
        self.assertEqual(self.__class__.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES,resultSring)

 # -- End of GhAdapterTestsuite Class

if __name__ == "__main__":
    unittest.main()

