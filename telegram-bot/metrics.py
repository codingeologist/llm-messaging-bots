import os
import pymongo

class Metrics:

    def __init__(self) -> None:
        
        env = os.getenv(key="ENV")
        username = os.getenv(key="USERNAME")
        password = os.getenv(key="PASSWORD")
        host = os.getenv(key="MONGO_HOST")
        db_name = os.getenv(key="DB_NAME")

        self.deveurl = f"mongodb://localhost:27017/?retryWrites=true&w=majority&appName={db_name}"
        self.produrl = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority&appName={db_name}"

        if env == "dev":
            self.client = pymongo.MongoClient(self.deveurl)
        elif env == "prod":
            self.client = pymongo.MongoClient(self.produrl)
        self.db = self.client["metrics-data"]
    

    def save_metric(self, collection: str, document: dict) -> None:
        """
        save metric data to mongo collection
        """

        try:
            coll = self.db[collection]
            coll.insert_one(document)
        except Exception as ex:
            print(f"Error saving metric data: {ex}")
            print(f"metric data:\n{document}")