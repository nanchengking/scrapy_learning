#coding=utf-8
from scrapy.contrib.loader import ItemLoader
import logging
from Mogodb import *
from dmoz.items import FirstPageItem
import scrapy
class w3cSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains = ["taobao.com"]
	start_urls = [
       "https://s.taobao.com/search?q=男鞋&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.2&initiative_id=tbindexz_20150824"
    ] 
	def parse(self,response):
		self.saveData=SaveData()
		self.num=0
		self.id=0
		self.wanted_num=10
		logging.log(logging.INFO, "==start==")
		info= str(response.xpath("//script/text()")[2].extract().encode('utf-8')).split('g_page_config =')[1].strip()
		info= info[1:len(info)-2].strip()
		data={info}
		file=open('item.txt','wb')
		file.write(str(data))
		self.saveData.save(data)
		#print info





