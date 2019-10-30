# -*- coding: utf-8 -*-
import scrapy
import json
from zhihu_title_url.settings import ALL_QUERY_WORD
from zhihu_title_url.items import ZhihuTitleUrlItem


class ZhtSpider(scrapy.Spider):
    name = 'zht'
    start_urls = [
        'https://www.zhihu.com/api/v4/search_v3?t=general&q={}&correction=1&offset=20&limit=20'.format(every_query_word)
        for every_query_word in ALL_QUERY_WORD]

    def parse(self, response):
        item = ZhihuTitleUrlItem()
        all_data_dict = json.loads(response.body.decode())["data"]
        for every_content_data in all_data_dict:
            try:
                item["title_url"] = self.detail_title_url(every_content_data["object"]["url"],
                                                  every_content_data["object"]["question"]["url"])
                item["voteup_count"] = every_content_data["object"]["voteup_count"]
                yield item
            except:
                pass

        if not json.loads(response.body.decode())["paging"]["is_end"]:
            next_url=json.loads(response.body.decode())["paging"]["next"]
            print(next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )

    def detail_title_url(self, question, answers):
        url = "https://www.zhihu.com/" + answers.split('/')[3][:-1] + '/' + answers.split('/')[4] + '/' + \
              question.split('/')[3][:-1] + '/' + question.split('/')[4]
        return url
