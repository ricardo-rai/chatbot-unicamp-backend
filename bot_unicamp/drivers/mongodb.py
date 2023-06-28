from pymongo import MongoClient


class MongoDatabaseContext:
    def __init__(self, db_uri=None, db_name=None, db_collection=None):
        self.db_uri = db_uri
        self.db_name = db_name
        self.db_collection = db_collection
        self.client = None
        self.db = None

    def add(self, value):
        self.db.insert_one(value)

        return value

    def get_all(self, **kwargs):
        values = self.db.find(kwargs, {"_id": False})

        return values

    def __enter__(self):
        self.client = MongoClient(self.db_uri)
        self.db = self.client[self.db_name][self.db_collection]

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
