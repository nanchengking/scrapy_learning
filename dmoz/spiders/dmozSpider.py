#coding=utf-8
from scrapy.contrib.loader import ItemLoader
import logging
from dmoz.items import FirstPageItem
from Mogodb import  connectMogod
import scrapy
import re
class w3cSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains = ["taobao.com"]
	start_urls = [
       "https://s.taobao.com/search?q=男鞋&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.2&initiative_id=tbindexz_20150824"
    ] 
	def parse(self,response):
		self.mongo=connectMogod()
		self.num=0
		self.id=0
		self.wanted_num=10
		logging.log(logging.INFO, "==start==")
		test=str(response.xpath("//script/text()")[2].extract().encode("utf-8")).split("g_page_config = ")
		print  "====group 1",test[0]
		print  "====group 2",test[1]
		result=test[1][0:len(test[1])-2]
		data=result[1]
		print "===data is: ",data
		#处理数量，省的下载一大堆
		self.num=self.num+1
		if(self.num>=self.wanted_num):
			return


