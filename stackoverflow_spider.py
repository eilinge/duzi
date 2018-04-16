# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EilingeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self,response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            print('full_url',full_url)
            yield scrapy.Request(full_url,callback=self.parse_question)

    def parse_question(self,response):

        yield {
            'title':response.css('h1 a::text').extract()[0],
            'votes':response.css('.question .vote-count-post::text').extract()[0],
            'body':response.css('.question .post-text').extract()[0],
            'tags':response.css('.question .post-tag::text').extract(),
            'link':response.url,
        }