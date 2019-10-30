# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_title_url project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
BOT_NAME = 'zhihu_title_url'

SPIDER_MODULES = ['zhihu_title_url.spiders']
NEWSPIDER_MODULE = 'zhihu_title_url.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihu_title_url.middlewares.ZhihuTitleUrlSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihu_title_url.middlewares.ZhihuTitleUrlDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihu_title_url.pipelines.ZhihuTitleUrlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_LEVEL = "WARNING"
ALL_QUERY_WORD = ['留学']
# COOKIES="_zap=f6478b18-6036-4ce9-af34-3a7f8745c374; _xsrf=W1nlNf70ImbDqe5QOmSeo6PScZU48o8n; d_c0='AEDmtg65IhCPTo9TFecFi71KoarLyF4gcY0=|1569988120'; tst=r; q_c1=7c2f33612db3473482683041e58fc5c7|1571734615000|1571734615000; cap_id='ZTViMDQyZDNmMzQ3NGRlZmJjMTU4Y2I2YTIzZDliNzI=|1572075342|286683c0b8a478356df29415c33681daaab3377c'; r_cap_id='YzExODQ0YjMwYWNlNGI3ZGFjY2U4MWIzMDcwY2QzYjk=|1572075342|41fc1c16f7c2cb462c2e07c6ecc66aac2ed9e055'; l_cap_id='ZjdmNzFjNTcxY2Y3NDdkMTk5NjdkNjAyMDRkYWNlMDA=|1572075343|18e09fe8093aa1cf1efcdf3bc6c154cdecad5499'; capsion_ticket='2|1:0|10:1572075346|14:capsion_ticket|44:ZWFhMTE0NGNhYzY5NDYzYjliNzE0ZGM2YzNiZGJiOWM=|871b10879adf09a5364f7548f10a13be438270905abe6812eb611e2d5985ef13'; z_c0='2|1:0|10:1572075354|4:z_c0|92:Mi4xLXZxYUV3QUFBQUFBUU9hMkRya2lFQ1lBQUFCZ0FsVk5Xa1doWGdBb2w4aExiR1ZYZS1BbDBjSjR5UHN0YXNzYkdB|87d467dbffdcd8b32b916c2be81d5d898aaaef41ed989f0755fe8b9d48f4dc02'; __utma=51854390.766070844.1571734619.1571734619.1572250861.2; __utmz=51854390.1572250861.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100--|2=registration_date=20191024=1^3=entry_date=20191022=1; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1572224187,1572311385,1572396038,1572426537; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1572426537"

MYSQL_HOST='服务器地址'
MYSQL_USER='MYSQL用户'
MYSQL_PASSWORD='MYSQL密码'
MYSQL_PORT=3306
MYSQL_TABLE='MYSQL表名'

name = "scrapy-{}.log".format(time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time())))
log_file_path = "log/scrapy-{}".format(name)