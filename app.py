from flask import Flask
from flask_cors import CORS
from flask_restful import Api,Resource,abort
from pymongo import MongoClient
from bson import ObjectId
from bson import json_util
import json
import os
import random
import firebase_admin
from firebase_admin import credentials,auth


app = Flask(__name__)
cors = CORS(app,resources = {r"*":{"origins":"*"}})
api = Api(app)

mongoURL = os.environ.get('MONGO_URL')

client = MongoClient(mongoURL)
database = client["lexisDatabse"]


firebase_admin.initialize_app(credentials.Certificate(json.loads(os.environ.get('FIREBASE'))))

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
	
	def get(self,uid):

		try:
			user = auth.get_user(uid)
			if database.playerbest.count_documents({'_id':uid},limit = 1) == 0:
				database.playerbest.insert_one({'_id':uid,'Best_Scores':[{"Category_Id": "4",'Score':0},{"Category_Id": "5",'Score':0},{"Category_Id": "6",'Score':0},{"Category_Id": "7",'Score':0}]})

			bestScore = database.playerbest.find_one({'_id':uid})
			categories = database.categories.find_one({'_id':'categories'})

			for category in categories['Categories']:
				for score in bestScore['Best_Scores']:
					if score['Category_Id'] == category['Category_Id']:
						category["Best_Score"] = score["Score"]
						break
			categories.pop("_id")			
			return categories
						
		except Exception as e:
			abort(400,message = "Invalid uid")


class UpdateScore(Resource):
	
	def post(self,categoryId,uid,score):

		try:
			user = auth.get_user(uid)
			if database.playerbest.find_one_and_update({'_id':uid,'Best_Scores':{"$elemMatch":{"Category_Id":categoryId,'Score':{"$lt" : score}}}},{"$set":{"Best_Scores.$.Score": score }}) != None:
				if database.highscores.find_one_and_update({'_id':categoryId,'Top_Scorers':{"$elemMatch":{"User_Id":uid}}},{"$set":{"Top_Scorers.$.Score":score}}) != None:
					database.highscores.find_one_and_update({ '_id': categoryId },{'$push': {'Top_Scorers': {'$each': [],'$sort': { 'Score': -1 }}}})
				else:
					database.highscores.find_one_and_update({ '_id': categoryId },{'$push': {'Top_Scorers': {'$each': [{"User_Id":uid,"Name":user.display_name,"Score":score}],'$sort': { 'Score': -1 },'$slice': 3}}})

		except Exception as e:
			abort(400,message = "Invalid uid")

class HighScore(Resource):
	
	def get(self,categoryId):

		data = database.highscores.find_one({'_id':categoryId})
		if data != None:
			data.pop("_id")
			return data
		else:
			abort(404,message = "Data not found")	



api.add_resource(Words,"/words/<string:numberOfLetters>/<int:numberOfWords>")
api.add_resource(Categories,"/categories/<string:uid>")
api.add_resource(UpdateScore,"/updatescore/<string:categoryId>/<string:uid>/<int:score>")
api.add_resource(HighScore,"/highscore/<string:categoryId>")

if __name__ == "__main__": 
	app.run()	
