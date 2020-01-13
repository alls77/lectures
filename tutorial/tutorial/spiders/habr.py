# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from tutorial.items import TutorialItem


class HabrSpider(scrapy.Spider):
    name = 'habr'
    allowed_domains = ['habr.com']
    start_urls = ['https://habr.com/ru/']


    def parse(self, response):
        article_urls = response.xpath("//li/article[contains(@class, 'post_preview')]/h2/a/@href").extract()

        for i in article_urls:
            yield scrapy.Request(url=i, callback=self.call_parse)
            


    def call_parse(self, response):
        name = response.xpath("//article[contains(@class, 'post_full')]/div/h1/span/text()").get()
        time = response.xpath("//article/div/header/span/text()").get()

        items = TutorialItem()
        items['name'] = name
        items['time'] = time

        yield items
