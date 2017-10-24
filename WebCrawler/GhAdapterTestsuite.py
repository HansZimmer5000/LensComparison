# Testsuite for CsvIntoRawData.py
# Decided just to test the functions with a return value.

from CsvIntoRawData import getProdImgFromRawSite
from CsvIntoRawData import getProdDescFromRawSite
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
    TESTDATA_PRODSITE_RAW_WITHOUT_PRODIMG1 = ""

    TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1 = ""
    TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES = ""

    TESTDATA_DICT_WITHOUT_VALUES = {}
    TESTDATA_DICT_WITH_EVERYTHING1 = {}
    TESTDATA_DICT_WITH_EVERYTHING2 = {}
    TESTDATA_DICT_WITH_EVERYTHING3 = {}
    TESTDATA_DICT_RAW_WITHOUT_PRODIMG1 = {}

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        
        self.__class__.TESTDATA_DICT_WITHOUT_VALUES = GhExamples.TESTDATA_DICT_WITHOUT_VALUES
        self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING1 = GhExamples.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING1
        self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING2 = GhExamples.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING2
        self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING3 = GhExamples.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING3
        self.__class__.TESTDATA_PRODSITE_RAW_WITHOUT_PRODIMG1 = GhExamples.TESTDATA_PRODSITE_RAW_WITHOUT_PRODIMG1

        self.__class__.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1 = GhExamples.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1
        self.__class__.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES = GhExamples.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES

        self.__class__.TESTDATA_DICT_WITH_EVERYTHING1 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING1
        self.__class__.TESTDATA_DICT_WITH_EVERYTHING2 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING2
        self.__class__.TESTDATA_DICT_WITH_EVERYTHING3 = GhExamples.TESTDATA_DICT_WITH_EVERYTHING3
        self.__class__.TESTDATA_DICT_RAW_WITHOUT_PRODIMG1 = GhExamples.TESTDATA_DICT_RAW_WITHOUT_PRODIMG1

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_getAllAttributes_without_prodimg(self):

        givenRawSite = self.__class__.TESTDATA_PRODSITE_RAW_WITHOUT_PRODIMG1
        givenProdDesc = getProdDescFromRawSite(givenRawSite)
        givenProdImg = getProdImgFromRawSite(givenRawSite)

        resultDict = GhAdapter.getAllAttributes(givenProdDesc,givenProdImg)

        self.assertEqual(self.__class__.TESTDATA_DICT_RAW_WITHOUT_PRODIMG1,resultDict)

    def test_pos_getAllAttributes_with_everything1(self):
        
        givenRawSite = self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING1
        givenProdDesc = getProdDescFromRawSite(givenRawSite)
        givenProdImg = getProdImgFromRawSite(givenRawSite)

        resultDict = GhAdapter.getAllAttributes(givenProdDesc,givenProdImg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING1,resultDict)

    def test_pos_getAllAttributes_with_everything2(self):
        
        givenRawSite = self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING2
        givenProdDesc = getProdDescFromRawSite(givenRawSite)
        givenProdImg = getProdImgFromRawSite(givenRawSite)
        
        resultDict = GhAdapter.getAllAttributes(givenProdDesc,givenProdImg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING2,resultDict)

    def test_pos_getAllAttributes_with_everything3(self):
        
        givenRawSite = self.__class__.TESTDATA_PRODSITE_RAW_WITH_EVERYTHING3
        givenProdDesc = getProdDescFromRawSite(givenRawSite)
        givenProdImg = getProdImgFromRawSite(givenRawSite)
        
        resultDict = GhAdapter.getAllAttributes(givenProdDesc,givenProdImg)

        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING3,resultDict)

    def test_neg_getAllAttributes_no_input(self):
        givenProdDesc = ""
        givenProdImgAndLinksText = ""

        resultDict = GhAdapter.getAllAttributes(givenProdDesc,givenProdImgAndLinksText)
        self.assertEqual(self.__class__.TESTDATA_DICT_WITHOUT_VALUES,resultDict)

    def test_pos_convertDictToCSVValueString_with_everything(self):
        resultSring = GhAdapter.convertDictToCSVValueString(self.__class__.TESTDATA_DICT_WITH_EVERYTHING1)
        self.assertEqual(self.__class__.TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1,resultSring)

    def test_neg_convertDictToCSVValueString_no_input(self):
        resultSring = GhAdapter.convertDictToCSVValueString(self.__class__.TESTDATA_DICT_WITHOUT_VALUES)
        self.assertEqual(self.__class__.TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES,resultSring)

 # -- End of GhAdapterTestsuite Class

if __name__ == "__main__":
    unittest.main()

