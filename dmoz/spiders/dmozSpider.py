#coding=utf-8
from scrapy.contrib.loader import ItemLoader
import logging
from dmoz.items import FirstPageItem
import scrapy
class w3cSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains = ["taobao.com"]
	start_urls = [
       "https://s.taobao.com/search?q=男鞋&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.2&initiative_id=tbindexz_20150824"
    ] 
	def parse(self,response):
		self.num=0
		self.id=0
		self.wanted_num=10
		logging.log(logging.INFO, "==start==")
		for sel in  response.xpath("//script"):
			#item=FirstPageItem()
			#yield item
			print sel.xpath("text()").extract()
			self.num=self.num+1
			if(self.num>=self.wanted_num):
				return


