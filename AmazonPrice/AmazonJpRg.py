# coding=utf-8
import re
import urllib,urllib2,httplib,cookielib,os,sys,time
import sys
import mechanize
import cookielib
import sys, bs4
sys.modules['BeautifulSoup'] = bs4
from lxml.html.soupparser import fromstring


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
	print(postdata)
        request=urllib2.Request(url,postdata,headers=headers)
    else:
        request=urllib2.Request(url,headers=headers)
    f = opener.open(request)
    content = f.read()
    #log(content,url);
    return content

def get_page1(opener,url,data):
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
    if data:
	print(data)
        request=urllib2.Request(url,data,headers=headers)
    else:
        request=urllib2.Request(url,headers=headers)
    f = opener.open(request)
    content = f.read()
    #log(content,url);
    return content
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)


br.set_handle_equiv(True) 
br.set_handle_gzip(True) 
br.set_handle_redirect(True) 
br.set_handle_referer(True) 
br.set_handle_robots(False) 

email = sys.argv[1]

#br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
#br.set_debug_http(True) 
#br.set_debug_redirects(True) 
#br.set_debug_responses(True)


br.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]  
sign_in = br.open('https://www.amazon.co.jp/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_ya_signin&prevRID=PD86A87YXFSRF6HGYB5G&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=jpflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

br.select_form(name="register")  
br["customerName"] = 'ghostbaby'
br["customerNamePronunciation"] = 'UNBMN'
br["email"] = email 
br["password"] = 'jjkcs123'
br["passwordCheck"] = 'jjkcs123'
logged_in = br.submit() 

#orders_html = br.open("https://www.amazon.jp/gp/css/history/orders/view.html?orderFilter=year-%s&startAtIndex=1000")
#print br.response().read()
#
#sign_in = br.open('https://www.amazon.co.jp/gp/sign-in.html')
#
#br.select_form(name="signIn")  
#br["email"] = email 
#br["password"] = 'jjkcs123'
#logged_in = br.submit() 
##print br.response().read()



one_click = br.open("https://www.amazon.co.jp/gp/css/account/address/view.html?ie=UTF8&ref_=myab_view_new_address_form&viewID=newAddress")

br.select_form(nr=1)
br["enterAddressFullName"] = 'zhuhuijun UYVIQC'
br["enterAddressPostalCode"] = '277'
br["enterAddressPostalCode2"] = '0834'
br.find_control(name="enterAddressStateOrRegion", kind="list").value = ['千葉県']
br["enterAddressAddressLine1"] = '松ヶ崎新田字水神前13-1'
br["enterAddressAddressLine2"] = 'ロジポート北柏1F104 IES CNUYVIQC'
br["enterAddressAddressLine3"] = ''
br["enterAddressPhoneNumber"] = '0471-28-9988'
one_clickcheck = br.submit()

cj1=urllib2.HTTPCookieProcessor(cj)
opener=urllib2.build_opener(cj1)

url = 'https://www.amazon.co.jp/gp/css/account/cards/view.html/ref=add_pay_meth?ie=UTF8&viewID=addCard'

url1 = get_page(opener,url)


local2 = open('tmp.xml', 'w')
local2.write(url1)
local2.close()


t = 'amazon.sh'
m = 'session'
cmd = "./%s %s" % (t,m)
session = os.popen(cmd).read()
session = session.strip('\n')

t = 'amazon.sh'
m = 'address'
cmd = "./%s %s" % (t,m)
address = os.popen(cmd).read()
address = address.strip('\n')
addressX = ""+address+".x"
addressY = ""+address+".y"
print(addressX)
print(addressY)

t = 'amazon.sh'
m = 'id'
cmd = "./%s %s" % (t,m)
id = os.popen(cmd).read()
id = id.strip('\n')
print(id)

filename = 'tmp.xml'
os.remove(filename)


values = '__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&action=add&sessionId='+ session +'&creditCardIssuer=V0&addCreditCardNumber=4024007186464797&card-name=CHENTAIZHONG&newCreditCardMonth=01&newCreditCardYear=2021&enterAddressFullName=&enterAddressPostalCode=&enterAddressPostalCode2=&enterAddressStateOrRegion=&enterAddressAddressLine1=&enterAddressAddressLine2=&enterAddressAddressLine3=&enterAddressPhoneNumber=&enterAddressCountryCode=JP&enterAddressIsDomestic=1&addressID_'+ id +'.x=77&addressID_'+ id +'.y=7'

url1 = 'https://www.amazon.co.jp/gp/css/account/cards/view.html'

price = get_page1(opener,url,values)

edit = 'https://www.amazon.co.jp/gp/css/account/address/view.html?ie=UTF8&viewID=editPaymentMethod'
editvalue = '__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&addressID='+ id +'&sessionId='+ session +'&ref_=myab_view_edit_payment_form&editPaymentMethod=%E5%A4%89%E6%9B%B4'

editdata = get_page1(opener,edit,editvalue)
local = open('tmp2.html', 'w')
local.write(editdata)
local.close()


t = 'amazon.sh'
m = 'payment'
cmd = "./%s %s" % (t,m)
payment = os.popen(cmd).read()
payment = payment.strip('\n')

addpayment = '__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&addressID='+ id +'&sessionId='+ session +'&dropdown-name=zhuhuijun+UYVIQC&action=editPaymentMethodAction&paymentMethod='+ payment +'&originalCreditCardMonth.'+ payment +'&originalCreditCardYear.'+ payment +'&creditCardMonth.'+ payment +'&creditCardYear.'+ payment +'&editPaymentMethod=%E6%AC%A1%E3%81%AB%E9%80%B2%E3%82%80&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&creditCardIssuer=V0&addCreditCardNumber=&card-name=&newCreditCardMonth=01&newCreditCardYear=2016&enterAddressFullName=&enterAddressPostalCode=&enterAddressPostalCode2=&enterAddressStateOrRegion=&enterAddressAddressLine1=&enterAddressAddressLine2=&enterAddressAddressLine3=&enterAddressPhoneNumber=&enterAddressCountryCode=JP&enterAddressIsDomestic=1'
paymenturl = 'https://www.amazon.co.jp/gp/css/account/address/view.html?ie=UTF8&viewID=editPaymentMethod'

price = get_page1(opener,paymenturl,addpayment)


turnonurl = 'https://www.amazon.jp/gp/css/account/address/view.html'

turnonValues = '__mk_de_DE=%C5M%C5%B4%D5%D1&oneClick=on&sessionId='+ session +'&ref_=myab_1_click_on'

price = get_page1(opener,turnonurl,turnonValues)

