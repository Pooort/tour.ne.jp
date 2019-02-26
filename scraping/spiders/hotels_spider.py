import scrapy
from scrapy.loader import ItemLoader

from scraping.items import HotelItem


class HotelsSpider(scrapy.Spider):
    name = "hotels"
    url_template = 'https://www.tour.ne.jp/j_hotel/parts_hotel_list/?pg={page_num}&dp_ymd=20190225'
    #start_urls = [url_template.format(page_num=1)]

    def start_requests(self):
        page_num = 1
        urls = [self.url_template.format(page_num=page_num)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'page_num': page_num})

    def parse(self, response):
        hotels = response.xpath('//section[@class="Area_plan_section search-result-item"]')
        if hotels:
            page_num = response.meta['page_num'] + 1
            hotel_list_url = self.url_template.format(page_num=page_num)
            yield response.follow(hotel_list_url, self.parse)
            for hotel in hotels:
                hotel_url = hotel.xpath('.//a[@class="viewSch Area_hotel_name"]')[0].attrib['href']
                yield response.follow(hotel_url, self.parse_hotel)

    def parse_hotel(self, response):

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
