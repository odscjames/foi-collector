# -*- coding: utf-8 -*-
import scrapy
import hashlib

class IcoSpider(scrapy.Spider):
    name = 'ico'
    source_title = 'Information Commissioner\'s Office (ICO)'
    source_link = 'https://icosearch.ico.org.uk/s/search.html?collection=ico-meta&profile=disclosurelog&&quer'
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
        question = ' '.join(question_bits).strip()[8:].strip()
        response = {
            'question': question,
            'link': response.request.url,
            'id': hashlib.md5(response.request.url.encode('utf-8')).hexdigest()
        }
        return response

