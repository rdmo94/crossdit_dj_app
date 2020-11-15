from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId

@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)


@api_view(["GET"])
def getReading(request):
    # client = MongoClient('mongodb+srv://crossdit:crossdit@cluster0.yqnrt.mongodb.net/crossdit?retryWrites=true&w=majority&authSource=admin', connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1)
    client = MongoClient('mongodb://crossdit:crossdit@cluster0-shard-00-00.yqnrt.mongodb.net:27017,cluster0-shard-00-01.yqnrt.mongodb.net:27017,cluster0-shard-00-02.yqnrt.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-it1cv8-shard-0&authSource=admin&retryWrites=true&w=majority', connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1)
    db = client.crossdit
    collection = db.data
    result = collection.aggregate([{ "$sample" : { "size" : 1 } }])
    meterId = ObjectId()
    for doc in result:
        meterId = doc['_id']
    reading = collection.find_one({"_id" : meterId})
    print(reading)
    obj = { 
        "meterId" : reading['meterId'],
        "value" : reading['value'],
    }
    return JsonResponse(obj)