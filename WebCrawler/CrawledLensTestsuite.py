import unittest
import GeneralExamples
from CrawledLens import CrawledLens

class CrawledLensTestsuite(unittest.TestCase):

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        
        self.__class__.CRAWLED_LENS1_LENS_DICT = GeneralExamples.TESTDATA_CRAWLED_LENS1_LENS_DICT
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT_LENS_DICT = GeneralExamples.TESTDATA_CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT_LENS_DICT
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT_LENS_DICT = GeneralExamples.TESTDATA_CRAWLED_LENS1_OLD_MOUNT_LENS_DICT
        self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT_LENS_DICT = GeneralExamples.TESTDATA_CRAWLED_LENS1_NEW_MOUNT_LENS_DICT

        self.__class__.CRAWLED_LENS2_LENS_DICT = GeneralExamples.TESTDATA_CRAWLED_LENS2_LENS_DICT
        self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT = GeneralExamples.TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT
        
        self.__class__.CRAWLED_LENS3_LENS_DICT = GeneralExamples.TESTDATA_CRAWLED_LENS3_LENS_DICT

        self.__class__.ALL_CRAWLED_LENSES_WITH_MISSING_INFO_LENS_DICTS = GeneralExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_MISSING_INFO_LENS_DICTS
        self.__class__.ALL_CRAWLED_LENSES_WITH_FULL_INFO_LENS_DICTS = GeneralExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_FULL_INFO_LENS_DICTS


        self.__class__.CRAWLED_LENS1 = CrawledLens(self.__class__.CRAWLED_LENS1_LENS_DICT)
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT = CrawledLens(self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT_LENS_DICT)
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT = CrawledLens(self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT_LENS_DICT)
        
        self.__class__.CRAWLED_LENS2 = CrawledLens(self.__class__.CRAWLED_LENS2_LENS_DICT)
        
        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_lens_data_exists_update_mount_and_weight(self):
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT.update(self.__class__.CRAWLED_LENS1_LENS_DICT)
        self.assertTrue(self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT.equals(self.__class__.CRAWLED_LENS1))

    def test_pos_lens_data_exists_update_sensor(self):
        lens_to_be_updated = CrawledLens(self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT.copy())
        lens_to_be_updated.update(self.__class__.CRAWLED_LENS2_LENS_DICT)
        self.assertTrue(lens_to_be_updated.equals(self.__class__.CRAWLED_LENS2))

    def test_pos_lens_data_exists_update_but_nothing_new_to_add(self):
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT.update(self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT_LENS_DICT)
        self.assertTrue(self.__class__.CRAWLED_LENS1.equals(self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT))

    def test_pos_lens_data_exists_update_but_no_new_mount_to_add(self):
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT.update(self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT_LENS_DICT)
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT.update(self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT_LENS_DICT)
        self.assertTrue(self.__class__.CRAWLED_LENS1.equals(self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT))
