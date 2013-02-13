import sys,os
from optparse import OptionParser
from worker import Worker,lock
from queue import queue

_options=['flickr','renren','douban','lastfm']

def init():
    #init threading
    for i in xrange(5):
        Worker(queue).start()

if __name__ == "__main__":
    dirname = os.path.dirname(os.path.abspath(__file__))
    init()
    parser = OptionParser()
    parser.add_option("-t", "--tool",dest="tool")
    #get args
    opts, args =parser.parse_args()
    print opts,args
    if opts.tool=='flickr':
        import flickr_image
        flickr_image.flickr(args[0])
    elif opts.tool=='renren':
        import renren_image
        renren_image.renren(args[0])
    elif opts.tool=='douban':
        import douban_image
        douban_image.douban(args[0])
    elif opts.tool=='lastfm':
        import lastfm_image
        lastfm_image.lastfm(args[0])
    else:
        print Exception 
    queue.join()
