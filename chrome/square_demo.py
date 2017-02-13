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
browser = webdriver.Chrome(chromedriver)
# cookies = pickle.load(open("cookies.pkl", "rb"))
# browser.get('https://xueqiu.com')
# time.sleep(3)
# for cookie in cookies:
#     browser.add_cookie(cookie)
browser.get('https://xueqiu.com/ask/square')
time.sleep(3)
# pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
pages=browser.find_elements_by_xpath('//*[@id="container"]/div/div/div/div/div/div/div/p')



for p in pages:
    print p.text

# pageSource = browser.page_source
# print pageSource
browser.close()


if __name__ == '__main__':
    pass