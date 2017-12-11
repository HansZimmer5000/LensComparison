import sys
import os

current_dir = os.getcwd()
sys.path.append(current_dir + '')

from webcrawler.spiders import startcrawling
from webcrawler.tests import testall
from webcrawler.persistency.mongotocsv import MongoToCsv

def run_spiders():
    startcrawling.start_spider_within_python()

def run_tests():
    testall.run_all_tests()

def export_lenses_to_csv():
    MongoToCsv("lens_db").gather_integrate_export_all_lenses()

if __name__ == "__main__": 
    user_input = sys.argv[1]
    print(user_input)
    if(user_input == "1"):
        run_tests()
    elif(user_input == "2"):
        run_spiders()
    elif(user_input == "3"):
        export_lenses_to_csv()

