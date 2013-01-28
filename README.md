Album-Downloader
================
Simple Python script to download all images in an douban/renren album at once.

## Requirements

使用包管理器pip / easy_install

解析网页用到了pyquery，pyquery依赖于lxml，win下请先到[这里](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml)下载lxml二进制安装包。

`pip install pyquery`

## Usage

###douban
`python -d controller.py ALBUM_URL` or `python --douban controller.py ALBUM_URL`
###flickr
`python -f controller.py ALBUM_URL` or `python --flickr controller.py ALBUM_URL`
###renren
`python -r controller.py ALBUM_URL` or `python -renren controller.py ALBUM_URL`

## Credits

Written by Yan Hong (redswallowjysc@gmail.com) (@redswallow)
