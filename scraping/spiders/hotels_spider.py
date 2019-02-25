import scrapy
from scrapy.loader import ItemLoader

from scraping.items import HotelItem


class HotelsSpider(scrapy.Spider):
    name = "hotels"
    url_template = 'https://www.tour.ne.jp/j_hotel/parts_hotel_list/?pg={page_num}&dp_ymd=20190225'
    start_urls = [url_template.format(page_num=1)]

    def parse(self, response):

        #for hotel in response.xpath('//div[@class="search-result-item-header"]'):
        for hotel in response.xpath('//section[@class="Area_plan_section search-result-item"]'):
            yield {
                'name': hotel.xpath('.//a[@class="viewSch Area_hotel_name"]/text()').get().strip(),
                'price_class': hotel.xpath('.//span[@class="review-rate Area_grade"]/span')[0].attrib['class'].split('rank-')[1],
                'prefecture': response.xpath('//div[@class="search-result-item-header"]')[0].xpath('.//div[@class="cell Area_hotel_area"]/a/text()')[0].get(),
                'city': response.xpath('//div[@class="search-result-item-header"]')[0].xpath('.//div[@class="cell Area_hotel_area"]/a/text()')[1].get()
            }

        #     l = ItemLoader(item=HotelItem(), response=response)
        #     l.add_xpath('name', '//div[@class="price"]/span')
        #     l.add_xpath('file_urls', '//img[@class="photo-tile-image"]/@href')
        #     l.add_value('meta', response.meta)
        #     # l.add_xpath('address', '//h1[@class="zsg-h1"]/descendant::*')
        # return l.load_item()
