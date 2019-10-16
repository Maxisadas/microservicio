from pymongo import MongoClient

def conectar_bd():		
	MONGO_URL = "mongodb://localhost"
	client = MongoClient(MONGO_URL)
	return	client['stats']

