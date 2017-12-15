# Testsuite for CsvIntoRawData.py
# Decided just to test the functions with a return value.

import unittest
from webcrawler.tests.testdata import plexamples
from webcrawler.crawler.itempipelines.plitempipeline import PlItemPipeline

class PlItemPipelineTestsuite(unittest.TestCase):

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        self.ghitempipeline = PlItemPipeline()
        
        self.TESTDATA_DICT_WITHOUT_VALUES = plexamples.TESTDATA_DICT_WITHOUT_VALUES
        self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1 = plexamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1
        self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING2 = plexamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING2
        self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING3 = plexamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING3
        self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1 = plexamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1
        self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1 = plexamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1

        self.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1 = plexamples.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1
        self.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES = plexamples.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES

        self.TESTDATA_DICT_WITH_EVERYTHING1 = plexamples.TESTDATA_DICT_WITH_EVERYTHING1
        self.TESTDATA_DICT_WITH_EVERYTHING2 = plexamples.TESTDATA_DICT_WITH_EVERYTHING2
        self.TESTDATA_DICT_WITH_EVERYTHING3 = plexamples.TESTDATA_DICT_WITH_EVERYTHING3
        self.TESTDATA_DICT_WITH_MISSING_INFO1 = plexamples.TESTDATA_DICT_WITH_MISSING_INFO1
        self.TESTDATA_DICT_WITHOUT_PRODIMG1 = plexamples.TESTDATA_DICT_WITHOUT_PRODIMG1

        self.TESTDATA_TITLE_RAW1 = plexamples.TESTDATA_TITLE_RAW1
        self.TESTDATA_TITLE_CLEAR1 = plexamples.TESTDATA_TITLE_CLEAR1

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_get_all_attributes_with_everything1(self):
        
        given_raw_site = self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1
        given_proddesc = self.ghitempipeline.get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = self.ghitempipeline.get_prodimg_from_raw_site(given_raw_site)

        result_dict = self.ghitempipeline.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.TESTDATA_DICT_WITH_EVERYTHING1,result_dict)

    def test_pos_get_all_attributes_with_everything2(self):
        
        given_raw_site = self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING2
        given_proddesc = self.ghitempipeline.get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = self.ghitempipeline.get_prodimg_from_raw_site(given_raw_site)
        
        result_dict = self.ghitempipeline.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.TESTDATA_DICT_WITH_EVERYTHING2,result_dict)

    def test_pos_get_all_attributes_with_everything3(self):
        
        given_raw_site = self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING3
        given_proddesc = self.ghitempipeline.get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = self.ghitempipeline.get_prodimg_from_raw_site(given_raw_site)
        
        result_dict = self.ghitempipeline.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.TESTDATA_DICT_WITH_EVERYTHING3,result_dict)

    def test_pos_get_all_attributes_with_missing_info1(self):
        given_raw_site = self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1
        given_proddesc = self.ghitempipeline.get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = self.ghitempipeline.get_prodimg_from_raw_site(given_raw_site)

        result_dict = self.ghitempipeline.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.TESTDATA_DICT_WITH_MISSING_INFO1, result_dict)

    def test_pos_get_all_attributes_without_prodimg(self):

        given_raw_site = self.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1
        given_proddesc = self.ghitempipeline.get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = self.ghitempipeline.get_prodimg_from_raw_site(given_raw_site)

        result_dict = self.ghitempipeline.get_all_attributes(given_proddesc,given_prodimg)

        self.assertEqual(self.TESTDATA_DICT_WITHOUT_PRODIMG1,result_dict)

    def test_pos_get_all_attributes_no_input(self):
        given_proddesc = ""
        given_prodimgAndLinksText = ""

        result_dict = self.ghitempipeline.get_all_attributes(given_proddesc,given_prodimgAndLinksText)
        self.assertEqual(self.TESTDATA_DICT_WITHOUT_VALUES,result_dict)

    def test_pos_convert_dict_to_csv_value_string_with_everything(self):
        result_string = self.ghitempipeline.convert_dict_to_csv_value_string(self.TESTDATA_DICT_WITH_EVERYTHING1)
        self.assertEqual(self.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1,result_string)

    def test_pos_convert_dict_to_csv_value_string_no_input(self):
        result_string = self.ghitempipeline.convert_dict_to_csv_value_string(self.TESTDATA_DICT_WITHOUT_VALUES)
        self.assertEqual(self.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES,result_string)

    def test_pos_get_lens_name_from_title(self):
        result_string = self.ghitempipeline.get_lens_name_from_title(self.TESTDATA_TITLE_RAW1)
        self.assertEqual(self.TESTDATA_TITLE_CLEAR1,result_string)
