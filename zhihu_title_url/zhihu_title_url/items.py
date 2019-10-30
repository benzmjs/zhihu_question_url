# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuTitleUrlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    title_url=scrapy.Field()
    voteup_count=scrapy.Field()
