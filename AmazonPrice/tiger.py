# coding=utf-8
from concurrent import futures
import urllib2,chardet
import datetime
import time
import requests
from lxml import html
import urllib,urllib2,httplib,cookielib,os,sys
from bs4 import BeautifulSoup
import lxml.html
import socket, traceback
import random
import linecache  
import base64
from pyDes import *
from xml.dom.minidom import parse, parseString
from socket import *
import re
import json

def get_page(opener,url,data={}):
	a = random.randrange(1, 9173)
	ua = linecache.getline(r'ua_list.txt', a)
	headers = {'User-Agent': ua} 
	postdata=urllib.urlencode(data)
	if postdata:
		request=urllib2.Request(url,postdata,headers=headers)
	else:
		request=urllib2.Request(url,headers=headers)
		f = opener.open(request)
		content = f.read()
		#log(content,url);
		return content

def amazonDe(arg,path):
        t = 'amazon.sh'
        cmd = "./%s %s %s" % (t,arg,path)
        session = os.popen(cmd).read()
        session = session.strip('\n')
        return session


#URLS = ['http://tiger-netshop.jp/shop/g/gMBR-A06GR-02/']
URLS = ['http://tiger-netshop.jp/shop/g/gMBR-A06GR/',
	'http://tiger-netshop.jp/shop/g/gMBR-A06GA/',
	'http://tiger-netshop.jp/shop/g/gMBR-A06GY/']
def load_url(url, timeout):
	#OFFERID_SELECTOR = '//*[@id="spec_stock_msg"]'
	OFFERID_SELECTOR = '//*[@id="spec_stock_msg"]'
	print "===================================>>"	
	cookiejar=cookielib.MozillaCookieJar()
	cj=urllib2.HTTPCookieProcessor(cookiejar)
	opener=urllib2.build_opener(cj)
	price1 = get_page(opener,url)
	mychar = chardet.detect(price1) 
	a = mychar['encoding']
	price = price1.decode(a,'ignore').encode('utf-8') 
	asinpath = './mobildata/tiger'
        datapath = asinpath + '/data'
        if os.path.isdir(asinpath):
                pass
        else:
                os.mkdir(asinpath)
        if os.path.exists(datapath):
                os.remove(datapath)
                os.mknod(datapath)
        else:
                os.mknod(datapath)
        local2 = open(datapath, 'w')
        local2.write(price)
        local2.close()
	offerid = amazonDe("getTigerStatus",datapath)
	items = url.split('/', 5 )[5]
	if offerid == '○': 
		print datetime.datetime.now(),items,"OK"
	else:
		print datetime.datetime.now(),"NULL" 
	
while True: 
	with futures.ThreadPoolExecutor(max_workers=10) as executor:
		#time.sleep(10)
		future_to_url = dict((executor.submit(load_url, url, 60), url)
				for url in URLS)
	   
