# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IpItem(scrapy.Item):
    # 自增属性
    # id =
    ip_type = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass
