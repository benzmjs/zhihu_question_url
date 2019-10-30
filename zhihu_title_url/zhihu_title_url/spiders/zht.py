# -*- coding: utf-8 -*-
import scrapy


class ZhtSpider(scrapy.Spider):
    name = 'zht'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
