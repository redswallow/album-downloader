# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class FilterWordsPipeline(object):
    words_to_filter = ['politics', 'free']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['desc']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
            else:
                return item
