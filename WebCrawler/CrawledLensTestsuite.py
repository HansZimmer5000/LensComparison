import unittest
import GhExamples
import DataKeys
from CrawledLens import CrawledLens

class CrawledLensTestsuite(unittest.TestCase):
    
    #\\\\\\\\\\\\
    # Class Variables
    #////////////

    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        
        self.__class__.CRAWLED_LENS1 = GhExamples.TESTDATA_CRAWLED_LENS1
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT = GhExamples.TESTDATA_CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT
        self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT = GhExamples.TESTDATA_CRAWLED_LENS1_NEW_MOUNT
        self.__class__.CRAWLED_LENS1_MOUNTS = GhExamples.TESTDATA_CRAWLED_LENS1_MOUNTS

        self.__class__.CRAWLED_LENS2 = GhExamples.TESTDATA_CRAWLED_LENS2
        self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR = GhExamples.TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR
        
        self.__class__.CRAWLED_LENS3 = GhExamples.TESTDATA_CRAWLED_LENS3

        self.__class__.ALL_CRAWLED_LENSES_WITH_MISSING_INFO = GhExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_MISSING_INFO
        self.__class__.ALL_CRAWLED_LENSES_WITH_FULL_INFO = GhExamples.TESTDATA_ALL_CRAWLED_LENSES_WITH_FULL_INFO

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_neg_lens_data_exists(self):
        self.assertFalse(self.__class__.CRAWLED_LENS3.lens_name in self.__class__.ALL_CRAWLED_LENSES_WITH_MISSING_INFO)

    def test_pos_lens_data_exists(self):
        self.assertTrue(self.__class__.CRAWLED_LENS1.lens_name in self.__class__.ALL_CRAWLED_LENSES_WITH_MISSING_INFO)

    def test_pos_lens_data_exists_update_mount_and_weight(self):
        self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT.update(self.__class__.CRAWLED_LENS1.lens_dict)

        self.assertTrue(self.__class__.CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT.equals(self.__class__.CRAWLED_LENS1))

    def test_pos_lens_data_exists_update_sensor(self):
        self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR.update(self.__class__.CRAWLED_LENS2.lens_dict)
        self.assertTrue(self.__class__.CRAWLED_LENS2_WITHOUT_SENSOR.equals(self.__class__.CRAWLED_LENS2))

    def test_pos_lens_data_exists_update_but_nothing_new_to_add(self):
        self.__class__.CRAWLED_LENS1.update(self.__class__.CRAWLED_LENS1_WITH_NEW_MOUNT.lens_dict)
        self.assertEqual(self.__class__.CRAWLED_LENS1_MOUNTS, \
                        self.__class__.CRAWLED_LENS1.lens_dict[DataKeys.key_mount_as_gh])
