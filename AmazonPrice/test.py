#!/usr/bin/env python

import lxml
from lxml.html.clean import Cleaner

cleaner = Cleaner()
cleaner.javascript = False # This is True because we want to activate the javascript filter
cleaner.style = False      # This is True because we want to activate the styles & stylesheet filter

print "WITHOUT JAVASCRIPT & STYLES"
data = lxml.html.tostring(cleaner.clean_html(lxml.html.parse('http://www.amazon.de/gp/offer-listing/B00FF6EHI0/ref=dp_olp_new?ie=UTF8&condition=new&m=A3JWKAKR8XB7XF')))
print data
#OFFERID_SELECTOR = '//form[@method="post"]/input[@name="oid"]/@value'
#tree = lxml.html.fromstring(data)
#price = tree.xpath(OFFERID_SELECTOR)
#print price 
