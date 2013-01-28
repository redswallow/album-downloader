import threading,urllib2
lock = threading.Lock()  

class Worker(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.daemon= True

    def run(self):
        while True:
            url,filename=self.queue.get()
            #running task
            self.save_image(url,filename)
            self.queue.task_done()

    def save_image(self,url,filename):
        image = urllib2.urlopen(url).read()
        with open(filename,"wb") as f:
            f.write(image)
            f.close()
        print "download "+url+" ok"
