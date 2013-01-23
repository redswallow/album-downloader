import time,urllib2,os

#global config
url='http://www.flickr.com/photos/bbqpork/sets/72157625179685854/with/5087985395/'

def create_folder():
    #create_folder  
    folder=time.strftime("%Y%m%d_%H%M%S", time.localtime())
    os.makedirs(folder)
    return folder

def download_album(photos,folder):
    for pic in photos:
        larg_pic=pic[:-6]+'_z.jpg'
        filename=large_pic.split('/')[-1]
        image = urllib2.urlopen(large_pic).read()
        with open(folder+'\\'+filename,"wb" ) as f:
            f.write(image)
            f.close()
        print "download "+large_pic+" ok"

start=time.clock()

response=urllib2.urlopen(url)
str=response.read()
from flickr_geturl import *
my=Get:wUrl()
my.feed(str)
download_album(my.links,create_folder())
 
elapsed=time.clock()-start
print "Time used:",elapsed
