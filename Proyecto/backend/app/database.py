'''Singleton class for the database connection'''

from pymongo import MongoClient



# MongoDB connection URI
MONGO_URI = "mongodb://localhost:27017/"
# MONGO_URI = "mongodb+srv://Administrador:PttuZVjgwQeAckM5@cluster0.kqodv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

class Database:
    '''Singleton class for the database connection'''
    _instance = None
    client = None
    db = None

    def __new__(cls):
        '''Creates the singleton instance'''
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)   # Creates the instance
            cls._instance.client = MongoClient(MONGO_URI)   # Connects to the database
            cls._instance.db = cls._instance.client.test # "test" is my local database
            # remote db
            # cls._instance.db = cls._instance.client["Base_de_datos_seguimiento_proyectos"]

        return cls._instance

    def __del__(self):
        '''Closes the connection'''
        self.client.close()
        self._instance = None
        self.client = None
        self.db = None


def get_db():
    '''Method that obtains the database instance from anywhere within the system'''
    return Database().db
