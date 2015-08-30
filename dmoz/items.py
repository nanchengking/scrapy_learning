# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field
class FirstPageItem(scrapy.Item):
    index=Field()#排名
    price=Field()#价格
    number=Field()#付款人数
    itemName=Field()#商品名称
    itemLink=Field()#商品链接
    shopName=Field()#店铺名字
    shopLink=Field()#店铺链接
    area=Field()#所属地区
    id=Field()#id
    
