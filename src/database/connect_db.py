from pymongo import MongoClient

def connect():
    db = None
    try:
        client = MongoClient()
        db = client.pages_analysis
    except Exception as e:
        print('Connection ERROR: ' + str(e))
    return db