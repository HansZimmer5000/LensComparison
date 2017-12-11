import unittest
from webcrawler.tests.testdata import generalexamples
from webcrawler.lenses.crawledlenses import CrawledLenses

class CrawledLensesTestsuite(unittest.TestCase):

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        self.__class__.CRAWLED_LENSES = CrawledLenses("test_db", "crawled_lenses_testsuite_coll")

        self.__class__.CRAWLED_LENS1_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS1_LENS_DICT
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT_LENS_DICT
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS1_OLD_MOUNT_LENS_DICT
        self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS1_NEW_MOUNT_LENS_DICT

        self.__class__.CRAWLED_LENS2_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS2_LENS_DICT
        self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT
        
        self.__class__.CRAWLED_LENS3_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS3_LENS_DICT

        self.__class__.CRAWLED_LENS2_NAME = generalexamples.TESTDATA_CRAWLED_LENS2_NAME

        self.__class__.ALL_CRAWLED_LENSES_WITH_MISSING_INFO_LENS_DICTS = generalexamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_MISSING_INFO_LENS_DICTS
        self.__class__.ALL_CRAWLED_LENSES_WITH_FULL_INFO_LENS_DICTS = generalexamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_FULL_INFO_LENS_DICTS

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        self.__class__.CRAWLED_LENSES.mongo_access.delete_all_lenses()
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_neg_lens_data_exists(self):
        self.assertFalse(self.__class__.CRAWLED_LENS2_NAME in self.__class__.CRAWLED_LENSES.lenses)

    def test_pos_lens_data_exists(self):
        self.__class__.CRAWLED_LENSES.new_lens_dict(self.__class__.CRAWLED_LENS2_LENS_DICT)
        self.assertTrue(self.__class__.CRAWLED_LENS2_NAME in self.__class__.CRAWLED_LENSES.lenses)

    def test_pos_lens_is_new(self):
        lens2_dict = self.__class__.CRAWLED_LENS2_LENS_DICT.copy()
        length_before = len(self.__class__.CRAWLED_LENSES.lenses)
        self.__class__.CRAWLED_LENSES.new_lens_dict(lens2_dict)
        length_after = len(self.__class__.CRAWLED_LENSES.lenses)
        added_lens = self.__class__.CRAWLED_LENSES.lenses[self.__class__.CRAWLED_LENS2_NAME]
        self.assertEqual(self.__class__.CRAWLED_LENS2_LENS_DICT, added_lens.lens_dict)

    def test_pos_lens_has_new_data(self):
        lens2_dict = self.__class__.CRAWLED_LENS2_LENS_DICT.copy()
        lens2_without_sensor_dict = self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT.copy()
        self.__class__.CRAWLED_LENSES.new_lens_dict(lens2_without_sensor_dict)
        length_before = len(self.__class__.CRAWLED_LENSES.lenses)
        self.__class__.CRAWLED_LENSES.new_lens_dict(lens2_dict)
        length_after = len(self.__class__.CRAWLED_LENSES.lenses)
        updated_lens = self.__class__.CRAWLED_LENSES.lenses[self.__class__.CRAWLED_LENS2_NAME]
        self.assertEqual(self.__class__.CRAWLED_LENS2_LENS_DICT, updated_lens.lens_dict)