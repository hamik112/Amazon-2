import httplib
import time
import urllib
import threading
import random
import linecache

lock = threading.Lock()
count = len(open("proxy.txt",'rU').readlines())

def test():
	while True:
		lock.acquire()
		a = random.randrange(1, 9173)
		ua = linecache.getline(r'ua_list.txt', a)
		lock.release()
		headers = {'Content-Type': 'application/x-www-form-urlencoded','Cookie': '','User-Agent': ua}
		lock.acquire()
		b = random.randrange(1, int(count))
		proxyip = linecache.getline(r'proxy.txt', b)
		lock.release()
		protocol, proxy = proxyip.split('=')
		try:
			conn = httplib.HTTPConnection(proxy, timeout=3.0)
			conn.request(method='GET', url='http://www.amazon.de/dp/B007X2CL6E?m=A3JWKAKR8XB7XF', headers=headers )
			res = conn.getresponse()
			html_doc = res.read().decode('utf-8')
			print html_doc	
		except Exception, e:
			print e

all_thread = []
for i in range(50):
	t = threading.Thread(target=test)
	all_thread.append(t)
	t.start()
    
for t in all_thread:
	t.join()

