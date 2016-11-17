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


URLS = ['http://m.rossmannversand.de/produkt/364396/aptamil-mit-prebiotics-ha-3-folgenahrung-mit-hydrolysiertem-eiweiss.aspx']
#URLS = ['http://m.rossmannversand.de/produkt/359207/aptamil-pronutra-folgemilch-2.aspx']
def load_url(url, timeout):
	OFFERID_SELECTOR = '//div[@class="col-xs-7 col-sm-offset-1 col-sm-6 col-lg-offset-4 col-lg-3"]/a/@disabled'
	HREF_SELECTOR = '//div[@class="col-xs-7 col-sm-offset-1 col-sm-6 col-lg-offset-4 col-lg-3"]/a/@*'
	
	filename = 'cookiejp.txt'
	cookiejar=cookielib.MozillaCookieJar(filename)
	file = open(filename)
	cookielines = file.readlines(100)
	if cookielines:
		cookiejar.load('cookiejp.txt', ignore_discard=True, ignore_expires=True)
	else:
		cookiejar=cookielib.MozillaCookieJar(filename)
	cj=urllib2.HTTPCookieProcessor(cookiejar)
	opener=urllib2.build_opener(cj)
	price = get_page(opener,url)
	print price
	tree = html.fromstring(price)
	asinpath = './mobildata/Rossman_Aptamil_HA3'
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
	inStock = tree.xpath(HREF_SELECTOR)
	print inStock
	if "disabled" in inStock: 
		print datetime.datetime.now(),"NO STOCK"
	else:
		if "#ctl00_Main_mbAddToCart_modal" in inStock:
			amazonDe("sendmailRosman","HA3")
			print("OK")
		else:
			print datetime.datetime.now(),"NO STOCK"
	
while True: 
	with futures.ThreadPoolExecutor(max_workers=10) as executor:
		time.sleep(10)
		future_to_url = dict((executor.submit(load_url, url, 60), url)
				for url in URLS)
	   
