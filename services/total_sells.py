

def total_sells():
	
	"""
    @api {get} /v1/stats/sells Generar estadistica de ventas
    @apiName Consultar total de ventas
    @apiGroup Sells

    @apiUse AuthHeader



    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
            {
                "articles_sells": [{
                    "id": "articleId",
                    "quantity": {quantity}
                }], ...  
            }

        }

    @apiUse Errors

    """
    

