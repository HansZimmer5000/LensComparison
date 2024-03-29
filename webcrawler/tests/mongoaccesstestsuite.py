
import unittest
from webcrawler.tests.testdata import generalexamples
from webcrawler.persistency.mongoaccess import MongoAccess

class MongoAccessTestsuite(unittest.TestCase):

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        self.__class__.MONGO_ACCESS = MongoAccess()
        self.__class__.MONGO_ACCESS.connect_to_db_and_collection("test_db", "mongoaccess_testsuite_coll")
        self.__class__.MONGO_ACCESS.delete_all_lenses()

        self.__class__.CRAWLED_LENS1_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS1_LENS_DICT
        self.__class__.CRAWLED_LENS2_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS2_LENS_DICT
        self.__class__.CRAWLED_LENS3_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS3_LENS_DICT

        self.__class__.CRAWLED_LENS2_NAME = generalexamples.TESTDATA_CRAWLED_LENS2_NAME
        self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT = generalexamples.TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT
        
        self.__class__.ALL_CRAWLED_LENSES_WITH_FULL_INFO = generalexamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_FULL_INFO_LENS_DICTS


        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        self.__class__.MONGO_ACCESS.delete_all_lenses()
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_add_and_find_lens(self):
        self.__class__.MONGO_ACCESS.add_lens(self.__class__.CRAWLED_LENS2_LENS_DICT)
        self.assertEqual(self.__class__.MONGO_ACCESS.get_lens_count(), 1)
        big_lens_dict = self.__class__.MONGO_ACCESS.find_all_lenses_into_one_dict()
        for key in big_lens_dict:
            lens_dict = big_lens_dict[key]

        self.assertEquals(self.__class__.CRAWLED_LENS2_LENS_DICT, lens_dict)

    def test_pos_update_lens(self):
        self.__class__.MONGO_ACCESS.add_lens(self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT)
        result = self.__class__.MONGO_ACCESS.update_lens(self.__class__.CRAWLED_LENS2_LENS_DICT)
        big_lens_dict = self.__class__.MONGO_ACCESS.find_all_lenses_into_one_dict()
        for key in big_lens_dict:
            lens_dict = big_lens_dict[key]

        self.assertEqual(self.__class__.CRAWLED_LENS2_LENS_DICT, lens_dict)

    def test_pos_get_lens_count(self):
        lens_count = self.__class__.MONGO_ACCESS.get_lens_count()
        self.assertEqual(lens_count, 0)

    def test_pos_delete_all_lenses(self):
        self.__class__.MONGO_ACCESS.delete_all_lenses()
        lens_count = self.__class__.MONGO_ACCESS.get_lens_count()
        self.assertEqual(lens_count, 0)