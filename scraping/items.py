# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelItem(scrapy.Item):

    name = scrapy.Field()
    price_class = scrapy.Field()
    prefecture = scrapy.Field()
    city = scrapy.Field()
    items_number = scrapy.Field()
    offer_sources = scrapy.Field()
