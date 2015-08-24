#coding=utf-8
import scrapy
class w3cSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains = ["taobao.com/"]
	start_urls = [
       "https://www.taobao.com/"
    ] 

	def parse(self,response):
		self.num=0
		self.wanted_num=10
		for sel in response.xpath("//a[@href]/@href"):
			self.num=self.num+1
			if(self.num>=self.wanted_num):
				return
			print sel.extract()




