import unittest
import GeneralExamples
from LensIntegration import LensIntegration

class LensIntegrationTestsuite(unittest.TestCase):


    #\\\\\\\\\\\\
    # setUp & tearDown
    #////////////

    def setUp(self):
        self.LENS2_DICT_WITHOUT_SENSOR = GeneralExamples.TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR_LENS_DICT
        self.LENS2_DICT = GeneralExamples.TESTDATA_CRAWLED_LENS2_LENS_DICT

        print("\n\nsetup Done\n" + self._testMethodName)
    #End of setUp

    def tearDown(self):
        
        print("tearDown Done, next Line E(Error), F(Failure) or .(Passed)")
    #End of tearDown

    #\\\\\\\\\\\\
    # Test cases
    #////////////

    def test_pos_integrate(self):
        lens_integration = LensIntegration([self.LENS2_DICT, self.LENS2_DICT_WITHOUT_SENSOR])
        integrated_lens = lens_integration.integrate()

        self.assertEqual(self.LENS2_DICT, integrated_lens)

    def test_pos_integrate_reversed(self):
        lens_integration = LensIntegration([self.LENS2_DICT_WITHOUT_SENSOR, self.LENS2_DICT])
        integrated_lens = lens_integration.integrate()

        self.assertEqual(self.LENS2_DICT, integrated_lens)
