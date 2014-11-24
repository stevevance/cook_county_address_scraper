# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CSVFeedSpider
from dirbot.items import Website

class DmozSpider(CSVFeedSpider):
    headers = ['street_number', 'street_name', 'street_direction']
    name = "propertyaddress"
    allowed_domains = ["www.cookcountypropertyinfo.com"]
    start_urls = (
        'http://www.chicagocityscape.com/propertytaxes/addresses_cleaned2.csv',
    )
    
    def parse_row(self, response, row):
        return scrapy.Request('http://www.cookcountypropertyinfo.com/Pages/Address-Results.aspx?hnum=' + row['street_number'] + '&sname=' + row['street_name'] + '&city=chicago&zip=&unit=&dir=' + row['street_direction'], callback=self.parse_address)

    def parse_address(self, response):
    	webpage = Website()
    	webpage['url'] = response.url
    	#webpage['body'] = response.css("#ctl00_PlaceHolderMain_ctl00_resultsPanel").extract()
    	webpage['body'] = response.body
    	return webpage