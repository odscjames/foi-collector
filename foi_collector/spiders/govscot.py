# -*- coding: utf-8 -*-
import scrapy
import hashlib

class GovScotSpider(scrapy.Spider):
    name = 'govscot'
    source_title = 'Scottish Government'
    source_link = 'https://www.gov.scot/publications/?publicationTypes=foi-eir-release&page=1'
    allowed_domains = ['gov.scot']
    start_urls = ['https://www.gov.scot/publications/?publicationTypes=foi-eir-release&page=1']

    def parse(self, response):
        # TODO Look for next page button here and go thru - beware if done in full that will be 5000 requests!

        for item in response.css('ol#search-results-list article'):
            link = 'https://www.gov.scot' + item.css('a::attr(href)').get()
            yield scrapy.Request(
                url=link,
                callback=self.parse_item
            )

    def parse_item(self, response):
        question_bits = response.css('.publication-body .publication-body *::text').extract()
        question = ' '.join(question_bits).strip()[22:].strip()
        response = {
            'question': question,
            'link': response.request.url,
            'id': hashlib.md5(response.request.url.encode('utf-8')).hexdigest()
        }
        return response

