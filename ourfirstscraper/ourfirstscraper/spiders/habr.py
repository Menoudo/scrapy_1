# -*- coding: utf-8 -*-
import scrapy


class HabrSpider(scrapy.Spider):
    name = 'habr'
    allowed_domains = ['habr.com']
    start_urls = ['https://habr.com/',
                  'https://habr.com/page2/',
                  'https://habr.com/page3/',
                  'https://habr.com/page4/']

    def parse(self, response):
        # Extracting the content using css selectors
        titles = response.css('.post__title_link::text').extract()
        #votes = response.css('.score.unvoted::text').extract()
        times = response.css('.post__time::text').extract()
        #comments = response.css('.comments::text').extract()

        # Give the extracted content row wise
        for item in zip(titles, times):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'created_at': item[1],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
