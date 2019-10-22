import app.gateways.mongo_service as mongo

	##db = mongo.conectar_bd()
	##collection = db['orders']
	##collection.insert_one({"probando":123})

def total_sells():
	
	"""
    @api {get} /v1/stats/sells Generar estadistica de ventas
    @apiName Consultar total de ventas
    @apiGroup Sells

    @apiUse AuthHeader



    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
			"sells":[{
				"order_id": "id de la orden"
				"total": "El dinero total obtenido por la orden"

			}]
			"total_sales":"Dinero total obtenido de todas las ordenes"
        }

    @apiUse Errors

    """
    pass

