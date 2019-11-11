import threading
import traceback
import pika
import app.utils.config as config
import app.domain.services.total_sells as service
import app.utils.json_serializer as json
import app.gateways.stats_service as statsService


##CONSUMIR COLA DE ORDER DE RABBITMQ PARA TRAER LAS ORDENES Y ALMACENARLAS.
def init():
    initOrder()

def initOrder():
    orderConsumer = threading.Thread(target=listenOrder)
    orderConsumer.start()
def listenOrder():

    EXCHANGE = "stats"
    QUEUE = "order_placed"

    try:
        
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config.get_rabbit_server_url())
        )
        
        channel = connection.channel()

        channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

        result = channel.queue_declare(QUEUE)
        queue_name = result.method.queue

        channel.queue_bind(exchange=EXCHANGE, queue=queue_name)

        def callback(ch, method, properties, body):
            
            event = json.body_to_dic(body.decode('utf-8'))
            resp = service.saveOrders(event) ## Se recibe una orden y se calcula la estadistica y se guarda los articulos en la base de datos.
            statsService.sendStats()## Se envia a la cola de rabbit , luego de que se haya calculado la estadistica al recibir una orden.
        


        print("RabbitMQ Order conectado")

        channel.basic_consume(queue_name, callback ,auto_ack=True)

        channel.start_consuming()
    except Exception as e:
        print("RabbitMQ Order desconectado, intentando reconectar en 10")
        print(format(e))
        threading.Timer(10.0, initOrder).start()