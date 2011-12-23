from urllib import urlencode
import urllib2,cookielib
import time,re

def albumdown(URL):
    #get_image_url
    str=urllib2.urlopen(URL).read()
    flist=[]
    flist=re.findall('src="(.*?thumb.*?)"',str)

    #download_image
    for file in flist:
        file=re.sub('(?<=/)thumb(?<!/)',r'photo',file)
        filename=file.split('/')[-1]
        jpg=urllib2.urlopen(file).read()
        File=open(PATH+folder+'//'+filename,"wb")
        File.write(jpg)
        File.close()
        print "download "+file+" ok"

#config
USERNAME='YOURUSERNAME'
PASSWORD='YOURPASSPORT'
DOWN_URL='http://www.douban.com/photos/album/52441585/'
PATH='YOUR_PATH'

start=time.time()

#cookie
cj=cookielib.LWPCookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#opener.addheaders=[('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
urllib2.install_opener(opener)
    
#login
url='https://www.douban.com/accounts/login'

data={'form_email':USERNAME,
      'form_password':PASSWORD
      }
url_data=urlencode(data)
req=urllib2.Request(url,url_data)
operate=opener.open(req)
print operate.geturl()
if operate.geturl()=='http://www.douban.com/':
    print 'Logged on successfully!'
    cj.save('douban.cookie')
else:
    print 'Logged on error'


#create_folder
folder=time.strftime("%Y%m%d_%H%M%S", time.localtime())
import os   
os.makedirs(folder)

#get album_total_page
str=urllib2.urlopen(DOWN_URL).read()
image_num=re.findall(r'<span class="count">.*?(\d+).*?</span>',str)
albumpage=(int(image_num[0])-1)/18+1

for i in range(albumpage):
    d="%i"%(i*18)
    DOWN_URL=DOWN_URL.split('?')[0]+'?start='+d
    albumdown(DOWN_URL)

elapsed=time.time()-start
print "Time used:",elapsed
