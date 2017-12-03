import os

DB_PATH = "C:/Users/Michael/AppData/Local/MongoDB/LensComparison"
MONGO_BIN = '"C:/Program Files/MongoDB/Server/3.4/bin/mongod"'
FUNCTION = "--dbpath"

try:
    os.system(MONGO_BIN + " " + FUNCTION + " " + DB_PATH)
except KeyboardInterrupt:
    print("Aborted due to User Cancel Command.")