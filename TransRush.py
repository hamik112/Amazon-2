#! /usr/bin/python
import urllib,urllib2,httplib,cookielib,os,sys,time,json
from bs4 import BeautifulSoup
from pylsy import pylsytable

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
    
    import time
    price = get_page(opener,url)
    time1 = bytes(int(round(time.time() * 1000)))
    tmp = "http://www.transrush.com/Ajax/AjaxTransportInfo.aspx?time="+ time1 +"&actionType=3&pidx=1&psize=20&day=90&pid=&wid=&orderno="
    tmpget = get_page(opener,tmp)
    UnPaidLen_string = json.loads(tmpget)
    UnpaidLen = len(UnPaidLen_string['ResultList'])
    ResultListUrl = "http://www.transrush.com/Ajax/AjaxTransportInfo.aspx?time="+ time1 +"&actionType=4&pidx=1&psize=20&day=90&pid=&wid=&orderno="
    ResultList = get_page(opener,ResultListUrl)
    #print(ResultList)
    data_string = json.loads(ResultList)
    num = len(data_string['ResultList'])
    if (num < 1) and (UnpaidLen < 1):
    	return
    #print ""
    #print "OrderNo			DeliveryNo	OrderState		TariffPrice		ProductCode		ProductName"
    #print ""
    #attributes = ["OrderNo","DeliveryNo","OrderState","TariffPrice","ProductCode","ProductName"]
    print(urllib.unquote(name))
    attributes = ["OrderNo","DeliveryNo","OrderState","TariffPrice","ProductCode","CatagoryName"]
    table=pylsytable(attributes)

    for i in range(UnpaidLen):
    	orderNo1 = UnPaidLen_string['ResultList'][i]['OrderNo']
    	DeliveryCode1 = UnPaidLen_string['ResultList'][i]['DeliveryCode']
    	ProductCode1 = UnPaidLen_string['ResultList'][i]['ProductCode']
        OrderState1 = UnPaidLen_string['ResultList'][i]['OrderState']
        orderInfoUrl1 = "http://www.transrush.com/ajax/AjaxTransportInfo.aspx?actionType=6&orderno="+ orderNo1 +"&ordertypeflag=3&time="+ time1
        orderInfo1 = get_page(opener,orderInfoUrl1)
        order_string1 = json.loads(orderInfo1)
        tariff1 = order_string1['TariffPrice']
        CatagoryName1 = order_string1['ProductList'][0]['CatagoryName']
        table.append_data("OrderNo",orderNo1)
        table.append_data("DeliveryNo",DeliveryCode1)
        table.append_data("OrderState",OrderState1)
        table.append_data("TariffPrice",tariff1)
        table.append_data("ProductCode",ProductCode1)
        table.append_data("CatagoryName",CatagoryName1)
    print(table.__str__())

    if (num < 1):
	return
    for i in range(num):
    	orderNo = data_string['ResultList'][i]['OrderNo']
    	DeliveryCode = data_string['ResultList'][i]['DeliveryCode']
    	ProductCode = data_string['ResultList'][i]['ProductCode']
	OrderState = data_string['ResultList'][i]['OrderState']
	orderInfoUrl = "http://www.transrush.com/ajax/AjaxTransportInfo.aspx?actionType=6&orderno="+ orderNo +"&ordertypeflag=3&time="+ time1
	orderInfo = get_page(opener,orderInfoUrl)
	#print(orderInfo)
	order_string = json.loads(orderInfo)
	tariff = order_string['TariffPrice']
	CatagoryName = order_string['ProductList'][0]['CatagoryName']
	#print "%s		%s	%s			%s			%s			%s"%(orderNo,DeliveryCode,OrderState,tariff,ProductCode,ProductName)
	table.append_data("OrderNo",orderNo)
	table.append_data("DeliveryNo",DeliveryCode)
	table.append_data("OrderState",OrderState)
	table.append_data("TariffPrice",tariff)
	table.append_data("ProductCode",ProductCode)
	table.append_data("CatagoryName",CatagoryName)
    print(table.__str__())	
	
    #url2 = "http://www.transrush.com/ajax/AjaxTransportInfo.aspx?actionType=21&userId=0&time="+ time1
    #price2 = get_page(opener,url2)
    #print(price2)


if __name__=='__main__':
    #name = sys.argv[1]
    #password = sys.argv[2]
    file = open("tracc")
    while 1:
    	line = file.readline()
	if not line:
       		break
	name = line.split(',')[0]
	password = line.split(',')[1].split('\n')[0]
	name = urllib.quote(name)
    	password = urllib.quote(password)
    	import time
	time = bytes(int(round(time.time() * 1000)))
    	url = "http://passport.transrush.com/AjaxPassport.aspx?time="+ time +"&actionType=0&pwd="+ password +"&email="+ name +"&isRememberPwd=false&ref="
	get_site_page(url,name,password)
