#coding=utf-8
import pymongo
import datetime
from pymongo import MongoClient
class connectMogod:
	def _init_(self):
		self.client=MongoClient()
		self.db = client.test
		self.collection=db.test_collection
		#post={"author":"Mike","id":001,"date":datetime.datetime.utcnow()}
		#posts=db.posts
		#post_id=posts.insert_one(post).inserted_id
	def saveData(self,data):
		self.collection.insert_on(data)
		insert_id=posts.insert_one(post).inserted_id
		print "===id is:",insert_id
		
		
		

#print post_id
#print db.collection_names(include_system_collections=False)
