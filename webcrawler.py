import sys
import os

current_dir = os.getcwd()
sys.path.append(current_dir + '')

from webcrawler.spiders import startcrawling
from webcrawler.tests import testall
from webcrawler.persistency.mongotocsv import MongoToCsv

if __name__ == "__main__": 
    #testall.run_all_tests()
    #startcrawling.start_spider_within_python()
    MongoToCsv("lens_db").gather_integrate_export_all_lenses()
