
import sys
import os
import time
from threading import Thread

current_dir = os.getcwd()
sys.path.append(current_dir + '')

from webcrawler.spiders import startcrawling
from webcrawler.tests import testall
from webcrawler.persistency.mongotocsv import MongoToCsv
from webcrawler.persistency import mongoservercontrol

def run_spiders():
    startcrawling.start_spider_within_python()

def run_tests():
    testall.run_all_tests()

def export_lenses_to_csv():
    MongoToCsv("lens_db").gather_integrate_export_all_lenses()

def __start_mongo_do_work_stop_mongo(function):
    mongo_thread = __start_mongo_server()
    time.sleep(3) #To make sure mongo_server is completly up and running.
    try:
        function()
    except KeyboardInterrupt:
        pass
    time.sleep(1) #To make sure function and all its function are really done.
    __stop_thread(mongo_thread)

def __start_mongo_server():
    mongo_server_thread = Thread(target = mongoservercontrol.start_mongo_server, daemon=False)
    mongo_server_thread.start()
    return mongo_server_thread

def __stop_thread(thread):
    os.system("taskkill /f /im mongod.exe")

if __name__ == "__main__": 
    user_input = sys.argv[1]
    if(user_input == "1"):
        __start_mongo_do_work_stop_mongo(run_tests)
    elif(user_input == "2"):
        __start_mongo_do_work_stop_mongo(run_spiders)
    elif(user_input == "3"):
        __start_mongo_do_work_stop_mongo(export_lenses_to_csv)
