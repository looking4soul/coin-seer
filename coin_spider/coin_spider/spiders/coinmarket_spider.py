#!/usr/bin/python
#-*- coding:utf-8 –*-

import scrapy
import datetime
from coin_spider.items import CoinItem

class CoinmarketSpider(scrapy.Spider):
    name = "coinmarket"
    start_urls = ["http://coinmarketcap.com/all/views/all/"]

    def parse(self, response):
        now_minute = datetime.datetime.strptime(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:00"), "%Y-%m-%d %H:%M:%S")
        for row in response.xpath('//tbody//tr'):
            item = CoinItem()
            item['coin_name'] = row.xpath("./td[2]/a/text()").extract_first()
            item['coin_price'] = row.xpath("./td[5]/a/text()").extract_first().strip("$")
            item['crawl_time'] = now_minute
            yield item