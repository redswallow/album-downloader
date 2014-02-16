Album-Downloader
================
Some simple image spider examples using scrapy.

## Requirements

使用包管理器pip / easy_install

依赖于scrapy, PIL:

`pip install scrapy`

`pip install PIL`

## Usage
Crawl all douban albums of a user:

e.g. http://www.douban.com/people/redswallow/photos

USERNAME = redswallow

`scrapy crawl douban_image_spider -a username=USERNAME`

Crawl a specific douban album

e.g. http://www.douban.com/photos/album/99908571/

ALBUM_ID = 99908571

`scrapy crawl douban_image_spider -a album=ALBUM_ID`

## Credits

Written by Yan Hong (redswallowjysc@gmail.com) (@redswallow)
