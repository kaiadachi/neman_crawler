import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import csv

class Neimanmarcus():
	def saveImg(imgurl):
		if("https:" not in imgurl):
			#imgurl = "https:" + imgurl.split("?")[0]
			imgurl = "https:" + imgurl

		re = requests.get(imgurl)

		if("https:" not in imgurl):
			ext = re.headers["content-type"].replace("image/", ".")
			imgurl = imgurl.split("?")[0] + ext

		with open("../saveImage/" + imgurl.split('/')[-1], 'wb') as f:
			f.write(re.content)


	def sentRequest(url):
		r = requests.get(url)

		if(False):
			print("header: {0}".format(r.headers))
			print("encoding: {0}".format(r.encoding))
			print("-------------")

		time.sleep(1)

		return BeautifulSoup(r.content, "html.parser")

	def writeData(a, b, name):
		with open('{0}.csv'.format(name), 'w') as f:
			writer = csv.writer(f, lineterminator='\n')
			for i,j in zip(a,b):
				writer.writerows([[i,j]])


	def getTopics(url='https://www.neimanmarcus.com/en-jp/'):
		soup = Neimanmarcus.sentRequest(url)

		topicsUrlList = []
		topicsList = []
		for i in soup.select('a.silo-link'):
		#for i in soup.select(''):
			topics = i.get_text()
			topicsUrl = 'https://www.neimanmarcus.com' + i.get("href")
			print("Topics: {0}".format(topics))
			#print("URL   : {0}".format(topicsUrl))
			topics = topics.replace(" ", "")
			topicsList.append(topics)
			topicsUrlList.append(topicsUrl)

		Neimanmarcus.writeData(topicsList, topicsUrlList, "topics")

		return topicsList, topicsUrlList

	def exceptKids(url):
		# options = ChromeOptions()
		# options.add_argument('--headless')
		# dri = Chrome()
		dri = Neimanmarcus.getDriver()
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
		try:
			temp = dri.find_element_by_xpath('/html/body/div[6]/div[4]/main/div[3]/ul/li[7]/h2/a')
			exCat = temp.text
			exCat = exCat.replace(" ", "")
			exCatList.append(exCat)
			#exCatUrl = 'https://www.neimanmarcus.com' + temp.get_attribute("href")
			exCatUrl = temp.get_attribute("href")
			exCatUrlList.append(exCatUrl)
		except:
			pass

		try:
			time.sleep(5)
			dri.find_element_by_xpath('/html/body/div[6]/div[4]/main/div[3]/ul/li[6]/h2/a').click()

			time.sleep(5)
			li = dri.find_elements_by_xpath('/html/body/div[6]/div[4]/main/div[3]/ul/li[6]/ul/li/h2/a')
			for i in li:
				exCat = i.text
				exCat = exCat.replace(" ", "")
				exCat = exCat.replace("Boys'", "boys_")
				exCat = exCat.replace("Girls'", "girls_")
				exCatList.append(exCat)
				#exCatUrl = 'https://www.neimanmarcus.com' + i.get_attribute("href")
				exCatUrl = i.get_attribute("href")
				exCatUrlList.append(exCatUrl)
		except:
			pass

		return exCatList,exCatUrlList


	def getCategory(url, topic):
		
		#取るの指定
		numdict = {"Women'sClothing":14, "Shoes":12, "Handbags":14, "Jewelry&Accessories":18, "Men":31, "Kids":16}
		if topic in numdict.keys():
			num = numdict[topic]
		else:
			num = 0

		catList = []
		catUrlList = []
		if(num == 0):
			print("Not Found key = {}...".format(topic))
		else:
			soup = Neimanmarcus.sentRequest(url)
			#for i in soup.select("ul.category-menu > li:nth-of-type(3) > ul.category-menu > li.hasChildren > h2 > a.navLastItem"):
			for i in soup.select("li.hasChildren > h2 > a.navLastItem", limit = num):
				#cat = i.get("href").split("/")
				cat = i.get_text()
				catUrl = 'https://www.neimanmarcus.com' + i.get("href")
				if(False):
					#print("Category: {0}".format(cat[3]))
					print("Category: {0}".format(cat))
					print("URL     : {0}".format(catUrl))

				cat = cat.replace("\t", "")
				cat = cat.replace(" ", "")
				cat = cat.replace("&", "-")
				cat = cat.replace(",", "-")
				cat = cat.strip()
				catList.append(cat)
				catUrlList.append(catUrl)


			if(topic == "Kids"):
				exCatList, exCatUrlList = Neimanmarcus.exceptKids(url)
				print(exCatList)
				for ii, kk in zip(exCatList, exCatUrlList):
					catList.append(ii)
					catUrlList.append(kk)


			topic = topic.replace(" ", "")
			Neimanmarcus.writeData(catList, catUrlList, "category_{0}".format(topic))

		return catList, catUrlList

	'''
	def getItem(nextUrl):
		soup = Neimanmarcus.sentRequest(nextUrl)

		#itemList = []
		itemUrlList =[]
		for i in soup.select("div.product-image-frame > #productTemplateId"):
			#item = i.get_text()
			itemUrl = 'https://www.neimanmarcus.com' + i.get("href")
			if(False):
				#print("name: {}".format(item))
				print("url : {}".format(itemUrl))
			#itemList.append(item)
			itemUrlList.append(itemUrl)

		return itemUrlList
	'''

	def getDriver():
		options = ChromeOptions()
		options.add_argument('--headless')
		driver = Chrome(options=options)
		#driver = Chrome()
		'''
		if(isHeadless):
			driver = Chrome(options=options)
		else:
			driver = Chrome()
		#url = 'https://www.neimanmarcus.com/en-jp/Clothing/Activewear/cat56820776_cat58290731_cat000001/c.cat?navpath=cat000000_cat000001_cat58290731_cat56820776'
		'''

		return driver


	def getElemants(i, data, driver):
		print("[page{}]".format(i))
		print("-------------------------------")

		#for k, a in enumerate( driver.find_elements_by_css_selector('div.productname > h2 > #colorSwatch') ):
		for k, a in enumerate( driver.find_elements_by_css_selector('#productTemplateId') ):
			#print(a.text)
			#print(a.get_attribute('href'))
			#data.at["No.{}".format( int( (i-1)*120+k ) ), "name"] = a.text
			try:
				data.at["No.{}".format( int( (i-1)*120+k ) ), "url"] = a.get_attribute('href')
			except:
				pass

		return data

	def setNextPage(driver):
		#NEXT PAGE
		try:
			time.sleep(5)
			driver.find_element_by_id('paging_next').click()
		except:
			try:
				print("error [next page], retry!")
				time.sleep(5)
				driver.find_element_by_id('paging_next').click()
			except:
				print("error [next page], retry!")
				time.sleep(5)
				driver.find_element_by_id('paging_next').click()


	def getItem(nextUrl, driver, limitPage):

		driver.get(nextUrl)
		print(nextUrl)
		#driver = Neimanmarcus.getDriver(isHeadless, nextUrl)

		try:
			time.sleep(5)
			driver.find_element_by_class_name('modal-close-x').click()
		except:
			try:
				time.sleep(5)
				driver.find_element_by_class_name('modal-close-x').click()
			except:
				pass
		#except:
		#	time.sleep(5)
		#	print("error, retry!")
		#	driver.find_element_by_class_name('modal-close-x').click()
		#driver.save_screenshot('picture0.png')

		try:
			time.sleep(5)
			driver.find_element_by_id('HundredTwentyPerPage').click()
		except:	
			try:
				print("error, retry!")
				time.sleep(10)
				driver.find_element_by_id('HundredTwentyPerPage').click()
			except:
				pass
	#driver.save_screenshot('picture00.png'
		try:
			time.sleep(5)
			driver.find_element_by_xpath('//*[@id="select-sort-by"]/option[4]').click()
		except:
			try:
				print("error, retry!")
				time.sleep(10)
				driver.find_element_by_xpath('//*[@id="select-sort-by"]/option[4]').click()
			except:
				pass
		

		time.sleep(1)
		end = driver.find_element_by_id('numItems')
		endPage = np.ceil( int(end.text)/120 )
		print( "end = {}".format(endPage) )

		data = pd.DataFrame(columns = ["name", "url"])

		try:
			data = Neimanmarcus.getElemants(1, data, driver)
		except:
			print("ERROR [{}]".format(nextUrl))
		time.sleep(2)

		if(endPage > limitPage):
			endPage = limitPage

		for i in np.arange(2, endPage+1):
			try:
				Neimanmarcus.setNextPage(driver)
			except:
				print("ERROR setNextPage")
				driver.refresh()
				print("Refresh, now")
				time.sleep(20)
				Neimanmarcus.setNextPage(driver)

			#GET ITEMS
			try:
				time.sleep(5)
				data = Neimanmarcus.getElemants(i, data, driver)
			except:
				print("error and retry")
				time.sleep(5)
				data = Neimanmarcus.getElemants(i, data, driver)

			#driver.save_screenshot('picture{0:02}.png'.format(int(i)))

		#driver.quit()
		#data.to_csv( 'data.csv' )

		return data, driver

	def getCode(url):
		s = url.split('&')
		for i in s:
			if("eItemId" in i):
				para = i.split("prod")

		return para[-1]


	def changeImgUrl(imageUrls, imgUrl):
		tempUrl = imgUrl.get_attribute("data-zoom-url")
		if("https:" not in tempUrl):
			tempUrl = tempUrl.split("?")[0]
			s =  tempUrl.split('/')[-1] + ".jpeg" 
			imageUrls.append("http://sukai9682.jp/nm_image/{0}".format(s))
		else:
			s = tempUrl.split('/')[-1]
			imageUrls.append("http://sukai9682.jp/nm_image/{0}".format(s))

		return imageUrls


	def getInfoBySelenium(url, isImgSave, driver):

		'''
		time.sleep(3)
		try:
			driver.find_element_by_class_name('modal-close-x').click()
		except:
			time.sleep(5)
			driver.find_element_by_class_name('modal-close-x').click()
		'''

		print("-------------------------------------------------------")
		

		# Get Name # Get Maker
		#name = driver.find_elements_by_css_selector('h1.product-name > span')
		try:
			name = driver.find_element_by_xpath('//*[@id="lineItemsForm"]/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/h1/span[2]').text
			print("name : {}".format(name))
			maker = driver.find_element_by_xpath('//*[@id="lineItemsForm"]/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/h1/span[1]').text
			print("maker : {}".format(maker))
		except:
			name = driver.find_element_by_xpath('//*[@id="lineItemsForm"]/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/h1/span').text
			print("name : {}".format(name))
			maker = "None"
			print("maker : {}".format(maker))
			

		# Get Price
		try:
			priceOrg = driver.find_element_by_xpath('//*[@id="lineItemsForm"]/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/span[2]').text.replace(u"\xa0",u"")
			priceNow = driver.find_element_by_xpath('//*[@id="lineItemsForm"]/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/ins/span[2]').text.replace(u"\xa0",u"")
			#price = driver.find_elements_by_css_selector('span.item-price')
			#priceOrg = price[0].text.replace(u"\xa0",u"")
			#priceNow = price[1].text.replace(u"\xa0",u"")
		except:
			try:
				priceOrg = driver.find_element_by_xpath('//*[@id="lineItemsForm"]/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/p[1]').text
				#priceOrg = driver.find_element_by_css_selector('p.product-price').text
				priceNow = "None"
			except:
				priceOrg = "Noen"
				priceNow = "Noen"

		priceOrg = priceOrg.replace(',', '')
		priceOrg = priceOrg.replace('.', '')
		priceOrg = priceOrg.replace('JPY', '')
		priceOrg = priceOrg.replace(' ', '')
		priceNow = priceNow.replace(',', '')
		priceNow = priceNow.replace('.', '')
		priceNow = priceNow.replace('JPY', '')
		priceNow = priceNow.replace(' ', '')

		print("price_org : {}".format(priceOrg))
		print("price_now : {}".format(priceNow))

		# Get Size
		sizeList = []
		for size in driver.find_elements_by_css_selector('div.sizeSelectBox > div > div.buttonValue'):
			sizeList.append(size.text)
		if(len(sizeList) == 0):
			sizeList.append("none")

		for i, s in enumerate(sizeList):
			print("Size{:02} : {}".format(i, s))

		# Get Color
		colorList = []
		for color in driver.find_elements_by_css_selector('div.colorSelectBox  > div > div.buttonValue'):
			colorList.append(color.text)
		
		if(len(colorList) == 0):
			for color in driver.find_elements_by_css_selector('img.swatch-picker'):
				colorList.append(color.get_attribute("title"))

		for i, c in enumerate(colorList):
			print("color{:02} : {}".format(i, c))

		# Get Image URL
		imgList = []
		imageUrls = []
		for imgUrl in driver.find_elements_by_css_selector('div.alt-img-wrap > img'):
			#imgList.append(imgUrl.get("src"))
			imgList.append(imgUrl.get_attribute("data-zoom-url"))
			imageUrls = Neimanmarcus.changeImgUrl(imageUrls, imgUrl)

		if(len(imgList) == 0):
			for imgUrl in driver.find_elements_by_css_selector('div.img-wrap > img'):
				#imgList.append(imgUrl.get("src"))
				imgList.append(imgUrl.get_attribute("data-zoom-url"))
				imageUrls = Neimanmarcus.changeImgUrl(imageUrls, imgUrl)

		for i, img in enumerate(imgList):
			print("image{:02} : {}".format(i, img))

		if(isImgSave):
			for url in imgList:
				try:
					Neimanmarcus.saveImg(url)
				except:
					print("NOT FOUND:{}".format(url))

		stock = 1
		code = Neimanmarcus.getCode(driver.current_url)

		gender = "None"

		dictInfo = {"name":name, "maker":maker, "code":code, "price":priceOrg,"sale":priceNow, "image":imageUrls, "color":colorList, "size":sizeList, "stock":stock, "gender":gender}

		return dictInfo

	# It is useless now
	def getInfo(url, isImgSave):
		soup = Neimanmarcus.sentRequest(url)

		try:
			name = soup.select('h1.product-name > span[itemprop="name"]')[0].get_text()
		except:
			name = "None"
			print("url:{}".format(url))


		try:
			maker = soup.select('span.product-designer > a')[0].get_text()
		except:
			maker = "None"


		try:
			priceOrg = soup.select('span.item-price')[0].get_text().replace(u"\xa0",u"")
		except:
			priceOrg = soup.select('p.product-price')[0].get_text()

		try:
			color = soup.select('img.swatch-picker')[0].get("data-color-name")
		except:
			color = ["none"]
			
		stock = 1

		imgList = []
		imageUrls = []
		for imgUrl in soup.select('div.alt-img-wrap > img'):
			#imgList.append(imgUrl.get("src"))
			imgList.append(imgUrl.get("data-zoom-url"))
			tempUrl = imgUrl.get("data-zoom-url")
			if(imgurl not in "https:"):
				tempUrl = tempUrl.split("?")[0]
				s =  tempUrl.split('/')[-1] + ".jpeg" 
				imageUrls.append("http://sukai9682.jp/nm_image/{0}".format(s))
			else:
				s = tempUrl.split('/')[-1]
				imageUrls.append("http://sukai9682.jp/nm_image/{0}".format(s))

		if(len(imgList) == 0):
			for imgUrl in soup.select('div.img-wrap > img'):
				#imgList.append(imgUrl.get("src"))
				imgList.append(imgUrl.get("data-zoom-url"))
				tempUrl = imgUrl.get("data-zoom-url")
				if(imgurl not in "https:"):
					tempUrl = tempUrl.split("?")[0]
					s =  tempUrl.split('/')[-1] + ".jpeg" 
					imageUrls.append("http://sukai9682.jp/nm_image/{0}".format(s))
				else:
					s = tempUrl.split('/')[-1]
					imageUrls.append("http://sukai9682.jp/nm_image/{0}".format(s))

		
		#print("name :{0}".format(name))
		#print("maker:{0}".format(maker))
		#print("price:{0}".format(priceOrg))
		#print(imgList)
		if( isImgSave ):
			for url in imgList:
				try:
					Neimanmarcus.saveImg(url)
				except:
					print("NOT FOUND:{}".format(url))

		dictInfo = {"name":name, "maker":maker, "price":priceOrg, "image":imageUrls, "color":color, "stock":stock}

		return dictInfo


if __name__ == '__main__':
	neimanmarcus = Neimanmarcus
	neimanmarcus.getCategory()
	neimanmarcus.getTopics()
