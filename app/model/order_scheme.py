# coding=utf_8
import app.gateways.mongo_service as mongo
import datetime
import numbers


def saveArticles(event):

    print("AGREGANDO ARTICULOS")
    db = mongo.conectar_bd()
    collection = db.articles
    collection.insert(createArticle(event))

def updateArticles(article):
    
    print("ACTUALIZANDO ARTICULOS")
  
    db = mongo.conectar_bd()
    collection = db.articles
    result = collection.find_and_modify({'articleId':article["articleId"]},{'$set': {"quantity": article["quantity"]}})
    print(result)


    
def createArticle(article):

    return {
        "articleId" : article["articleId"],
        "quantity" : article["quantity"]

    }


def loadAllArticles():
    db = mongo.conectar_bd()
    collection = db.articles
    return collection.find({})