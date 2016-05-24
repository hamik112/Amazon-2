import cookielib
import urllib2

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib2.Request("http://www.amazon.de/dp/B00BSNACII?m=A3JWKAKR8XB7XF")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()  
