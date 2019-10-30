# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from zhihu_title_url.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_TABLE


class ZhihuTitleUrlPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            db=MYSQL_TABLE,
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if item["voteup_count"] >= 1000:
            insert_sql = """INSERT INTO high_heat_url(url,voteup_count) VALUES ("{}","{}")""".format(item["title_url"],
                                                                                     item["voteup_count"])
            try:
                self.cursor.execute(insert_sql)
                self.connect.commit()
                print("插入数据库成功")
            except Exception as e:
                print("插入数据库失败")
                self.connect.rollback()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
