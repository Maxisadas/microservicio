import threading
import traceback
import pika
import app.utils.config as config

##CONSUMIR COLA DE ORDER DE RABBITMQ PARA TRAER LAS ORDENES.
def init():
    initOrder()

def initOrder():
    orderConsumer = threading.Thread(target=listenOrder)
    orderConsumer.start()
def listenOrder():

    EXCHANGE = "stats"

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config.get_rabbit_server_url())
        )
        channel = connection.channel()

        channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue

        print(queue_name)

        def callback(ch, method, properties, body):
            event = json.body_to_dic(body.decode('utf-8'))
            print(event)
            return event
        


        print("RabbitMQ Order conectado")

        channel.basic_consume(queue_name, callback ,auto_ack=True)

        channel.start_consuming()
    except Exception as e:
        print("RabbitMQ Order desconectado, intentando reconectar en 10")
        print(format(e))
        threading.Timer(10.0, initOrder).start()