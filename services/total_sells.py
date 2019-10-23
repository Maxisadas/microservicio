import app.model.order_scheme as orderScheme


def saveOrders(event):
	

    orderScheme.saveOrder(event)

## FUNCION DEL CASO DE USO:ESTADISTICA DE VENTAS ##########
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
    
    list_orders = orderScheme.loadOrders()
    totalSells = []
    for order in list_orders:
        for article in order["articles"]:
            


