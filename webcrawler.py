import sys
import os

current_dir = os.getcwd()
sys.path.append(current_dir + '')

from webcrawler.spiders import startcrawling
from webcrawler.tests import testall

if __name__ == "__main__": 
    testall.run_all_tests()