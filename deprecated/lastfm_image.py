import urllib2,re,os,time
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

def lastfm(url):
    page=PyQuery(urllib2.urlopen(url).read())
    page_num=int(page('.lastpage').html())
    print page_num
    folder=create_folder()
    for i in xrange(1,page_num+1):
        page=PyQuery(urllib2.urlopen('%s?page=%d'%(url,i)).read())
        links=[link.values()[-1].replace('/126s/','/500/') for link in page('.pic img')]
        download_album(links,folder)

if __name__=='__main__':
    url='http://cn.last.fm/music/%E7%8E%8B%E5%BF%83%E5%87%8C/+images'
    lastfm(url)
