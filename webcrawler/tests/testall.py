# Starts all testsuite available.

import unittest
from webcrawler.tests.ghitempipelinetestsuite import GhItemPipelineTestsuite
from webcrawler.tests.crawledlenstestsuite import CrawledLensTestsuite
from webcrawler.tests.crawledlensestestsuite import CrawledLensesTestsuite
from webcrawler.tests.mongoaccesstestsuite import MongoAccessTestsuite
from webcrawler.tests.lensintegrationtestsuite import LensIntegrationTestsuite

def run_all_tests():
    test_classes_to_run = [
        GhItemPipelineTestsuite,
        CrawledLensTestsuite,
        CrawledLensesTestsuite,
        MongoAccessTestsuite,
        LensIntegrationTestsuite
    ]

    unit_test_loader = unittest.TestLoader()

    all_test_suites = [] 
    for test_class in test_classes_to_run:
        suite = unit_test_loader.loadTestsFromTestCase(test_class)
        all_test_suites.append(suite)

    unified_suite = unittest.TestSuite(all_test_suites)

    test_runner = unittest.TextTestRunner()
    test_runner.run(unified_suite)

if __name__ == '__main__':
    run_all_tests()