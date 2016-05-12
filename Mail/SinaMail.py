#! /usr/bin/python
import urllib,urllib2,httplib,cookielib,os,sys,time
import xmltodict;
import json;
from bs4 import BeautifulSoup
import re
import datetime

def log(msg,title=""):
    if title:
        print "for " + str(title) + ":\n"
    print msg + "\n==========================\n\n";

def print_cookie(ck):
    log("print the cookie")
    for value in ck:
        print value ,"\n";

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

def get_form_data(page):
    data = {}
    soup = BeautifulSoup(page)
    inputs = soup.find('form').findAll('input')
    for input in inputs:
        name = input.get('name')
        value = input.get('value')
        data[name] = value
    return data

def get_site_page(url,name,pwd):
    cookiejar=cookielib.CookieJar()
    cj=urllib2.HTTPCookieProcessor(cookiejar)
    opener=urllib2.build_opener(cj)
    #num = sys.argv[1]
    #url = url + num
    mailname = sys.argv[1]
    mailpass = sys.argv[2]
    values = {'local':mailname,'domain':'sina.com','pwd':mailpass,'remember':'1'}
    price = get_page(opener,url,values)
    
    soup = BeautifulSoup(price, "html.parser")
    p = soup.body.div.div.a
    s = str(p).split('=')[2].split('&')[0]
    
    mail = 'http://m0.mail.sina.cn/basic/listmail.php?sid='+ s +'&vt=3&fid=new'
    unread = 'http://m0.mail.sina.cn/basic/listmail.php?sid='+ s +'&vt=3&type=1&fid=all'
    maillist = get_page(opener,mail)
    soup2 = BeautifulSoup(maillist, "html.parser")
    g = soup2.body.div.form.findAll('cite')
    mailnum = len(g)
    today_time = datetime.datetime.now()
    oneday = datetime.timedelta(days=5)
    tmp = today_time - oneday
    tmp2 = datetime.datetime.strftime(tmp,'%Y-%m-%d %H:%M:%S')
    tmp3 = time.strptime(tmp2,'%Y-%m-%d %H:%M:%S')
    starttime = time.mktime(tmp3)
    for i in range(mailnum):
	maildate = ''.join(g[i])
	p = "2016-" + maildate +" 00:00:00"
	p_struct = time.strptime(p,'%Y-%m-%d %H:%M:%S')
	p_mktime = time.mktime(p_struct)
	if (p_mktime < starttime):
		return
	#g2 = soup2.body.div.findAll('p')
	#print(g2[1])
	else:
		#g2 = soup2.body.div.findAll('p')
    		g2 = soup2.p.text
		print(g2)
		print(i)
		mail2 = 'http://m0.mail.sina.cn/basic/readmail.php?sid='+ s +'&vt=3&fid=new&type=0&pageno=1&pos=' + str(i)
		mail2info = get_page(opener,mail2)
		info = re.findall(r"[0-9]{12}",mail2info)
		print(info[0])

if __name__=='__main__':
    name='zhuhuijunzhj@gmail.com'
    password='564549024Zmm'
    #time1 = bytes(int(round(time.time() * 1000)))
    #url = "http://shop.hipp.de/baby-milchnahrungen-combiotik-r30478.html"
    url = "http://mail.sina.cn/cgi-bin/sla.php?vt=3" 
    get_site_page(url,name,password)
