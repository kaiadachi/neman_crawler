import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import neimanmarcusClass


if __name__ == '__main__':
	print("start")
	neimanmarcus = neimanmarcusClass.Neimanmarcus

	url = "https://www.neimanmarcus.com/en-jp/Womens-Clothing/cat000001/c.cat?navpath=cat000000_cat000001"

	if(False):
		catList, catUrlList = neimanmarcus.getCategory(url)
		for cat, url in zip(catList, catUrlList):
			print(cat)
			print(url)

	url = "https://www.neimanmarcus.com/en-jp/Clothing/Coats-Jackets/cat44700742_cat58290731_cat000001/c.cat?navpath=cat000000_cat000001_cat58290731_cat44700742"
	if(False):
		dataItem = neimanmarcus.getItem(url)
		print(dataItem["name"])
		print(dataItem["url"])

	url = "https://www.neimanmarcus.com/en-jp/Rebecca-Minkoff-Blythe-Leather-Belt-Bag-Fanny-Pack-Belt-Bags/prod210200052_cat67650739__/p.prod?icid=&searchType=EndecaDrivenCat&rte=%252Fcategory.jsp%253FitemId%253Dcat67650739%2526pageSize%253D30%2526No%253D0%2526refinements%253D&eItemId=prod210200052&xbcpath=cat000000_cat13030735_cat46860739_cat67650739&cmCat=product"
	if(False):
		info = neimanmarcus.getInfo(url, False)
		#print(len(info["color"]))
		print(type(info["stock"]))
		print(info["stock"])

	url = "https://www.neimanmarcus.com/en-jp/Rickie-Freeman-for-Teri-Jon-Beaded-Lace-Tulle-Gown-Dresses/prod197360061_cat43810733__/p.prod?icid=&searchType=EndecaDrivenCat&rte=%252Fcategory.jsp%253FitemId%253Dcat43810733%2526pageSize%253D30%2526No%253D0%2526refinements%253D&eItemId=prod197360061&xbcpath=cat000000_cat000001_cat58290731_cat43810733&cmCat=product"
	if(True):
		time.sleep(3)
		driver = neimanmarcus.getDriver()
		time.sleep(3)
		info = neimanmarcus.getInfoBySelenium(url, True, driver)		

	if(False):
		topics, topicsUrl = neimanmarcus.getTopics()
		for top, url in zip(topics, topicsUrl):
			print('topic:{}'.format(top))
			print('url  :{}'.format(url))