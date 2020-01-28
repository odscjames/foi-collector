# -*- coding: utf-8 -*-
import scrapy


class IcoSpider(scrapy.Spider):
    name = 'ico'
    allowed_domains = ['icosearch.ico.org.uk', 'ico.org.uk']
    start_urls = ['https://icosearch.ico.org.uk/s/search.html?collection=ico-meta&profile=disclosurelog&&query=']

    def parse(self, response):
        for item in response.css('.resultlist .itemlink-content'):
            link = item.css('a::attr(title)').get()
            yield scrapy.Request(
                url=link,
                callback=self.parse_item
            )

    def parse_item(self, response):
        question_bits = response.css('.article-content *::text').extract()
        question = ' '.join(question_bits)
        response = {
            'question': question,
            'link': response.request.url,
        }
        return response

