#coding:utf-8
import urllib2
import random
import linecache

def url_user_agent(url):
	b = random.randrange(1, int(count))
        proxyip = linecache.getline(r'proxy.txt', b)
        protocol, proxy = proxyip.split('=')
	print proxy,protocol
	proxy = {protocol:proxy}
	proxy_support = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
	req = urllib2.Request(url,headers=i_headers)
	html = urllib2.urlopen(req)
	doc = html.read()
	return doc


count = len(open("proxy.txt",'rU').readlines())
url = 'http://133.130.106.179/2.php'
doc = url_user_agent(url)
print doc
