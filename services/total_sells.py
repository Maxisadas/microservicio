import app.model.order_scheme as orderScheme

"""
Esta funcion guarda los articulos vendido de las ordenes que nos entrega la cola de Rabbitmq, se hace verificaciones de si el producto del vendedor, ya esta en la base de datos , 
entoneces se le suma y se actualiza. En caso contrario, se crear el nuevo articulo vendido.
"""
def saveOrders(event):

    list_articles_bd = orderScheme.loadAllArticles()
    if list_articles_bd.count() != 0:
        for article in event["message"]["articles"]:
            id_article = article["articleId"]

            for article_bd in orderScheme.loadAllArticles():

                if id_article == article_bd["articleId"]:

                    article_bd["quantity"] = article_bd["quantity"] + article["quantity"]
                    orderScheme.updateArticles(article_bd)
    else:
        for article in event["message"]["articles"]:
            orderScheme.saveArticles(article)




## FUNCION DEL CASO DE USO:ESTADISTICA DE VENTAS ##########
def total_sells():
    """
    ENTREGAMOS EL TOTAL DE ARTICULOS VENDIDOS.

    @api {get} /v1/stats/sells Generar estadistica de ventas
    @apiName Consultar total de ventas
    @apiGroup Sells

    @apiUse AuthHeader



    @apiSuccessExample {json} Respuesta
    HTTP/1.1 200 OK
    {
        {
        "articles_more_sold": [{
            "id": "articleId",
            "quantity": {quantity}
            }], ...  
        "totals_sell={int}"    
        }
        

    }

    @apiUse Errors

    """
    total_articles = 0
    total_sells = []
    for article in orderScheme.loadAllArticles():
        total_articles += article["quantity"]
        total_sells.append(article)
    return {
        "articles_more_sold" : total_sells,
        "totals_sell": total_articles
        
    }


