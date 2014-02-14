import urllib2,re,os,time,ConfigParser
from queue import queue

#global config
config = ConfigParser.ConfigParser()
config.read("config.ini")
cookie = "".join(("t=",config.get("renren","t")))

def create_folder():
    #create_folder  
    folder=time.strftime("%Y%m%d_%H%M%S", time.localtime())
    os.makedirs(folder)
    return folder

def download_album(photos,folder):
    for pic in photos:
        url=re.findall('large:\'(.*?)\'',pic)[0]
        filename="".join((folder,'\\',url.split('/')[-1]))
        queue.put((url,filename))

def renren(url):
    req=urllib2.Request(url)
    req.add_header('Cookie',cookie)
    content=urllib2.urlopen(req).read()
    photos=re.findall('data-photo="(.*?)"',content)
    download_album(photos,create_folder())

if __name__=='__main__':
    url='http://photo.renren.com/photo/245983299/album-462669527'
    renren(url)
