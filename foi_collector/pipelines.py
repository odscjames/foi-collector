# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from foi_collector.writer import FOISourceWriter


class FoiCollectorPipeline(object):

    def __init__(self):
        self.writer = FOISourceWriter()

    def process_item(self, item, spider):
        self.writer.add_data(item)
        return item

    def close_spider(self, spider):
        self.writer.write('/tmp/out.json')

