# coding=utf-8
from concurrent import futures
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

def get_page(opener,url,data={},referer={},ua={}):
        if referer:
                headers = {'User-Agent': ua, 
                        'Referer': referer
                }
        else:
                headers = {'User-Agent': ua 
		}
	#postdata = urllib.quote(data)
        postdata = data
        if postdata:
                request=urllib2.Request(url,postdata,headers=headers)
        else:
                request=urllib2.Request(url,headers=headers)
        f = opener.open(request)
        content = f.read()
        return content

mail = sys.argv[1] 
encode_mail = urllib.quote(mail)
time1 = bytes(int(round(time.time() * 1000))) 
a = random.randrange(1, 9173)
ua = linecache.getline(r'ua_list.txt', a)
url = 'https://oracle.padiact.com/tracker.php?nrlsk_key=446b7d43273d224900c6b9c467949ec5&action=1&segment=13876&template=11&Email%7Cemail=' + encode_mail + '&segment=13876&segment=13876&nrlsk_type=1&noCacheIE=' + time1
referer = 'https://www.feedo.cz'

filename = 'cookie'
cookiejar=cookielib.MozillaCookieJar(filename)
file = open(filename,'a+')
cookielines = file.readlines(100)
file.close()
if cookielines:
	cookiejar.load(filename, ignore_discard=True, ignore_expires=True)
else:
	print("NULL COOKIE")
	cookiejar=cookielib.MozillaCookieJar(filename)
cj=urllib2.HTTPCookieProcessor(cookiejar)
opener=urllib2.build_opener(cj)
price = get_page(opener,url,"",referer,ua)
print price
if "true" in price:
	print mail,"OK"
	datapath = 'NO_TRAN_OK'
	if os.path.exists(datapath):
		print "File ok"
	else:
		os.mknod(datapath)
	local2 = open(datapath, 'a+')
	local2.write(mail)
	local2.write('\n')
	local2.close()
