#!/usr/bin/env python

from bs4 import BeautifulSoup
import sys

file_path = sys.argv[2] 
file = sys.argv[1]

soup = BeautifulSoup(open(file), "html.parser")
with open(file_path,"w") as f:
	f.write(soup.prettify().encode('utf8'))
