# coding=utf-8
import re
import urllib,urllib2,httplib,cookielib,os,sys,time
import sys
import mechanize
import cookielib
import sys, bs4
from lxml import html
sys.modules['BeautifulSoup'] = bs4
from lxml.html.soupparser import fromstring


def get_page(opener,url,data={},referer={}):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
		'Referer': referer
		}

	postdata=urllib.quote(data)
	if postdata:
		#print(postdata)
		request=urllib2.Request(url,postdata,headers=headers)
	else:
		request=urllib2.Request(url,headers=headers)
	f = opener.open(request)
	content = f.read()
	#log(content,url);
	return content

def get_page3(opener,url,data={},referer={}):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
		'Referer': referer, 
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

def get_page1(opener,url,data={},referer={}):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
		'Referer': referer}

    if data:
	#print(data)
        request=urllib2.Request(url,data,headers=headers)
    else:
        request=urllib2.Request(url,headers=headers)
    f = opener.open(request)
    content = f.read()
    #log(content,url);
    return content
br = mechanize.Browser()
#cookie_file = sys.argv[1]
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

def check_code(code):
	cartlist = 'https://einkaufsportal.rossmann.de/DesktopModules/WebShop/shopaddtocart.aspx'
	cart = get_page(opener,cartlist,"","")
	#print cart
	tree = html.fromstring(cart)
	VIEWSTATE_SELECTOR = '//div/input[@name="__VIEWSTATE"]/@value'
	PREVIOUSPAGE_SELECTOR = '//div/input[@name="__PREVIOUSPAGE"]/@value'
	VIEWSTATEGENERATOR_SELECTOR = '//div/input[@name="__VIEWSTATEGENERATOR"]/@value'
	ct01 = '//div/input[@name="ctl00$Main$ShopCartPartsFremdversand$rCartProdsPart$ctl00$rCartProdsPositions$ctl00$mengenControl$hiddenProductIdWithMenge"]/@value'
	ct02 = '//div/input[@id="ctl00_Main_ShopCartPartsFremdversand_rCartProdsPart_ctl00_rCartProdsPositions_ctl00_hiddenImageUrl"]/@value'
	view = urllib.quote(tree.xpath(VIEWSTATE_SELECTOR)[0])
	prev = urllib.quote(tree.xpath(PREVIOUSPAGE_SELECTOR)[0])
	stat = urllib.quote(tree.xpath(VIEWSTATEGENERATOR_SELECTOR)[0])
	#print view
	#print prev 
	#print stat
	
	cartlist1 = 'https://einkaufsportal.rossmann.de/DesktopModules/WebShop/shopaddtocart.aspx?Lang=de-DE'	
	addcode = 'ctl00%24ScriptManager1=ctl00%24Main%24updatepanel1%7Cctl00%24Main%24Coupons%24ctl00%24btCoupon&ctl00_ScriptManager1_HiddenField=&ctl00%24Main%24ArtnrDirekt%24box=&ctl00%24Main%24qcArtNrAmount%24mengenFeld=1&ctl00%24Main%24qcArtNrAmount%24hiddenProductIdWithMenge=&ctl00%24Main%24ShopCartPartsNormal%24ShopCartParts%24ctl00%24ShopCartPositions%24ctl00%24Menge%24mengenFeld=12&ctl00%24Main%24ShopCartPartsNormal%24ShopCartParts%24ctl00%24ShopCartPositions%24ctl00%24Menge%24hiddenProductIdWithMenge=&ctl00%24Main%24ShopCartPartsNormal%24ShopCartParts%24ctl00%24ShopCartPositions%24ctl01%24Menge%24mengenFeld=10&ctl00%24Main%24ShopCartPartsNormal%24ShopCartParts%24ctl00%24ShopCartPositions%24ctl01%24Menge%24hiddenProductIdWithMenge=&ctl00%24Main%24Coupons%24ctl00%24CouponCode%24box=' + code + '&ctl00%24Main%24LoginBox%24dfEmail%24box=yefktxubl27067%40163.com&ctl00%24Main%24LoginBox%24dfPassword%24box=564549024Zmm&__EVENTTARGET=ctl00%24Main%24Coupons%24ctl00%24btCoupon&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=' + view + '&__VIEWSTATEGENERATOR=' + stat + '&__PREVIOUSPAGE=' + prev + '&__ASYNCPOST=true&'
	addcode_url = get_page1(opener,cartlist1,addcode,cartlist)
	tree1 = html.fromstring(addcode_url)
	#stat_line = '//div/div[@id="ctl00_Main_coupon_Coupons_ctl00_pCouponError"]'
	#stat_line = '//div/div[@class="alert alert-danger alert-sm small"]'
	#stat_line_str = tree1.xpath(stat_line)[0].text
	#print stat_line_str
	if "Dieser Gutschein kann nur von Neukunden benutzt werden." in addcode_url:
		print code,"OK"
		datapath = 'NO_TRAN_OK'
		if os.path.exists(datapath):
			print "File ok"
		else:
			os.mknod(datapath)
		local2 = open(datapath, 'a+')
		local2.write(code)
		local2.write('\n')
		local2.close()
	else:
		print code,"FUCK"


br.set_handle_equiv(True) 
br.set_handle_gzip(True) 
br.set_handle_redirect(True) 
br.set_handle_referer(True) 
br.set_handle_robots(False) 


br.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]  
#sign_in = br.open('https://m.rossmannversand.de/DesktopModules/WebShop/mobile_shoplogin.aspx')
sign_in = br.open('https://www.rossmann.de/einkaufsportal/mein-konto/login')
formcount=0
for frm in br.forms():  
  if str(frm.attrs["class"])=="c-form--account-login":
    break
  formcount=formcount+1
br.select_form(nr=formcount)

br["username"] = 'zhuhuijunzhj@gmail.com'
br["password"] = '564549024Zmm'
logged_in = br.submit() 

#items = br.open('http://m.rossmannversand.de/produkt/359107/aptamil-pronutra-pre-anfangsmilch.aspx')

cj1=urllib2.HTTPCookieProcessor(cj)
opener=urllib2.build_opener(cj1)

carturl = 'https://einkaufsportal.rossmann.de/api/Cart'
cartreferer = 'https://www.rossmann.de/produkte/aptamil/pronutra-folgemilch-2/4008976022336.html'

#getratingurl = 'http://m.rossmannversand.de/WebService/Mobile_WebService.asmx/GetRatingItems'
#getratingdata = "{'pageNumber':'0', 'catalogId':'359107'}"
#
#minicart = get_page3(opener,getratingurl,getratingdata,cartreferer)

addcartdata = "{'id':'4008976022336','quantity':12}" 
addcart = get_page3(opener,carturl,addcartdata,cartreferer)


code_init = int(sys.argv[1])
#code_init = 9022842

# File: readline-example-1.py
 
#file = open("nocode")
# 
while 1:
    #lines = file.readlines(100000)
    #if not lines:
    #    break
    #for line in lines:
	code_str = 'SOVERS0'
	code_end = 'A'
	code_init = code_init + 1
	code = code_str + str(code_init) + code_end
	check_code(code)
