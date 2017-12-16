
from webcrawler.persistency.plrawdatacleaner import clean_dict
from webcrawler.tests.testdata import plexamples
import unittest

class PlRawDataCleanerTestsuite(unittest.TestCase):

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):

        self.raw_dict1 = plexamples.TESTDATA_RAW_DICT_1
        self.raw_dict2 = plexamples.TESTDATA_RAW_DICT_2
        self.raw_dict3 = plexamples.TESTDATA_RAW_DICT_3
        self.raw_dict4 = plexamples.TESTDATA_RAW_DICT_4
        self.raw_dict5 = plexamples.TESTDATA_RAW_DICT_5
        self.raw_dict6 = plexamples.TESTDATA_RAW_DICT_6
        self.raw_dict7 = plexamples.TESTDATA_RAW_DICT_7
        self.raw_dict8 = plexamples.TESTDATA_RAW_DICT_8
        self.raw_dict9 = plexamples.TESTDATA_RAW_DICT_9
        self.raw_dict10 = plexamples.TESTDATA_RAW_DICT_10


        self.clean_dict1 = plexamples.TESTDATA_CLEAN_DICT_1
        self.clean_dict2 = plexamples.TESTDATA_CLEAN_DICT_2
        self.clean_dict3 = plexamples.TESTDATA_CLEAN_DICT_3
        self.clean_dict4 = plexamples.TESTDATA_CLEAN_DICT_4
        self.clean_dict5 = plexamples.TESTDATA_CLEAN_DICT_5
        self.clean_dict6 = plexamples.TESTDATA_CLEAN_DICT_6
        self.clean_dict7 = plexamples.TESTDATA_CLEAN_DICT_7
        self.clean_dict8 = plexamples.TESTDATA_CLEAN_DICT_8
        self.clean_dict9 = plexamples.TESTDATA_CLEAN_DICT_9
        self.clean_dict10 = plexamples.TESTDATA_CLEAN_DICT_10

        print("\n\nsetup Done\n" + self._testMethodName)

    def tearDown(self):    
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_dict_1(self):
        self.assertEqual(self.clean_dict1, clean_dict(self.raw_dict1))
    def test_dict_2(self):
        self.assertEqual(self.clean_dict2, clean_dict(self.raw_dict2))
    def test_dict_3(self):
        self.assertEqual(self.clean_dict3, clean_dict(self.raw_dict3))
    def test_dict_4(self):
        self.assertEqual(self.clean_dict4, clean_dict(self.raw_dict4))
    def test_dict_5(self):
        self.assertEqual(self.clean_dict5, clean_dict(self.raw_dict5))
    def test_dict_6(self):
        self.assertEqual(self.clean_dict6, clean_dict(self.raw_dict6))
    def test_dict_7(self):
        self.assertEqual(self.clean_dict7, clean_dict(self.raw_dict7))
    def test_dict_8(self):
        self.assertEqual(self.clean_dict8, clean_dict(self.raw_dict8))
    def test_dict_9(self):
        self.assertEqual(self.clean_dict9, clean_dict(self.raw_dict9))
    def test_dict_10(self):
        self.assertEqual(self.clean_dict10, clean_dict(self.raw_dict10))