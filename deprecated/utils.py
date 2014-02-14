def get_failed():
    f=open('log_error.txt','r')
    lines=f.readlines()
    failed=set([line.split()[-1] for line in lines])
    print len(failed),failed

if __name__=='__main__':
    get_failed()
