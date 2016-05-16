#!/usr/bin/env python
#this is the udp broadcast client
import socket, traceback ,base64
import os,sys,string,psutil,re,time,datetime,json
from xml.dom.minidom import parse, parseString

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

print "Amaozn DE Price broker Start listening..."

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

data = "Data from pc"
s.bind(("",9683))
while True:
	try:
		data,address=s.recvfrom(9683)
		deCode = base64.b64decode(data)
		if deCode == "CODESAPPEA":
			processinfo("python")
			repose = '{"cmd":"stopedmon"}'
			baserepose = base64.b64encode(data)
			s.sendto(baserepose,(serverip,serverport))
		else:		
			print deCode
			cmdjson = json.loads(deCode)
			cmd = cmdjson["cmd"]
			asin = cmdjson["asin"]
			ip = cmdjson["ip"]
			port = cmdjson["port"]
			print cmd,asin
			if cmd == "startmon":
				screen = 'screen'
				arg = '-dmS'
				title = 'Amazon' + asin
				m = 'python'
				t = 'amazon.de'
				cmd = "%s %s %s %s %s %s %s %s" % (screen,arg,title,m,t,ip,port,asin)
				os.popen(cmd) 
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
