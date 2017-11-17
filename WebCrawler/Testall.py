# Starts all testsuite available.

from CsvIntoRawDataTestsuite import CsvIntoRawDataTestSuite
from GhAdapterTestsuite import GhAdapterTestsuite
from CrawledLensTestsuite import CrawledLensTestsuite
import unittest

if __name__ == '__main__':
    testClassesToRun = [
        GhAdapterTestsuite, 
        CsvIntoRawDataTestSuite,
        CrawledLensTestsuite
    ]

    unittestLoader = unittest.TestLoader()

    AllTestSuites = [] 
    for test_class in testClassesToRun:
        suite = unittestLoader.loadTestsFromTestCase(test_class)
        AllTestSuites.append(suite)

    UnifiedSuite = unittest.TestSuite(AllTestSuites)

    testRunner = unittest.TextTestRunner()
    testRunner.run(UnifiedSuite)
