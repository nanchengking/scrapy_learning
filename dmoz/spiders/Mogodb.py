#coding=utf-8
import pymongo
import datetime
from pymongo import MongoClient
client=MongoClient()
db = client.test
collection=db.test_collection
post={"author":"Mike","id":001,"date":datetime.datetime.utcnow()}
posts=db.posts
post_id=posts.insert_one(post).inserted_id
print post_id
print db.collection_names(include_system_collections=False)
