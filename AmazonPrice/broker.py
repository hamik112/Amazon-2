#!/usr/bin/env python
import socket, traceback ,base64, logging, netifaces
import os,sys,string,psutil,re,time,datetime,json
from xml.dom.minidom import parse, parseString
from pyDes import *
import threading

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

def asinsearch(processName):
	pids = psutil.pids()
        a = 1
	asinlist = []
        for pid in pids:
                p = psutil.Process(pid)
                if p.name() == processName:
                        a = list(p.cmdline())
                        if a[1] == "amazon.de":
				print a[2]
				asinlist.append(a[2])
	return asinlist

def asinnum(processName):
	pids = psutil.pids()
        a = 1
	num = 0
        for pid in pids:
                p = psutil.Process(pid)
                if p.name() == processName:
                        a = list(p.cmdline())
                        if a[1] == "amazon.de":
				num += 1
	return num

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
		if type(asinnum("python")) == int:
			hbjson = '{"cmd":"heartbeat","monitornum":"' + str(asinnum("python")) + '","ip":"' + localip + '","bindport":"9683"}'
		else:
			hbjson = '{"cmd":"heartbeat","monitornum":"0","ip":"' + localip + '","bindport":"9683"}'
		hb_json = DesEncrypt(hbjson)
		s.sendto(hb_json,(serverip,serverport))
		print hbjson 
		time.sleep(10)

def write(info,mode):
        f=file("monIPlist.txt",mode)
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
				#ip = cmdjson["ip"]
				#port = cmdjson["port"]
				print cmd,asin
				screen = 'screen'
				arg = '-dmS'
				title = 'Amazon' + asin
				m = 'python'
				t = 'amazon.de'
				cmd = "%s %s %s %s %s %s" % (screen,arg,title,m,t,asin)
				print cmd
				os.popen(cmd)
				time.sleep(2)
				monasin = asinsearch("python")
				monasinStr = ";".join(monasin)
				repose = '{"cmd":"start_mon_return","status":"OK","ip":"' + localip + '","bindport":"9683","asin":"'+ monasinStr +'"}'
				print repose
				monrepose = DesEncrypt(repose)
				s.sendto(monrepose,(serverip,serverport))
			elif cmd == "login_succ":
				print("Login success....")
			elif cmd == "updatepool":
				mode = "w"
				ipnum = len(cmdjson["ippool"])
				for i in range(ipnum):
					i += 1
					ip = cmdjson["ippool"]["ip" + str(i)]
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
ip = print_ifaces_data()
num = 0
Login(serverip,serverport,ip,s)
threads = []
t1 = threading.Thread(target=heartbeat,args=(serverip,serverport,ip,s))
threads.append(t1)
t2 = threading.Thread(target=acc,args=(serverip,serverport,ip,s))
threads.append(t2)

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
