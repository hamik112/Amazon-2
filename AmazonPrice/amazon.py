# coding=utf-8
from concurrent import futures
import urllib2
import datetime
import time
import requests
from lxml import html
import urllib,urllib2,httplib,cookielib,os,sys
from bs4 import BeautifulSoup
import lxml.html
import socket, traceback
import json

def udp_send(ID):
	host = '' # Bind to all interfaces
	port = 1234
	print "python UDP multi case server test"
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.bind((host, port))
	ip = sys.argv[1]
        sendport = int(sys.argv[2])
	for i in range(1,2):
		try:
			#s.sendto(ID,('133.130.106.179', 2345))
			s.sendto(ID, (ip, sendport))
			#message, address = s.recvfrom(1234)
			#print "Got data from", address,":",message
			#s.sendto(ID, ('23.234.223.143', 19121)) 
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			traceback.print_exc()
	return


def get_page(opener,url,data={}):
    headers = {'Referer': 'http://www.amazon.de/dp/B00BSNACII?m=A3JWKAKR8XB7XF',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Host': 'www.amazon.de'
	}

    postdata=urllib.urlencode(data)
    if postdata:
        request=urllib2.Request(url,postdata,headers=headers)
    else:
        request=urllib2.Request(url,headers=headers)
    f = opener.open(request)
    content = f.read()
    #log(content,url);
    return content
 
URLS = ['http://www.amazon.de/gp/twister/dimension?asinList=B00BSNACII&vs=1&exclusiveMerchantId=A3JWKAKR8XB7XF&productTypeDefinition=GROCERY&productGroupId=grocery_display_on_website&storeId=grocery&parentAsin=B013USRV1E&isPrime=0&nodeID=340846031&webpSupport=1&fastRenderTreatment=C']
num = 1 
def load_url(url, timeout):
	XPATH_SELECTOR = '//span[@id="priceblock_ourprice"]'
	SLEEP_INTERVAL = 1
	cookiejar=cookielib.CookieJar()
	cj=urllib2.HTTPCookieProcessor(cookiejar)
	opener=urllib2.build_opener(cj)
	price = get_page(opener,url)
	pricetmp = price.split('[')[1].split(']')[0]
	pricejson = json.loads(pricetmp)
	priceAsin = pricejson[u"price"]
	Asin = pricejson[u"asin"]
	pricestatus = pricejson[u"isAvailable"]
	time = datetime.datetime.now()
	print num
	print "%s\t%s\t%s\t%s"%(time,Asin,priceAsin,pricestatus)
		
	if priceAsin == None:
		return
	else:
		if pricestatus == True:
			if (num > 20):
				udp_send("B00BSNACII")
				global num
				num = 1
			else:
				return
		else:
			return	
while True: 
	with futures.ThreadPoolExecutor(max_workers=5) as executor:
		num += 1
		future_to_url = dict((executor.submit(load_url, url, 60), url)
				 for url in URLS)
