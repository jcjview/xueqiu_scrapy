#!/usr/bin/python
#coding:utf8
import json
import os
import pickle

from selenium import webdriver
import  time

from xueqiu_spider.cookies import get_cookie

chromedriver = "../chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
cookies,user=get_cookie()
cookies_list=[]
for c in cookies:
    cookies_list.append(json.loads(json.dumps({'name': c, 'value': cookies[c], 'path': '/'})))
# browser = webdriver.Firefox()
browser = webdriver.Chrome(chromedriver)
# browser.get('https://xueqiu.com')
# time.sleep(3)
# cookies = browser.get_cookies()
# for c in cookies_list:
#     browser.add_cookie(c)
    # print {c:cookies[c]}
    # browser.add_cookie({'name':c,'value':cookies[c],'path':'/'})

browser.get('https://xueqiu.com')
time.sleep(30)

pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))

pageSource = browser.page_source
print pageSource
browser.close()


if __name__ == '__main__':
    pass