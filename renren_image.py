import urllib2,re,os,time,ConfigParser,Queue
from worker import *

#global config
config = ConfigParser.ConfigParser()
config.read("config.ini")
cookie = "".join(("t=",config.get("renren","t")))
queue=Queue.Queue()

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

def save_image(url,filename):
    image = urllib2.urlopen(url).read()
    with open(filename,"wb" ) as f:
        f.write(image)
        f.close()
    print "download "+url+" ok"

def renren(url):
    req=urllib2.Request(url)
    req.add_header('Cookie',cookie)
    content=urllib2.urlopen(req).read()
    photos=re.findall('data-photo="(.*?)"',content)
    download_album(photos,create_folder())

def running_task():
    url,filename=queue.get()
    save_image(url,filename)
    #signals to queue job is done
    queue.task_done()

def init():
    #init threading
    for i in xrange(5):
        Worker(queue,running_task).start()

if __name__=='__main__':
    init()
    url='http://photo.renren.com/photo/449261954/album-852067402'
    renren(url)
    queue.join()
