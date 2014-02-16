# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.conf import settings
import os
import urllib2

class FilterWordsPipeline(object):
    words_to_filter = ['politics', 'free']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['desc']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
            else:
                return item

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta=dict(album=item['album'])) for x in item.get(self.IMAGES_URLS_FIELD, [])]

    def file_path(self, request, response=None, info=None):
        url = request.url
        album = request.meta.get('album')
        image_guid = url.split('/')[-1]
        return '%s/%s.jpg' % (album, image_guid)
