#coding=utf-8
import logging
from pymongo import MongoClient
class SaveData(object):
    ''' 用来存储数据的'''
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.taobao
        self.collection=self.db.shoes
    def save(self,data):
        post_id= self.collection.insert_one(data).inserted_id
        ''' 存完，拿一次已经存好的数据的id，证明已经存好'''
        logging.warning("===saveSuccessfull!=== id is "+post_id)
        
#print db.collection_names(include_system_collections=False)
#print collection.find()
#TODO：==king
