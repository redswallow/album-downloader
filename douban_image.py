import urllib2,time,re,os
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

def douban(url):
    page=PyQuery(urllib2.urlopen(url).read())
    count=re.findall(r'\d+',page('.count').text())
    page_num=(int(count[0])-1)/18+1
    folder=create_folder()
    for i in xrange(page_num):
        page=PyQuery(urllib2.urlopen('%s?start=%d'%(url,i*18)).read())
        links=[link.values()[0].replace('thumb','photo') for link in page('.photo_wrap img')]
        download_album(links,folder)
        

if __name__=='__main__':
    url='http://www.douban.com/photos/album/83044911/'
    douban(url)
