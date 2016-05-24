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
import re

def get_page(opener,url,data={}):
	user_agent_list = [\
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
	"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
	]
	ua = random.choice(user_agent_list)
	headers = {'Connection': 'keep-alive',
		'Adf-Ads-Page-Id': '2',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
		'Adf-Rich-Message': 'true',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept-Encoding': 'gzip, deflate'
		}

	headers = {'User-Agent': ua 
		+ ".NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; "
		+ "InfoPath.2; .NET4.0E)"}
	postdata=urllib.urlencode(data)
	if postdata:
		request=urllib2.Request(url,postdata,headers=headers)
	else:
		request=urllib2.Request(url,headers=headers)
		f = opener.open(request)
		content = f.read()
		#log(content,url);
		return content


URLS = ['http://www.xicidaili.com/wn/1']
num = 1
def load_url(url, timeout):
	of = open('proxy.txt' , 'w')
	for page in range(1,160):
		url = 'http://www.xicidaili.com/wn/' + str(page)
		print url
		XPATH_SELECTOR = '//tr/td/text()'
		SLEEP_INTERVAL = 1
		cookiejar=cookielib.CookieJar()
		cj=urllib2.HTTPCookieProcessor(cookiejar)
		opener=urllib2.build_opener(cj)
		price = get_page(opener,url)
		soup = BeautifulSoup(price)
		trs = soup.find('table', id='ip_list').find_all('tr')
		for tr in trs[1:]:
			tds = tr.find_all('td')
			ip = tds[1].text.strip()
			port = tds[2].text.strip()
			protocol = tds[5].text.strip()
			print ip,port,protocol
			if protocol == 'HTTP' or protocol == 'HTTPS':
				of.write('%s=%s:%s\n' % (protocol, ip, port) )
				print '%s=%s:%s' % (protocol, ip, port)
	of.close()
	#tree = html.fromstring(price)
	#price1 = tree.xpath(XPATH_SELECTOR)
	#print price1
	
with futures.ThreadPoolExecutor(max_workers=10) as executor:
    num += 1
    future_to_url = dict((executor.submit(load_url, url, 60), url)
			 for url in URLS)
