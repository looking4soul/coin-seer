# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinItem(scrapy.Item):
    # define the fields for your item here like:
    coin_name = scrapy.Field()
    coin_price = scrapy.Field()
    crawl_time = scrapy.Field()
    pass
