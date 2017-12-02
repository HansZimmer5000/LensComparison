import unittest
import GeneralExamples
from MongoAccess import MongoAccess

class MongoAccessTestsuite(unittest.TestCase):

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        self.__class__.MONGO_ACCESS = MongoAccess("mongoaccess_testsuite_collection")
        self.__class__.MONGO_ACCESS.delete_all_lenses()

        self.__class__.CRAWLED_LENS1 = GeneralExamples.TESTDATA_CRAWLED_LENS1
        self.__class__.CRAWLED_LENS2 = GeneralExamples.TESTDATA_CRAWLED_LENS2
        self.__class__.CRAWLED_LENS3 = GeneralExamples.TESTDATA_CRAWLED_LENS3

        self.__class__.CRAWLED_LENS2_NAME = GeneralExamples.TESTDATA_CRAWLED_LENS2_NAME
        self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR = GeneralExamples.TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR
        
        self.__class__.ALL_CRAWLED_LENSES_WITH_FULL_INFO = GeneralExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_FULL_INFO

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
        self.__class__.MONGO_ACCESS.add_lens(self.__class__.CRAWLED_LENS2.lens_dict)
        self.assertEqual(self.__class__.MONGO_ACCESS.get_lens_count(), 1)
        lenses = self.__class__.MONGO_ACCESS.find_all_lenses()
        for key in lenses.keys():
            lens = lenses[key]

        self.assertTrue(self.__class__.CRAWLED_LENS2.equals(lens))

    def test_pos_update_lens(self):
        self.__class__.MONGO_ACCESS.add_lens(self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR.lens_dict)
        result = self.__class__.MONGO_ACCESS.update_lens(self.__class__.CRAWLED_LENS2.lens_dict)
        lenses = self.__class__.MONGO_ACCESS.find_all_lenses()
        for key in lenses.keys():
            lens = lenses[key]

        self.assertTrue(self.__class__.CRAWLED_LENS2.equals(lens))

    def test_pos_get_lens_count(self):
        lens_count = self.__class__.MONGO_ACCESS.get_lens_count()
        self.assertEqual(lens_count, 0)

    def test_pos_delete_all_lenses(self):
        self.__class__.MONGO_ACCESS.delete_all_lenses()
        lens_count = self.__class__.MONGO_ACCESS.get_lens_count()
        self.assertEqual(lens_count, 0)