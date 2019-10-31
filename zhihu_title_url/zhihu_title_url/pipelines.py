# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from zhihu_title_url.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_TABLE
from zhihu_title_url.settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB
import hashlib
import redis


class ZhihuTitleUrlPipeline(object):
    def __init__(self):
        self.connect_mysql = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            db=MYSQL_TABLE,
            charset='utf8'
        )
        self.cursor = self.connect_mysql.cursor()
        self.pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)
        self.connect_redis = redis.StrictRedis(connection_pool=self.pool)


    def process_item(self, item, spider):
        if item["voteup_count"] >= 1000:
            sha1_url=self.sha1(item["title_url"])
            start_count = self.connect_redis.scard('url')
            self.connect_redis.sadd('url', sha1_url)
            end_count = self.connect_redis.scard('url')
            if start_count != end_count:
                insert_sql = """INSERT INTO high_heat_url(url,voteup_count) VALUES ("{}","{}")""".format(
                    item["title_url"],
                    item["voteup_count"])
                try:
                    self.cursor.execute(insert_sql)
                    self.connect_mysql.commit()
                    print("插入数据库成功")
                except Exception as e:
                    print("插入数据库失败,失败原因{}".format(e))
                    self.connect_mysql.rollback()

    def sha1(self,url):
        sha1obj = hashlib.sha1()
        sha1obj.update(url.encode('utf-8'))
        sha1_url = sha1obj.hexdigest()
        return sha1_url

    def close_spider(self, spider):
        self.cursor.close()
        self.connect_mysql.close()
        self.pool.disconnect()