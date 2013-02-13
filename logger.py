import time

def log(file,info,printflag=True):
    if printflag: 
        print info
    now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    file=open(file,"a+")
    file.write('%s %s\n'%(now,info))
    file.close()

if __name__=='__main__':
    log("hello")
