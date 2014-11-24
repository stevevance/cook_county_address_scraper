import scrapy

class Website(scrapy.Item):

    body = scrapy.Field()
    url = scrapy.Field()