# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from foi_collector.writer import FOISourceWriter


class FoiCollectorPipeline(object):

    def __init__(self, crawler):
        self.writer = FOISourceWriter()
        self.writer_output_file = crawler.settings['OUTPUT_FILE']

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_item(self, item, spider):
        self.writer.add_data(item)
        return item

    def close_spider(self, spider):
        self.writer.set_source(
            source_title=spider.source_title,
            source_link=spider.source_link,
        )
        self.writer.write(self.writer_output_file)

