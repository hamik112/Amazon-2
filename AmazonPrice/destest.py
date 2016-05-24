import base64
from pyDes import *

Des_Key = "12345678"
Des_IV = "\x22\x33\x35\x81\xBC\x38\x5A\xE7" 

def DesEncrypt(str):
	k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
	EncryptStr = k.encrypt(str)
	return base64.b64encode(EncryptStr) 

def DesDecrypt(str):
	k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
	DecryptStr = k.decrypt(str)
	return DecryptStr
	

a = DesEncrypt('{"cmd":"status_captcha","status":"OK","ip":"133.130.106.179","bindport":"9683"}')
print a
b = DesDecrypt(a)
print b 

