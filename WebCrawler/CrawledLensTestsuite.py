import unittest
import GeneralExamples
from CrawledLens import CrawledLens

class CrawledLensTestsuite(unittest.TestCase):
    
    #\\\\\\\\\\\\
    # Class Variables
    #////////////

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        
        self.__class__.CRAWLED_LENS1 = GeneralExamples.TESTDATA_CRAWLED_LENS1
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT = GeneralExamples.TESTDATA_CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT = GeneralExamples.TESTDATA_CRAWLED_LENS1_OLD_MOUNT
        self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT = GeneralExamples.TESTDATA_CRAWLED_LENS1_NEW_MOUNT

        self.__class__.CRAWLED_LENS2 = GeneralExamples.TESTDATA_CRAWLED_LENS2
        self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR = GeneralExamples.TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR
        
        self.__class__.CRAWLED_LENS3 = GeneralExamples.TESTDATA_CRAWLED_LENS3

        self.__class__.ALL_CRAWLED_LENSES_WITH_MISSING_INFO = GeneralExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_MISSING_INFO
        self.__class__.ALL_CRAWLED_LENSES_WITH_FULL_INFO = GeneralExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_FULL_INFO

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_lens_data_exists_update_mount_and_weight(self):
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT.update(self.__class__.CRAWLED_LENS1.lens_dict)
        self.assertTrue(self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT.equals(self.__class__.CRAWLED_LENS1))

    def test_pos_lens_data_exists_update_sensor(self):
        lens_to_be_updated = CrawledLens(self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR.lens_dict.copy())
        lens_to_be_updated.update(self.__class__.CRAWLED_LENS2.lens_dict)
        self.assertTrue(lens_to_be_updated.equals(self.__class__.CRAWLED_LENS2))

    def test_pos_lens_data_exists_update_but_nothing_new_to_add(self):
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT.update(self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT.lens_dict)
        self.assertTrue(self.__class__.CRAWLED_LENS1.equals(self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT))

    def test_pos_lens_data_exists_update_but_no_new_mount_to_add(self):
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT.update(self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT.lens_dict)
        self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT.update(self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT.lens_dict)
        self.assertTrue(self.__class__.CRAWLED_LENS1.equals(self.__class__.CRAWLED_LENS1_WITH_OLD_MOUNT))
