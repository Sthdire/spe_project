from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["py_app_db"]
comments_collection = db["comments"]

cursor = comments_collection.find({})
count = comments_collection.count_documents({})


def push_comm(username, comm):
    comment = {
        'username': username,
        'com_value': comm
    }
    comments_collection.insert_one(comment)


def get_comm_username(x):
    username = cursor[count - x]['username']
    return username


def get_comm_value(x):
    com_value = cursor[count - x]['com_value']
    return com_value
