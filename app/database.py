
from pymongo import MongoClient

client = None
db = None
book_collection = None


def connect_to_mongo():
    global client, db, book_collection
    client = MongoClient('mongodb://localhost:27017/')
    db = client.Bookstore  # Replace with your actual database name
    book_collection = db.Book  # Replace with your actual collection name

def close_mongo_connection():
    global client
    if client:
        client.close()
