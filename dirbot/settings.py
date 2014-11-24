# Scrapy settings for dirbot project

BOT_NAME = 'cook_county_address_scraper'

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'

DOWNLOAD_DELAY = 0.05