import time,urllib2,os
from pyquery import PyQuery
from queue import queue

def create_folder():
    #create_folder  
    folder=time.strftime("%Y%m%d_%H%M%S", time.localtime())
    os.makedirs(folder)
    return folder

def download_album(links,folder):
    for link in links:
        filename='%s\\%s'%(folder,link.split('/')[-1])
        queue.put((link,filename))

def flickr(url):
    page=PyQuery(urllib2.urlopen(url).read())
    #get img-src
    links=[link.values()[0].replace('_s','_z') for link in page('.photo-display-item img')]
    download_album(links,create_folder())

if __name__=='__main__':
    url='http://www.flickr.com/photos/bbqpork/sets/72157625179685854/with/5087985395'
    flickr(url)
