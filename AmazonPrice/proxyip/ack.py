import httplib
import time
import urllib
import threading

inFile = open('proxy.txt', 'r')
outFile = open('available.txt', 'w')

lock = threading.Lock()

def test():
    while True:
        lock.acquire()
        line = inFile.readline().strip()
        lock.release()
        if len(line) == 0: break
        protocol, proxy = line.split('=')
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': ''}
        try:
            conn = httplib.HTTPConnection(proxy, timeout=3.0)
            conn.request(method='GET', url='http://d3l3lkinz3f56t.cloudfront.net/aan/de?Operation=GetDecoratedOffers&asins=B01DK14I6W&attributes=customerReviewSummary,itemTitle&marketplaceId=A1PA6795UKMFR9&token=CE3761E7E32448021808867B519D0E22C2360BFB&ContentType=JSON&JSONCallBack=serviceCallback', headers=headers )
            res = conn.getresponse()
            ret_headers = str( res.getheaders() ) 
            html_doc = res.read().decode('utf-8')
            print html_doc
            if "serviceCallback" in html_doc:
                lock.acquire()
                print 'add proxy', proxy
                outFile.write(proxy + '\n')
                lock.release()
            else:
                print '.',
        except Exception, e:
            print e

all_thread = []
for i in range(50):
    t = threading.Thread(target=test)
    all_thread.append(t)
    t.start()
    
for t in all_thread:
    t.join()

inFile.close()
outFile.close()
