import mechanize
import cookielib

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Open some site, let's pick a random one, the first that pops in mind:
r = br.open('https://www.amazon.de/ap/signin?_encoding=UTF8&openid.assoc_handle=anywhere_v2_de&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.de%2Fgp%2Faw%2Fpsi.html%3Fie%3DUTF8%26cartID%3D275-1876454-7334207%26destinationURL%3D%252Fgp%252Faw%252Fcustomer-reviews%252Fvote%252F3954530937%252FR77XOZNL1VVBN%252F1%253FappAction%253Dvote%2526appActionToken%253De2d603690102981ebb11a0e3b5d203fb5666bb72c2d16f99f1c6e733b275e933%2526csrfRnd%253D0.0769195250383525%2526csrfTs%253D1454819975&pageId=avl_de')

print br.response().read()

br.select_form(predicate=lambda form: form.attrs.get('value') == 'Anmelden')  
br["email"] = 'nloqbmscq139976@163.com'  #provide email
br["password"] = 'jjkcs123' #provide passowrd
logged_in = br.submit() 
