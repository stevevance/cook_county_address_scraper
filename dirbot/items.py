from scrapy.item import Item, Field


class Website(Item):

    body = scrapy.Field()
    url = scrapy.Field()