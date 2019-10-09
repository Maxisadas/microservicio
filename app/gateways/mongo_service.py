def obtener_bd():
	host = "localhost"
	puerto = "27017"
	base_de_datos = "stats"
	cliente = MongoClient("mongodb://{}:{}@{}:{}".format("","",host,puerto))
	return cliente[base_de_datos]