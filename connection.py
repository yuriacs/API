from pymongo import MongoClient

class Database:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 27017,
        db: str = "dbsigaa",
        username: str = None,
        password: str = None,
    ) -> None:
        self.CLIENT = MongoClient(
            host=host, port=port, username=username, password=password
        )
        self.DB = self.CLIENT[db]