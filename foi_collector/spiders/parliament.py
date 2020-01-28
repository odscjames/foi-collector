# -*- coding: utf-8 -*-
import scrapy
import hashlib


class ParliamentSpider(scrapy.Spider):
    name = 'parliament'
    source_title = 'House of Commons'
    source_link = 'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/'
    allowed_domains = ['www.parliament.uk']
    start_urls = [
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/events/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/estates-information/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/catering-services-retail/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/the-speaker/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/information-technology/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/human-resources/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/official-expenditure-/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/members-of-the-house-of-commons-and-members-staff/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/other-house-matters/',
        'https://www.parliament.uk/site-information/foi/foi-and-eir/commons-foi-disclosures/environmental/',
    ]

    def parse(self, response):
        for item in response.css('#ctl00_ctl00_FormContent_SiteSpecificPlaceholder_PageContent_ctlMainBody_wrapperDiv a'):
            link = 'https://www.parliament.uk' + item.css('a::attr(href)').get()
            yield scrapy.Request(
                url=link,
                callback=self.parse_item
            )

    def parse_item(self, response):
        question_bits = response.css('.main-introduction *::text').extract()
        question = ' '.join(question_bits).strip()[8:].strip()
        response = {
            'question': question,
            'link': response.request.url,
            'id': hashlib.md5(response.request.url.encode('utf-8')).hexdigest()
        }
        return response

