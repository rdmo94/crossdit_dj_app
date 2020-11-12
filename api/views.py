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
    client = MongoClient('mongodb+srv://crossdit:crossdit@cluster0.yqnrt.mongodb.net/crossdit?retryWrites=true&w=majority')
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