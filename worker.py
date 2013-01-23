import threading
lock = threading.Lock()  

class Worker(threading.Thread):
    def __init__(self,queue,task):
        threading.Thread.__init__(self)
        self.queue = queue
        self.task = task
        self.daemon= True

    def run(self):
        while True:
            self.task()
