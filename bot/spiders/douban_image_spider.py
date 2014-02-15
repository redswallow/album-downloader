from scrapy.spider import Spider
from scrapy.selector import Selector
from bot.items import ImageItem

class DoubanImageSpider(Spider):
    name = "douban_image_spider"
    allowed_domains = ["douban.com"]
    start_urls = ['http://www.douban.com/photos/album/117515388']

    def __init__(self):
        pass

    def parse(self, response):
        sel = Selector(response)
        photolst = sel.xpath('//div[@class="photolst clearfix"]/div')
        items = []
        for photo in photolst:
            try:
                item = ImageItem()
                item['image_urls'] = [url.replace('thumb','photo') for url in photolst.xpath('a/img/@src').extract()]
                items.append(item)
            except:
                pass
        return items
