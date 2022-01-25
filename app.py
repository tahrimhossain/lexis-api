from flask import Flask
from flask_cors import CORS
from flask_restful import Api,Resource,abort
from pymongo import MongoClient
from bson import ObjectId
from bson import json_util
import json
import os
import random

app = Flask(__name__)
cors = CORS(app,resources = {r"*":{"origins":"*"}})
api = Api(app)

mongoURL = os.environ.get('MONGO_URL')

client = MongoClient(mongoURL)
database = client["lexisDatabse"]

class Words(Resource):
	
	def get(self,numberOfLetters,numberOfWords):

		data = database.words.find_one({"_id":numberOfLetters})
		if data == None:
			abort(404,message = "Data not found")
		if numberOfWords > len(data["Data"]):
			abort(400,message = "Only "+str(len(data["Data"]))+" words can be returned at a time")

		data["Data"] = random.sample(data["Data"],numberOfWords)
		data.pop("_id")
		return data	

class Categories(Resource):
	
	def get(self):

		data = database.categories.find_one({"_id":"categories"})
		if data == None:
			abort(404,message = "Data not found")

		data.pop("_id")
		return data		



api.add_resource(Words,"/words/<string:numberOfLetters>/<int:numberOfWords>")
api.add_resource(Categories,"/categories")

if __name__ == "__main__": 
	app.run()	
