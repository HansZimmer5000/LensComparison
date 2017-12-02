import unittest
import GeneralExamples
from CrawledLenses import CrawledLenses

class CrawledLensesTestsuite(unittest.TestCase):

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        self.__class__.CRAWLED_LENSES = CrawledLenses("crawled_lenses_tellsuite_coll")

        self.__class__.CRAWLED_LENS1 = GeneralExamples.TESTDATA_CRAWLED_LENS1
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT = GeneralExamples.TESTDATA_CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT = GeneralExamples.TESTDATA_CRAWLED_LENS1_OLD_MOUNT
        self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT = GeneralExamples.TESTDATA_CRAWLED_LENS1_NEW_MOUNT

        self.__class__.CRAWLED_LENS2 = GeneralExamples.TESTDATA_CRAWLED_LENS2
        self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR = GeneralExamples.TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR
        
        self.__class__.CRAWLED_LENS3 = GeneralExamples.TESTDATA_CRAWLED_LENS3

        self.__class__.CRAWLED_LENS2_NAME = GeneralExamples.TESTDATA_CRAWLED_LENS2_NAME

        self.__class__.ALL_CRAWLED_LENSES_WITH_MISSING_INFO = GeneralExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_MISSING_INFO
        self.__class__.ALL_CRAWLED_LENSES_WITH_FULL_INFO = GeneralExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_FULL_INFO

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
        self.__class__.CRAWLED_LENSES.new_lens_dict(self.__class__.CRAWLED_LENS2.lens_dict)
        self.assertTrue(self.__class__.CRAWLED_LENS2_NAME in self.__class__.CRAWLED_LENSES.lenses)

    def test_pos_lens_is_new(self):
        pass

    def test_pos_lens_has_new_data(self):
        pass