from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["py_app_db"]
comments_collection = db["comments"]
comments_collection.drop()
def push_comm(username, comm):
    comment = {
        'username': username,
        'com_value': comm
    }
    comments_collection.insert_one(comment)


def get_comm_username(x):
    count = comments_collection.count_documents({})
    username = 'none'
    if count > 9:
        cursor = comments_collection.find({})
        username = cursor[count - x]['username']
    return username


def get_comm_value(x):
    count = comments_collection.count_documents({})
    com_value = 'none'
    if count > 9:
        cursor = comments_collection.find({})
        com_value = cursor[count - x]['com_value']
    return com_value
