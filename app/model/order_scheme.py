# coding=utf_8
import app.gateways.mongo_service as mongo
import datetime
import numbers


def saveOrder(event):


    db = mongo.conectar_bd()
    collection = db.orders
    collection.insert(createOrder(event))



    
def createOrder(order):

    return {
        "orderId" : order["message"]["orderId"],
        "articles" : order["message"]["articles"]
    }

def loadOrders():
    db = mongo.conectar_bd()
    collection = db.orders
    return collection.find({})