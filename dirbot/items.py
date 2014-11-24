from scrapy.item import Item, Field


class Website(scrapy.Item):

    body = scrapy.Field()
    url = scrapy.Field()