import datetime

import pymongo

import scrapy
import re

from pytz import timezone

# client = pymongo.MongoClient()
# db = client['test']

japan = timezone('Japan')
japan_now = datetime.datetime.now(japan)
date_str = '{}{:02d}{}'.format(japan_now.year, japan_now.month, japan_now.day)

class HotelsSpider(scrapy.Spider):
    name = "hotels"
    url_template = 'https://www.tour.ne.jp/j_hotel/parts_hotel_list/?pg={page_num}&dp_ymd={date_str}'

    def start_requests(self):
        page_num = 1
        urls = [self.url_template.format(page_num=page_num, date_str=date_str)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'page_num': page_num})

    def parse(self, response):
        hotels = response.xpath('//section[@class="Area_plan_section search-result-item"]')
        if hotels:
            page_num = response.meta['page_num'] + 1
            hotel_list_url = self.url_template.format(page_num=page_num, date_str=date_str)
            yield response.follow(hotel_list_url, self.parse, meta={'page_num': page_num})
            for hotel in hotels:
                hotel_url = hotel.xpath('.//a[@class="viewSch Area_hotel_name"]')[0].attrib['href']

                # if we need this functionality better to add middleware
                #id = hotel_url.rsplit('/', 2)[1]
                # existed_hotel = db.hotels.find_one({"id": id})
                # if not existed_hotel:
                yield response.follow(hotel_url, self.parse_hotel)

    def parse_hotel(self, response):

        try:
            type = re.search('TRAVELKO.APP.hotel_type="(\d)"', response.text).group(1)
        except:
            type = ''

        yield {
            'id': response.url.rsplit('/', 2)[1],
            'name': response.xpath('//span[@id="Area_hotel_name"]/text()').get(),
            'type': type,
            'region': re.search('dist1=(\d*)', response.xpath('//div[@class="cell Area_hotel_area"]/a[1]')[0].attrib['href']).group(1),
            'prefecture': response.xpath('//div[@class="cell Area_hotel_area"]/a[1]/text()').get(),
            'city': response.xpath('//div[@class="cell Area_hotel_area"]/a[2]/text()').get(),
            'hotel_address': response.xpath('//span[@id="Area_hotel_address"]/text()').get(),
            'x': re.search('TRAVELKO.APP.pos_x="(.*?)"', response.text).group(1),
            'y': re.search('TRAVELKO.APP.pos_y="(.*?)"', response.text).group(1),
            'rating': response.xpath('//span[@class="review-sup Area_evaluation_text"]/text()').get('')
        }
