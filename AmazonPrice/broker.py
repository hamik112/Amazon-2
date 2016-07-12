#!/usr/bin/env python
import socket, traceback ,base64, logging, netifaces
import os,sys,string,psutil,re,time,datetime,json
from xml.dom.minidom import parse, parseString
from pyDes import *
import threading
import linecache
import urllib,urllib2,httplib,cookielib,os,sys,random

logging.basicConfig(level=logging.DEBUG,
	format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
	datefmt='%a, %d %b %Y %H:%M:%S',
	filename='myapp.log',
	filemode='w')

def Login(serverip,serverport,localip,s):
	loginjson = '{"cmd":"login","ip":"' + localip  + '","bindport":"9683","monitornum":"0"}'
	print loginjson
	des_json = DesEncrypt(loginjson)
	s.sendto(des_json,(serverip,serverport))
	monasindata = monasin("monasin","")
	repose = '{"cmd":"start_mon_return","status":"OK","ip":"' + localip + '","bindport":"9683","asin":"'+ str(monasindata) +'"}'
	print repose
	monrepose = DesEncrypt(repose)
	s.sendto(monrepose,(serverip,serverport))

def monasin(arg,arg2):
	t = 'amazon.sh'
	cmd = "./%s %s %s" % (t,arg,arg2)
	session = os.popen(cmd).read()
	session = session.strip('\n')
	return session

def get_page(opener,url,data={}):
        a = random.randrange(1, 9173)
        ua = linecache.getline(r'ua_list.txt', a)
        headers = {'User-Agent': ua}
        postdata=urllib.urlencode(data)
        if postdata:
                request=urllib2.Request(url,postdata,headers=headers)
        else:
                request=urllib2.Request(url,headers=headers)
                f = opener.open(request)
                content = f.read()
                #log(content,url);
                return content

#def asinsearch(processName):
#	pids = psutil.pids()
#        a = 1
#	asinlist = []
#        for pid in pids:
#                p = psutil.Process(pid)
#                if p.name() == processName:
#                        a = list(p.cmdline())
#                        if a[1] == "amazon.de":
#				print a[2]
#				asinlist.append(a[2])
#	return asinlist
#
#def asinnum(processName):
#	pids = psutil.pids()
#        a = 1
#	num = 0
#        for pid in pids:
#                p = psutil.Process(pid)
#                if p.name() == processName:
#                        a = list(p.cmdline())
#                        if a[1] == "amazon.de":
#				num += 1
#	return num

def processinfo(processName):
        pids = psutil.pids()
        a = 1
        for pid in pids:
                p = psutil.Process(pid)
                if p.name() == processName:
                        a = list(p.cmdline())
                        if a[1] == "amazon.de":
                                print a[1],pid
				p.kill()
def print_ifaces_data():
        iface_data = netifaces.ifaddresses("eth0")
        data = iface_data.get(netifaces.AF_INET)[0]
        print data
	return data.get("addr")

def DesEncrypt(str):
        k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(str)
        return base64.b64encode(EncryptStr)

def DesDecrypt(str):
        k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
        DecryptStr = k.decrypt(base64.b64decode(str))
        return DecryptStr

def getText(nodelist):
	rc = ""
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc = rc + node.data
	return rc

dom1 = parse('broker.xml')
config_element = dom1.getElementsByTagName("config")[0]
servers = config_element.getElementsByTagName("server")
for server in servers:
	serverip = getText(server.childNodes)
	print serverip

ports = config_element.getElementsByTagName("port")
for port in ports:
	serverport = int(getText(port.childNodes))
	print serverport 

des_key = config_element.getElementsByTagName("Des_Key")
for key in des_key:
        Des_Key = bytes(getText(key.childNodes))
        print Des_Key 


des_iv = config_element.getElementsByTagName("Des_IV")
for iv in des_iv:
        Des_IV = bytes(getText(iv.childNodes))
        print Des_IV

def heartbeat(serverip,serverport,localip,s):
	while True:
		num = monasin("getloginT","")
		monasindata = monasin("monasin","")
		print num
		if int(num) > 30:
			#Login(serverip,serverport,localip,s)			
			print("Login time out,please check broker.....")
		else:
			print("OK")
		monnum = monasin("monnum","")
		print monnum
		if int(monnum) > 0: 
			hbjson = '{"cmd":"heartbeat","monitornum":"' + str(monnum) + '","mon_asin_list":{"asin1":"' + monasindata  + '"},"ip":"' + localip + '","bindport":"9683"}'
		else:
			hbjson = '{"cmd":"heartbeat","monitornum":"0","mon_asin_list":{"asin1":""},"ip":"' + localip + '","bindport":"9683"}'
		hb_json = DesEncrypt(hbjson)
		s.sendto(hb_json,(serverip,serverport))
		time.sleep(2)
		#s.sendto(hb_json,(serverip,serverport))
		#time.sleep(2)
		#s.sendto(hb_json,(serverip,serverport))
		#time.sleep(2)
		print hbjson 
		time.sleep(6)


def rebuildCookie():
	while True:
		os.remove("cookie.txt")
		os.remove("cookiejp.txt")
		print("Delete cookie.txt")
		print("Delete cookiejp.txt")
		os.mknod("cookie.txt") 
		os.mknod("cookiejp.txt") 
		print("Create cookie.txt")
		print("Create cookiejp.txt")
		time.sleep(60)

def write(info,mode):
        f=file("monIPlist.txt",mode)
        f.write(info)
	f.write('\n')
        f.close()

def loginstatus(info):
	f=file("LoginStatus","a+")
	f.write(info)
	f.write('\n')
	f.close()

def acc(serverip,serverpot,localip,s):		
	while True:
		try:
			data,address=s.recvfrom(9683)
			deCode = DesDecrypt(data)
			print deCode
			cmdjson = json.loads(deCode)
			print cmdjson
			cmd = cmdjson["cmd"]
			if cmd == "CODESAPPEA":
				processinfo("python")
				repose = '{"cmd":"status_captcha","status":"F**K","ip":"' + localip + '","bindport":"9683"}'
				baserepose = DesEncrypt(repose)
				print ""
				print repose
				s.sendto(baserepose,(serverip,serverport))
			elif cmd == "start_mon":		
				asin = cmdjson["asin"]
				#areacode = cmdjson["areacode"]
				#ip = cmdjson["ip"]
				#port = cmdjson["port"]
				asinar = cmdjson["areacode"]
				print cmd,asin,asinar
				if asinar == "DE":
					price = monasin("asinpriceDE",asin)
					print(asin,price)
					#print cmd,asin,areacode
					screen = 'screen'
					arg = '-dmS'
					title = 'Amazon_' + asin + '_DE'
					m = 'python'
					t = 'amazon_list.de'
					cmd = "%s %s %s %s %s %s" % (screen,arg,title,m,t,asin)
					print cmd
					os.popen(cmd)
					time.sleep(2)
				elif asinar == "JP":
					price = monasin("asinpriceJP",asin)
					print(asin,price)
					#print cmd,asin,areacode
					screen = 'screen'
					arg = '-dmS'
					title = 'Amazon_' + asin + '_JP'
					m = 'python'
					t = 'amazon_list.jp'
					cmd = "%s %s %s %s %s %s" % (screen,arg,title,m,t,asin)
					print cmd
					os.popen(cmd)
					time.sleep(2)
				else:
					print "Amazon area is NULL......"
					return
				#monasin = asinsearch("python")
				#monasinStr = ";".join(monasin)
				monasindata = monasin("monasin","")
				repose = '{"cmd":"start_mon_return","status":"OK","ip":"' + localip + '","bindport":"9683","asin":"'+ str(monasindata) +'"}'
				print repose
				monrepose = DesEncrypt(repose)
				s.sendto(monrepose,(serverip,serverport))
			elif cmd == "login_succ":
				print("Login success....")
			elif cmd == "stop_mon":
				asin = cmdjson["asin"]
				stopmon = monasin("killasin",asin)
				repose = '{"cmd":"stop_mon_return","asin":"' + asin  + '","status":"OK"}'
                                print repose
                                monrepose = DesEncrypt(repose)
				s.sendto(monrepose,(serverip,serverport))
			elif cmd == "updatepool":
				logintime = bytes(int(round(time.time())))
				loginif = logintime + ';1'
				loginstatus(loginif)
				cookiejar=cookielib.MozillaCookieJar()
				cj=urllib2.HTTPCookieProcessor(cookiejar)
				opener=urllib2.build_opener(cj)
				url = 'http://' + cmdjson["ippool"] 
				try:
					iplist = get_page(opener,url).strip('\n').split('\n')
				except:
					traceback.print_exc()
				mode = "w"
				#ipnum = len(cmdjson["ippool"])
				ipnum = len(iplist)
				for i in range(ipnum):
					i -= 1
					#ip = cmdjson["ippool"]["ip" + str(i)]
					ip = iplist[i]
					write(ip,mode)
					mode = "a+"
			else:
				print("OK") 
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			traceback.print_exc()

print "Amaozn DE Price broker Start listening..."

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(("",9683))
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s1.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s1.bind(("",9684))
ip = (urllib.urlopen('http://ipv4.icanhazip.com/').read()).strip('\n')
num = 0
Login(serverip,serverport,ip,s)
threads = []
t1 = threading.Thread(target=heartbeat,args=(serverip,serverport,ip,s1))
threads.append(t1)
t2 = threading.Thread(target=acc,args=(serverip,serverport,ip,s))
threads.append(t2)
t3 = threading.Thread(target=rebuildCookie)
threads.append(t3)
if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True)
		t.start()
	t.join()
#heartbeat(serverip,serverport,s)
#acc(serverip,serverport,s)
#while True:
#	try:
#		data,address=s.recvfrom(9683)
#		deCode = DesDecrypt(data) 
#		print deCode
#		cmdjson = json.loads(deCode)
#		cmd = cmdjson["cmd"]
#		if cmd == "CODESAPPEA":
#			processinfo("python")
#			repose = '{"cmd":"stopedmon"}'
#			baserepose = base64.b64encode(data)
#			s.sendto(baserepose,(serverip,serverport))
#		elif cmd == "start_mon":		
#			asin = cmdjson["asin"]
#			ip = cmdjson["ip"]
#			port = cmdjson["port"]
#			print cmd,asin
#			screen = 'screen'
#			arg = '-dmS'
#			title = 'Amazon' + asin
#			m = 'python'
#			t = 'amazon.de'
#			cmd = "%s %s %s %s %s %s %s %s" % (screen,arg,title,m,t,ip,port,asin)
#			print cmd
#			os.popen(cmd)
#		elif cmd == "login_succ":
#			print("Login success....")
#		else:
#			print("OK") 
#	except (KeyboardInterrupt, SystemExit):
#		raise
#	except:
#		traceback.print_exc()
