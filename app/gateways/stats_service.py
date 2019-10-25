import threading
import traceback
import pika
import app.utils.config as config
import services.total_sells as service
import app.utils.json_serializer as json



##Se pondra las estadisticas calculadas en la cola de Stats de RabbitMQ, este evento es llamado cuando entra una order en estado Placed y se haya calculado las estadistica.

def sendStats():

    EXCHANGE = "stats"
    QUEUE = "stats"
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config.get_rabbit_server_url())
    )
    channel = connection.channel()

    channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

    channel.queue_declare(queue = QUEUE)

    channel.queue_bind(exchange=EXCHANGE, queue=QUEUE)

    message = service.sendRabbit()

    channel.basic_publish(exchange =EXCHANGE, routing_key=QUEUE, body=json.dic_to_json(message))
    
    print("MENSAJE ENVIADO a la cola de stats")

    connection.close()

