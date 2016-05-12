# coding: UTF-8
# filename: moniter.py

import time
import requests

url = 'http://www.amazon.co.jp/exec/obidos/ASIN/B00NNJ5B0E'
last_modified = ''
def get_page():
    global last_modified
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Connection':'keep-alive'
    }
    if last_modified:
        headers['If-Modified-Since'] = last_modified
    res = requests.get(url, headers = headers)
    print res.status_code
    print last_modified
    if res.status_code == 200:
        if last_modified and last_modified is not res.headers['Last-Modified']:
            print 'page has changed\r',
            return False
        last_modified = res.headers['Last-Modified']
    elif res.status_code == 304:
        print 'normal\r',
    return True

if __name__ == '__main__':
    while 1:
        result = get_page()
        if result:
            time.sleep(2)
        else:
            break
