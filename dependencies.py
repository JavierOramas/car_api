import pymongo

def get_current_user():
    return True

def get_db():
    client = pymongo.MongoClient("localhost", 27017)
    try:
        return client.car_api_db
    except:
        # close client connection pymongo
        client.close()
def close_db(db):
    db.close()