from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from bot.items import ImageItem

class DoubanImageSpider(CrawlSpider):
    name = "douban_image_spider"
    allowed_domains = ["douban.com"]
    start_urls = []
    rules = [
            Rule(SgmlLinkExtractor(allow = 'photos/album/\d+/[\?start=\d+]?'), callback = 'parse_image', follow = True)
    ]

    def __init__(self, username = 'redswallow', *args, **kwargs):
        super(DoubanImageSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
                "http://www.douban.com/people/%s/photos" % username
        ]

    def parse_image(self, response):
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
