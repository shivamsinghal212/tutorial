# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
DOWNLOAD_DELAY = 1 


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'Accept-Language': 'en-US,en;q=0.8',
   'Accept-Encoding': 'gzip, deflate',
   'Cookie': '__cfduid=d0183106273890ae73fba475a4992ce311507718917; cb_config=%7B%7D; cbzads=IN|AS|16|Pune; _col_uuid=797ec2d6-2011-40ab-839b-c034982cd15a-10oqo~1; ext_name=jaehkpjddfdgiiefcnhahapilbejohhj',
   'DNT': '1',
   'Host': 'www.cricbuzz.com',
   'Proxy-Connection': 'keep-alive',
   'Upgrade-Insecure-Requests':'1',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
   'Proxy-Authorization': 'Negotiate TlRMTVNTUAADAAAAGAAYAHwAAAAgASABlAAAAAQABABYAAAAEAAQAFwAAAAQABAAbAAAABAAEAC0AQAAFYKI4goAACgAAAAPSlpzW/gK4J/SPkQ4Z21GB0EAUABzAGkAbgBnAGkAcwBoAGkAVwBMADMAMAA0ADkAOQAyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZxIPxU0TY0UN8plkD0njsBAQAAAAAAAKVyOTWHQtMBU66nIgJcyf8AAAAAAgAEAEEAUAABABAAVwBTADAAMAAzADAANgA0AAQAGABhAHAALgB0AGkAZQB0AG8ALgBjAG8AbQADACoAVwBTADAAMAAzADAANgA0AC4AYQBwAC4AdABpAGUAdABvAC4AYwBvAG0ABQASAHQAaQBlAHQAbwAuAGMAbwBtAAgAMAAwAAAAAAAAAAEAAAAAIAAABIRb2e7svFlBUl8LPYV91gymLuK4gEQXTZU8zdRvpIEKABAAAAAAAAAAAAAAAAAAAAAAAAkAJABIAFQAVABQAC8AMQAwAC4AOAAzAC4AMQA5ADIALgAyADEANgAAAAAAAAAAABFa5Mll9TM/mvOaa1yWQt0=',
   'Cache-Control':' max-age=0'
   }



# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
