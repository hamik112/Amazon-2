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

def get_page3(opener,url,data={},referer={}):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                'Referer': 'http://m.rossmannversand.de/produkt/359107/aptamil-pronutra-pre-anfangsmilch.aspx',
                'Content-Type': 'application/json; charset=UTF-8'
                }
        print headers
        postdata=data
        if postdata:
                #print(postdata)
                request=urllib2.Request(url,postdata,headers=headers)
        else:
                request=urllib2.Request(url,headers=headers)
        f = opener.open(request)
        content = f.read()
        #log(content,url);
        return content

def get_page(opener,url,data={},referer={},ua={}):
        if referer:
                headers = {'User-Agent': 'Opera/9.23 (Windows NT 5.1; U; zh-cn)',
                        'Referer': referer,
			'Host': 'www.rossmannversand.de',
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

def check_code(filename,productid):
        cartlist = 'http://www.rossmannversand.de/DesktopModules/WebShop/shopexd.aspx?productid=' + productid
        cart = get_page(opener,cartlist,"","")
        tree = html.fromstring(cart)
        VIEWSTATE_SELECTOR = '//div/input[@name="__VIEWSTATE"]/@value'
        VIEWSTATEGENERATOR_SELECTOR = '//div/input[@name="__VIEWSTATEGENERATOR"]/@value'
        Field = '//div/input[@name="ctl00$ctl00$SearchBoxTop$searchField"]/@value'

        view = urllib.quote(tree.xpath(VIEWSTATE_SELECTOR)[0])
        stat = urllib.quote(tree.xpath(VIEWSTATEGENERATOR_SELECTOR)[0])
        field = urllib.quote(tree.xpath(Field)[0])
	username = urllib.quote(filename)
        #print view
        #print stat
        #print field
	addurl = 'http://www.rossmannversand.de/DesktopModules/WebShop/shopexd.aspx?productid=' + productid + '&id=149819'
        addcode = 'ctl00%24ScriptManager1=ctl00%24ctl00%24MiniCart1%24updMinicar%7Cctl00_ctl00_MiniCart1_updMinicart&ctl00_ScriptManager1_HiddenField=&__EVENTTARGET=ctl00_ctl00_MiniCart1_updMinicart&__EVENTARGUMENT=&__VIEWSTATE=' + view + '&__VIEWSTATEGENERATOR=' + stat + '&ctl00%24ctl00%24SearchBoxTop%24searchField=' + field + '&ctl00%24BabyweltLeiste1%24tebBabyClubText=Ihre babywelt Mitglieds-Nr.&ctl00%24Main%24ctl60%24mengenFeld=10&ctl00%24Main%24ctl60%24hiddenProductIdWithMenge=&ctl00%24Main%24ctl95%24HiddenFieldCcode=&ctl00%24Main%24ctl95%24FeedBackModal%24HiddenFieldFeedbackid=&ctl00%24Main%24ctl95%24FeedBackModal%24HiddenFieldRatingText=0&ctl00%24Main%24ctl95%24FeedBackModal%24TextBoxBewertungstext=&ctl00%24LoginBox%24dfEmail%24box=XCLHBPNH%40outlook.com&ctl00%24LoginBox%24dfPassword%24box=564549024Zmm&ctl00%24ModalFilialSpezial%24dfFilialfinderPlzOrt%24box=&ctl00%24ModalFilialSpezial%24dfFilialfinderStrasse%24box=&__ASYNCPOST=true&'
	addcode_url = get_page1(opener,addurl,addcode,cartlist,"")
       


filename = sys.argv[1] 
productid = str(sys.argv[2])
num = str(sys.argv[3])
cookiefile = filename
#cookiefile = 'RossmanCookie/' + filename
file = open(cookiefile)
cookielines = file.readlines(100)
if cookielines:
        cookiejar=cookielib.MozillaCookieJar(cookiefile)
        cookiejar.load(cookiefile, ignore_discard=True, ignore_expires=True)
else:
        print("NULL COOKIE")
        cookiejar=cookielib.MozillaCookieJar(filename)
cj=urllib2.HTTPCookieProcessor(cookiejar)
opener=urllib2.build_opener(cj)
testurl = 'https://www.rossmannversand.de/DesktopModules/WebShop/shopcustadmin.aspx'
test = get_page(opener,testurl,"","","")
print test

carturl = 'http://www.rossmannversand.de/DesktopModules/WebShop/Cart.aspx/AddItemToCart'
cartreferer = 'http://www.rossmannversand.de/DesktopModules/WebShop/shopresultsearch.aspx?keyword=aptamil'


addcartdata = "{'catalogid' : '" + productid + "', 'qty':'" + num + "', 'isabo':'false', 'aboInterval':'0'}"
addcart = get_page3(opener,carturl,addcartdata,cartreferer)
print addcart
check_code(filename,productid)
