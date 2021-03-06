# -*- coding: utf-8 -*-

# Scrapy settings for scrapeNews project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import logging
import os

BOT_NAME = 'scrapeNews'

SPIDER_MODULES = ['scrapeNews.spiders']
NEWSPIDER_MODULE = 'scrapeNews.spiders'

LOG_LEVEL = 'ERROR'  # to only display errors
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapeNews (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapeNews.middlewares.ScrapenewsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
HTTP_PROXY = 'http://127.0.0.1:8118'
DOWNLOADER_MIDDLEWARES = {
    'scrapeNews.middlewares.TorProxyMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapeNews.pipelines.ScrapenewsPipeline': 100,
    'scrapeNews.pipelines.DuplicatesPipeline': 200,
    'scrapeNews.pipelines.DataFormatterPipeline': 300,
    'scrapeNews.pipelines.DatabasePipeline': 400
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 1.0
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 30
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.5
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Logger Configuration (scrapeNews)
logger = logging.getLogger("scrapeNews")
handler = logging.FileHandler('scrapeNews.log')
formatter = logging.Formatter('%(asctime)s %(name)-12s [%(lineno)d]%(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

DB_INFO = {}
try:
    DB_INFO['USERNAME'] = os.environ['SCRAPER_DB_USER']
    DB_INFO['PASSWORD'] = os.environ['SCRAPER_DB_PASS']
    DB_INFO['NEWS_TABLE'] = os.environ['SCRAPER_DB_TABLE_NEWS']
    DB_INFO['SITE_TABLE'] = os.environ['SCRAPER_DB_TABLE_SITE']
    DB_INFO['LOG_TABLE'] = os.environ['SCRAPER_DB_TABLE_LOG']
    DB_INFO['DATABASE_NAME'] = os.environ['SCRAPER_DB_NAME']
    DB_INFO['HOST_NAME'] = os.environ['SCRAPER_DB_HOST']
except Exception as e:
    logger.critical(__name__ + " Getting Environment Variabled Failed! Msg: " + str(e))
    exit()