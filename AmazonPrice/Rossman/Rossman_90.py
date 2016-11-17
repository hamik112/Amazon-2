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

def get_page1(opener,url,data):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

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
	cartlist = 'http://m.rossmannversand.de/DesktopModules/WebShop/mobile_shopaddtocart.aspx'
	cart = get_page(opener,cartlist,"","")
	#print cart
	tree = html.fromstring(cart)
	VIEWSTATE_SELECTOR = '//div/input[@name="__VIEWSTATE"]/@value'
	EVENTVALIDATION_SELECTOR = '//div/input[@name="__EVENTVALIDATION"]/@value'
	VIEWSTATEGENERATOR_SELECTOR = '//div/input[@name="__VIEWSTATEGENERATOR"]/@value'
	ct01 = '//div/input[@name="ctl00$Main$ShopCartPartsFremdversand$rCartProdsPart$ctl00$rCartProdsPositions$ctl00$mengenControl$hiddenProductIdWithMenge"]/@value'
	ct02 = '//div/input[@id="ctl00_Main_ShopCartPartsFremdversand_rCartProdsPart_ctl00_rCartProdsPositions_ctl00_hiddenImageUrl"]/@value'
	view = urllib.quote(tree.xpath(VIEWSTATE_SELECTOR)[0])
	event = urllib.quote(tree.xpath(EVENTVALIDATION_SELECTOR)[0])
	stat = urllib.quote(tree.xpath(VIEWSTATEGENERATOR_SELECTOR)[0])
	ct01_stat =  "359107_10"
	ct02_stat = urllib.quote(tree.xpath(ct02)[0])
	#print view
	#print event
	#print stat
	#print ct02_stat
	#addcode = 'ctl00%24scriptManager=ctl00%24Main%24updatepanel1%7Cctl00%24Main%24coupon%24Coupons%24ctl00%24btCoupon&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24DeliveryDatePicker%24DatePicker1%24DateInput=&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24hiddenImageUrl=' + ct02_stat + '&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24hiddenEnergieEffizienz=&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24mengenControl%24hiddenProductIdWithMenge=' + ct01_stat + '&ctl00%24Main%24coupon%24Coupons%24ctl00%24CouponCode=' + code + '&ctl00%24Main%24coupon%24Coupons%24ctl00%24wwwinternet=&ctl00%24Main%24wwwinternet=&__EVENTTARGET=ctl00%24Main%24coupon%24Coupons%24ctl00%24btCoupon&__EVENTARGUMENT=&__VIEWSTATE=' + view + '&__VIEWSTATEGENERATOR=' + stat + '&__EVENTVALIDATION=' + event + '&__ASYNCPOST=true&'
#	delcode = 'ctl00%24scriptManager=ctl00%24Main%24updatepanel1%7Cctl00%24Main%24coupon%24Coupons%24ctl00%24btCouponEdit&__EVENTTARGET=ctl00%24Main%24coupon%24Coupons%24ctl00%24btCouponEdit&__EVENTARGUMENT=&__VIEWSTATE=' + view + '&__VIEWSTATEGENERATOR=' + stat + '&__EVENTVALIDATION=' + event + '&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24DeliveryDatePicker%24DatePicker1%24DateInput=&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24hiddenImageUrl=' + ct02_stat + '&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24hiddenEnergieEffizienz=&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24mengenControl%24hiddenProductIdWithMenge=' + ct01_stat + '&ctl00%24Main%24coupon%24Coupons%24ctl00%24CouponCode=Gratis%20Ariel%20Waschmittel&ctl00%24Main%24coupon%24Coupons%24ctl00%24wwwinternet=&ctl00%24Main%24coupon%24Coupons%24ctl01%24CouponCode=&ctl00%24Main%24coupon%24Coupons%24ctl01%24wwwinternet=&ctl00%24Main%24wwwinternet=&__ASYNCPOST=true&'
#	delcode_url = get_page1(opener,cartlist,delcode)
	
	addcode = 'ctl00%24scriptManager=ctl00%24Main%24updatepanel1%7Cctl00%24Main%24coupon%24Coupons%24ctl01%24btCoupon&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24DeliveryDatePicker%24DatePicker1%24DateInput=&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24hiddenImageUrl=' + ct02_stat + '&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24hiddenEnergieEffizienz=&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl00%24mengenControl%24hiddenProductIdWithMenge=' + ct01_stat + '&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl01%24hiddenImageUrl=181303_1.jpg&ctl00%24Main%24ShopCartPartsFremdversand%24rCartProdsPart%24ctl00%24rCartProdsPositions%24ctl01%24hiddenEnergieEffizienz=&ctl00%24Main%24coupon%24Coupons%24ctl00%24CouponCode=Gratis%20Ariel%20Waschmittel&ctl00%24Main%24coupon%24Coupons%24ctl00%24wwwinternet=&ctl00%24Main%24coupon%24Coupons%24ctl01%24CouponCode=' + code + '&ctl00%24Main%24coupon%24Coupons%24ctl01%24wwwinternet=&ctl00%24Main%24wwwinternet=&ctl00%24Main%24wwwinternet=&__EVENTTARGET=ctl00%24Main%24coupon%24Coupons%24ctl01%24btCoupon&__EVENTARGUMENT=&__VIEWSTATE=' + view + '&__VIEWSTATEGENERATOR=' + stat + '&__EVENTVALIDATION=' + event + '&__ASYNCPOST=true&'
	addcode_url = get_page1(opener,cartlist,addcode)
	tree1 = html.fromstring(addcode_url)
	stat_line = '//div/div[@id="ctl00_Main_coupon_Coupons_ctl02_pCouponError"]'
	stat_line_str = tree1.xpath(stat_line)[0].text
	print stat_line_str
	if "Dieser Gutschein ist leider nicht mit anderen Gutscheinen kombinierbar." in stat_line_str:
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


#br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
#br.set_debug_http(True) 
#br.set_debug_redirects(True) 
#br.set_debug_responses(True)


br.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]  
sign_in = br.open('https://m.rossmannversand.de/DesktopModules/WebShop/mobile_shoplogin.aspx')
formcount=0
for frm in br.forms():  
  if str(frm.attrs["id"])=="aspnetForm":
    break
  formcount=formcount+1
br.select_form(nr=formcount)

br["ctl00$Main$tbMail"] = 'zhuhuijunzhj@gmail.com'
br["ctl00$Main$tbPassword"] = '564549024Zmm'
logged_in = br.submit() 

#items = br.open('http://m.rossmannversand.de/produkt/359107/aptamil-pronutra-pre-anfangsmilch.aspx')

cj1=urllib2.HTTPCookieProcessor(cj)
opener=urllib2.build_opener(cj1)

carturl = 'http://m.rossmannversand.de/DesktopModules/WebShop/Cart.aspx/AddItemToCart'
cartreferer = 'http://m.rossmannversand.de/produkt/359107/aptamil-pronutra-pre-anfangsmilch.aspx'

#getratingurl = 'http://m.rossmannversand.de/WebService/Mobile_WebService.asmx/GetRatingItems'
#getratingdata = "{'pageNumber':'0', 'catalogId':'359107'}"
#
#minicart = get_page3(opener,getratingurl,getratingdata,cartreferer)

addcartdata = "{'catalogid':'359107', 'qty':'10'}"
addcart = get_page3(opener,carturl,addcartdata,cartreferer)

code_init = int(sys.argv[1])
code_num = sys.argv[2]
#code_init = 9022842
while True:
	code_str = 'AY2924'
	code_init = code_init + 1
	code = code_str + str(code_num) + str(code_init)
	check_code(code)
