# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class DmozItem(scrapy.Item):
    name=Field()
    link=Field()
    desc=Field()
