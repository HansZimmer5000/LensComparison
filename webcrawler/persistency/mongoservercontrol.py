import os

DB_PATH = "C:/Users/Michael/AppData/Local/MongoDB/LensComparison"
MONGO_BIN = '"C:/Program Files/MongoDB/Server/3.4/bin/mongod"'
FUNCTION = "--dbpath"

def start_mongo_server():
    try:
        os.system(MONGO_BIN + " " + FUNCTION + " " + DB_PATH)
    except KeyboardInterrupt:
        print("Aborted due to User Cancel Command.")

if __name__ == "__main__":
    start_mongo_server()