import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import csv

#dri = Neimanmarcus.getDriver()
url = "https://www.neimanmarcus.com/en-jp/Kids/cat5160748/c.cat?siloId=cat5160748&navid=topNavKids&navpath=cat000000_cat5160748"
options = ChromeOptions()
options.add_argument('--headless')
dri = Chrome()
dri.get(url)
time.sleep(5)
try:
	time.sleep(5)
	dri.find_element_by_class_name('modal-close-x').click()
except:
	try:
		time.sleep(5)
		dri.find_element_by_class_name('modal-close-x').click()
	except:
		pass
time.sleep(5)
exCatList = []
exCatUrlList = []

temp = dri.find_element_by_xpath('/html/body/div[6]/div[4]/main/div[3]/ul/li[7]/h2/a')
exCat = temp.text
exCatList.append(exCat)
exCatUrl = 'https://www.neimanmarcus.com' + temp.get_attribute("href")
exCatUrlList.append(exCatUrl)

time.sleep(10)
dri.find_element_by_xpath('/html/body/div[6]/div[4]/main/div[3]/ul/li[6]/h2/a').click()

time.sleep(30)
li = dri.find_elements_by_xpath('/html/body/div[6]/div[4]/main/div[3]/ul/li[6]/ul/li/h2/a')
for i in li:
	exCat = i.text
	exCatList.append(exCat)
	exCatUrl = 'https://www.neimanmarcus.com' + i.get_attribute("href")
	exCatUrlList.append(exCatUrl)

print(exCatList)
print(exCatUrlList)