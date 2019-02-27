# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelItem(scrapy.Item):

    name = scrapy.Field()
    type = scrapy.Field()
    region = scrapy.Field()
    prefecture = scrapy.Field()
    city = scrapy.Field()
    hotel_address = scrapy.Field()
    geocoordinates = scrapy.Field()
    rating = scrapy.Field()
    offer_sources = scrapy.Field()

#Each
#hotel should include: hotel name, hotel type, region, prefecture, city, hotel address, geocoordinates,
#number of reviews, offers from what additional source are available.