BOT_NAME = 'bot'
BOT_VERSION = '0.1'

SPIDER_MODULES = ['bot.spiders']
NEWSPIDER_MODULE = 'bot.spiders'
DEFAULT_ITEM_CLASS = 'bot.items.ImageItem'

ITEM_PIPELINES = [
    #'scrapy.contrib.pipeline.images.ImagesPipeline'
    'bot.pipelines.MyImagesPipeline'
]
IMAGES_STORE = 'images'
IMAGE_EXPIRES = 180 # 180 days

USER_AGENT = "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0"
