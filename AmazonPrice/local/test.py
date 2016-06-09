#coding=gbk
import urllib
import time
import string
import ctypes
from ctypes import * 

dll = ctypes.windll.LoadLibrary('AntiVC.dll')
#dll.UseUnicodeString(True)
CdsIndex = dll.LoadCdsFromFile('B196.cds','AvXv5d5,mb5fx4')
print CdsIndex
if(CdsIndex == -1):
	print('LoadCds Fail!')
else:

	Str = create_string_buffer(20)
	if(dll.GetVcodeFromFile(CdsIndex,'Captcha_2.jpg',Str)):
		print('GetVcode Success:',Str.raw.decode("utf-8"))
	else:
                print('GetVcode Fail!')
