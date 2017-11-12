# Testsuite for CsvIntoRawData.py
# Decided just to test the functions with a return value.

import GhExamples
import CsvIntoRawData
import unittest
import os

class CsvIntoRawDataTestSuite(unittest.TestCase):
    
    #\\\\\\\\\\\\
    # Class Variables
    #////////////

    PROJECT_MAIN_DIR = ""
    RAWRESPONSE_FILES_DIR = ""

    EMPTY_SET = set()
    RAWRESPONSE_FILES_FULLPATH_SET = set()

    RAWRESPONSE_TWELVE_SIXTY_ENTRY_1_DICT = {} #May just need for testing GhAdapterlater
    RAWRESPONSE_TWELVE_SIXTY_ENTRY_269_DICT = {} #May just need for testing GhAdapterlater


    RAWRESPONSE_TWELVE_SIXTY_FILE_FULLPATH = ""
    RAWRESPONSE_TWELVE_SIXTY_ENTRY_1 = ""
    RAWRESPONSE_TWELVE_SIXTY_ENTRY_1_DICT_VALUE_STRING = ""  #May just need for testing GhAdapterlater
    RAWRESPONSE_TWELVE_SIXTY_ENTRY_269 = ""

    RAWRESPONSE_TWELVE_SIXTY_FILE= ""

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        self.__class__.PROJECT_MAIN_DIR = 'C:\\Users\\Michael\\IdeaProjects\\LensComparison\\'
        self.__class__.RAWRESPONSE_FILES_DIR = self.__class__.PROJECT_MAIN_DIR + "WebCrawler\\"

        self.__class__.EMPTY_SET = set()
        self.__class__.RAWRESPONSE_FILES_FULLPATH_SET = {
            #Deleted due to not using it. self.__class__.RAWRESPONSE_FILES_DIR + "rawResponseData 1-4.csv",
            #Deleted due to not using it.self.__class__.RAWRESPONSE_FILES_DIR + "rawResponseData 5-7.csv",
            #Deleted due to not using it. self.__class__.RAWRESPONSE_FILES_DIR + "rawResponseData 8-11.csv",
            self.__class__.RAWRESPONSE_FILES_DIR + "rawResponseData 12 - 60.csv"
        }

        self.__class__.RAWRESPONSE_TWELVE_SIXTY_ENTRY_1_DICT = GhExamples.TESTDATA_DICT_RAWRESPONSE_TWELVE_SIXTY_ENTRY_1
        self.__class__.RAWRESPONSE_TWELVE_SIXTY_ENTRY_269_DICT = GhExamples.TESTDATA_DICT_RAWRESPONSE_TWELVE_SIXTY_ENTRY_269

        self.__class__.RAWRESPONSE_TWELVE_SIXTY_FILE_FULLPATH = self.__class__.RAWRESPONSE_FILES_DIR + "rawResponseData 12 - 60.csv"
        self.__class__.RAWRESPONSE_TWELVE_SIXTY_ENTRY_1 = GhExamples.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_RESPONSE_TWELVE_SIXTY_ENTRY_1
        self.__class__.RAWRESPONSE_TWELVE_SIXTY_ENTRY_1_DICT_VALUE_STRING = GhExamples.TESTDATA_DICT_VALUE_STRING_RAWRESPONSE_TWELVE_SIXTY_ENTRY_1
        self.__class__.RAWRESPONSE_TWELVE_SIXTY_ENTRY_269 = GhExamples.TESTDATA_RPODSITE_RAW_RESPONSE_TWELVE_SICTY_ENTRY_269

        self.__class__.RAWRESPONSE_TWELVE_SIXTY_FILE = open(self.__class__.RAWRESPONSE_TWELVE_SIXTY_FILE_FULLPATH,'r')

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        self.__class__.RAWRESPONSE_TWELVE_SIXTY_FILE.close()

        print("tearDown Done, next Line E (Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_get_all_raw_response_full_paths(self):
        #With

        #Then
        result = CsvIntoRawData.getall_raw_response_full_paths(self.__class__.RAWRESPONSE_FILES_DIR)
        resultAsSet = set(result)

        #Give        
        self.assertEqual(self.__class__.RAWRESPONSE_FILES_FULLPATH_SET,resultAsSet)

    def test_neg_get_all_raw_response_full_paths(self):
        #With

        #Then
        result = CsvIntoRawData.getall_raw_response_full_paths(self.__class__.PROJECT_MAIN_DIR)
        resultAsSet = set(result)

        #Give        
        self.assertEqual(self.__class__.EMPTY_SET,resultAsSet)
    
    def test_pos_without_prodimg_extract_data_from_raw_response_row(self):
        #With
        givenRow269 = self.__class__.RAWRESPONSE_TWELVE_SIXTY_FILE.read().split("\n")[268]

        #Then
        resultDict = CsvIntoRawData.extract_data_from_raw_response_row(givenRow269)

        #Give
        self.assertEqual(self.__class__.RAWRESPONSE_TWELVE_SIXTY_ENTRY_269_DICT, resultDict)

    def test_pos_full_info_extract_data_from_raw_response_row(self):
        #With
        givenRow1 = self.__class__.RAWRESPONSE_TWELVE_SIXTY_FILE.read().split("\n")[0]

        #Then
        resultDict = CsvIntoRawData.extract_data_from_raw_response_row(givenRow1)

        #Give
        self.maxDiff = None #Show us whole difference, if there is any.
        self.assertEqual(self.__class__.RAWRESPONSE_TWELVE_SIXTY_ENTRY_1_DICT,resultDict)

    def test_neg_extract_data_from_raw_response_row(self):
        #TODO: Really usefull? Doubt it.
        #With
        givenRow4 = self.__class__.RAWRESPONSE_TWELVE_SIXTY_FILE.read().split("\n")[3]

        #Then
        resultDict = CsvIntoRawData.extract_data_from_raw_response_row(givenRow4)

        #Give
        self.maxDiff = None #Show us whole difference, if there is any.
        self.assertNotEqual(self.__class__.RAWRESPONSE_TWELVE_SIXTY_ENTRY_269,resultDict)

# -- End of CsvIntoRawDataTestSuite Class

if __name__ == "__main__":
    unittest.main()



