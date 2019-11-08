import app.model.order_scheme as orderScheme
from datetime import datetime


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
    ENTREGAMOS EL TOTAL DE ARTICULOS VENDIDOS, CON SUS RESPECTIVOS ARTICULOS Y CANTIDAD.

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
        "total_sells": "{int}"
        "lastStatic": "{date}"    
        }
        

    }

    @apiUse Errors

    """
    total_articles = 0
    total_sells = []
    now = datetime.now()
    for article in orderScheme.loadAllArticles():
        total_articles += article["quantity"]
        total_sells.append(article)
    return {
        "articles_more_sold" : total_sells,
        "totals_sell": total_articles,
        "lastStatic": str(now.day)+"/"+str(now.month)+"/"+str(now.year)+" "+str(now.hour)+":"+str(now.minute)
        
    }


def sendRabbit():
    """
    Envio las estadisticas de las ventas de los usuarios, a la cola de rabbit para que otro microservicio lo quiera consumir.

    Se que se es igual al metodo total_sells(), pero por ahi en un futuro algo se tendria que cambiar al enviar la informacion a la cola de rabbit,y por ende es mejor tener ambos metodos 
    por separados.

    @api {topic} stats/stats Envio de estadisticas

    @apiGroup RabbitMQ GET

    @apiDescription Envio de estadisticas de los vendedores a la cola de rabbit para que cualquier otro microservicio lo pueda consumir.

    @apiExample {json} Mensaje
    {
        {
        "articles_more_sold": [{
            "id": "articleId",
            "quantity": {quantity}
            }], ...  
        "total_sells={int}"
        "lastStatic": "{date}"    
        }
        

    }
    """
    total_articles = 0
    total_sells = []
    now = datetime.now()
    for article in orderScheme.loadAllArticles():
        total_articles += article["quantity"]
        total_sells.append(article)
    return {
        "articles_more_sold" : total_sells,
        "totals_sell": total_articles,
        "lastStatic": str(now.day)+"/"+str(now.month)+"/"+str(now.year)+" "+str(now.hour)+":"+str(now.minute)
        
    }