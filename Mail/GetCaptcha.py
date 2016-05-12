#! /usr/bin/python
import urllib,urllib2,httplib,cookielib,os,sys,subprocess,pdb
from bs4 import BeautifulSoup
from subprocess import Popen, PIPE, STDOUT

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

def get_site_page():
   	CaptchaUrl = "http://login.sina.com.cn/cgi/pin.php?r=18405726&s=0&p=gz-3e95a4a60b671fe8d394a809fe4a6489bc84"
	cookiejar=cookielib.CookieJar()
    	cj=urllib2.HTTPCookieProcessor(cookiejar)
    	opener=urllib2.build_opener(cj)
	
	picture = opener.open(CaptchaUrl).read()
	local = open('test.gif', 'wb')
	local.write(picture)
	local.close()

	cmd = [ "python", \
        "yunsu.py", \
        "upload", \
        "test.gif", \
        ]
	retval = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
 	local2 = open('tmp.xml', 'w')
        local2.write(retval[0])
        local2.close()
	
	#cmd2 = [ "sh", \
        #"getCaptcha.sh", \
        #"tmp.xml", \
        #]
        #p = subprocess.Popen(cmd2,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
	#print p

	t = 'getCaptcha.sh'
	m = 'tmp.xml'
	cmd = "./%s %s" % (t,m)
	captcha = os.popen(cmd).read()
	print(captcha)	
	#url = sys.argv[1]+'&vcode=%s'%(captcha)
	#price = get_page(opener,url)
    	#print(price)


if __name__=='__main__':
    get_site_page()
