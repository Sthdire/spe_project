from pymongo import MongoClient


def push_comm(username, comm):
    client = MongoClient('localhost', 27017)
    db = client["py_app_db"]
    comments_collection = db["comments"]

    comment = {
        'username': username,
        'com_value': comm
    }

    comments_collection.insert_one(comment)
    print(db.comments_collection.find())
