# -*- coding: utf-8 -*- 
from socket import *
from pyDes import *
import base64

Des_Key = '2UfIwSBY'

def DesEncrypt(str):
        k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(str)
        return base64.b64encode(EncryptStr)

def DesDecrypt(str):
        k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
        DecryptStr = k.decrypt(base64.b64decode(str))
        return DecryptStr


HOST ='103.236.223.152'          #主机名
PORT =  9683               #端口号 与服务器一致
BUFSIZE = 1024              #缓冲区大小1K
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)    #连接服务器

while True:                 #无限循环等待连接到来
    try:
        data = '{"cmd":"resolve_captcha","url":"http://ecx.images-amazon.com/captcha/huyzhwry/Captcha_pwwmfsmdgt.jpg"}'
	des_data = DesEncrypt(data)
        if not data:
            break
        tcpCliSock.send(des_data)            #发送数据
        data = tcpCliSock.recv(BUFSIZE)  #接受数据
        if not data:
            break
        print 'Server: ', DesDecrypt(data)
    except Exception,e:
        print 'Error: ',e
        
tcpCliSock.close()          #关闭客户端

