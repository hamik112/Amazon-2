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
import json

def get_page(opener,url,data={}):
    headers = {'Connection': 'keep-alive',
        'Adf-Ads-Page-Id': '2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Adf-Rich-Message': 'true',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate'
        }

    headers = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; "
            + ".NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; "
            + "InfoPath.2; .NET4.0E)"}
    #print data;
    postdata=urllib.urlencode(data)
    if postdata:
        request=urllib2.Request(url,postdata,headers=headers)
    else:
        request=urllib2.Request(url,headers=headers)
    f = opener.open(request)
    content = f.read()
    #log(content,url);
    return content
 
#URLS = ['http://www.amazon.de/dp/B00BSNACII',
#	'http://www.amazon.de/dp/B00BSNACII',
#	'http://www.amazon.de/dp/B00BSNACII',
#	'http://www.amazon.de/dp/B00D8V09FE',
#        'http://www.amazon.de/dp/B004X0XALE']
URLS = ['http://d3l3lkinz3f56t.cloudfront.net/aan/de?Operation=GetDecoratedOffers&asins=B01DK14I6W&attributes=customerReviewSummary,itemTitle&marketplaceId=A1PA6795UKMFR9&token=CE3761E7E32448021808867B519D0E22C2360BFB&ContentType=JSON&JSONCallBack=serviceCallback',
        'http://d3l3lkinz3f56t.cloudfront.net/aan/de?Operation=GetDecoratedOffers&asins=B00ZPVFYFU&attributes=customerReviewSummary,itemTitle&marketplaceId=A1PA6795UKMFR9&token=57BC59C2C8A3EC48598CEDD5C2FF0973EB0A2906&ContentType=JSON&JSONCallBack=serviceCallback']
 
def load_url(url, timeout):
	XPATH_SELECTOR = '//span[@id="priceblock_ourprice"]'
	SLEEP_INTERVAL = 1
	cookiejar=cookielib.CookieJar()
	cj=urllib2.HTTPCookieProcessor(cookiejar)
	opener=urllib2.build_opener(cj)
	price = get_page(opener,url)
	tmp = price.split('(')[1].split(')')[0]
	pricejson = json.loads(tmp)
	asin = pricejson[u'GetDecoratedOffersResponse'][u'GetDecoratedOffersResult'][u'offers'][0][u'asin']
	price1 = pricejson[u'GetDecoratedOffersResponse'][u'GetDecoratedOffersResult'][u'offers'][0][u'buyingPrice']
	time = datetime.datetime.now()
	print "%s\t%s\t%s"%(time,asin,price1)

#	tree = html.fromstring(price)
#	price1 = float(tree.xpath(XPATH_SELECTOR)[0].text[3:].replace(',','.'))
#	print datetime.datetime.now(),price1
while True: 
	with futures.ThreadPoolExecutor(max_workers=2) as executor:
	    future_to_url = dict((executor.submit(load_url, url, 60), url)
				 for url in URLS)
