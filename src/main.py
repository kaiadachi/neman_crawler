import neimanmarcusClass
import time
import re
import pandas as pd
import os
import sys
import tool
from datetime import datetime

def makeDir(name):
	if( os.path.exists(name) ):
		print("exists [{}]".format(name))
	else:
		os.mkdir(name)


def checkList(names ,urls, fname):
	try:
		target = pd.read_csv(fname, header=None)

		newNames = []
		newUrls = []
		for n,u in zip(names, urls):
			t = target[target == n].dropna(how='all', axis=1)
			if not(t.empty):
				newNames.append(n)
				newUrls.append(u)

		return newNames, newUrls

	except:
		fname = "ErrorLog.txt"
		getErrorMag("None", "None", "None", "checkList", fname)
		sys.exit()


def getErrorMag(top, cat, url, nn, name):
	import traceback
	print("ERROR [{0}]->{1}->{2}".format(nn, top, cat))
	print("URL : {}".format(url))
	mag = "ERROR [{0}]->{1}->{2} \nURL : {2} \n".format(nn, top, url)
	error = traceback.format_exc()
	tool.writeLog(name, mag + error + "\n")


def check_Kids(top, cats):
	if(top == "Kids"):
		name = [ "girls", "boys", "baby"]
		ndict = {"girls":4, "boys":4, "baby":6}
		start = 0
		for n in name:
			for i in range(start, start + ndict[n]):
				cats[i] = n + "_" + cats[i] 
				start = i
			start = start + 1 
		return 1, cats
	else:
		return 0, []


def getGender(top, cat):
	men = "Men"
	kids = "Kids"
	name_kids = ["girls", "boys", "baby"]
	women = "Women"

	if( men in top ):
		return men

	elif( kids in top ):
		for n in name_kids:
			if( n in cat ):
				return n
				
	else:
		return women


def runCategory(tops, urls, driver, isImgSave, limitPage, isLimit):
	for top, url in zip(tops, urls):
		try:
			print("Topic:{}".format(top))
			catList, catUrlList = neimanmarcus.getCategory(url, top)
			isKids, cats_temp = check_Kids(top, catList)
			if(isKids):
				catList = cats_temp
			catList, catUrlList = checkList(catList, catUrlList, "./target/target_{}.csv".format(top))
			runItem(catList, catUrlList, driver, top, isImgSave, limitPage, isLimit)
			print("---------------------")
			time.sleep(weitTime)
		except:
			fname = "ErrorLog.txt"
			getErrorMag(top, "None", url, "runCategory", fname)


def runItem(cats, urls, driver, top, isImgSave, limitPage, isLimit):
	print("[cat]:{}".format(len(urls)))
	if(len(urls) != 0):
		for cat, url in zip(cats, urls):
			try:
				col = ["name", "maker", "code", "price", "sale", "color", "size", "stock", "gender", "image00", "image01", "image02", "image03", "image04", "image05", "image06", "image07", "image08"]
				dataInfo = data = pd.DataFrame(columns = col)
				dataItem, driver = neimanmarcus.getItem(url, driver, limitPage)
				time.sleep(weitTime)
				driver = runInfo(dataItem["url"], dataInfo, cat, driver, top, isImgSave, isLimit)
				time.sleep(weitTime)
				cat = cat.replace(" ", "")
				date = datetime.now().strftime('%y%m%d')
				#saveName = './' + top + '/' + str(cat) + '.csv'
				saveName = '../nm_origin_csv/{0}{1}_{2}.csv'.format(date, top,cat)
				dataInfo.to_csv(saveName)
			except:
				fname = "ErrorLog.txt"
				getErrorMag(top, cat, url, "runItem", fname)


def runInfo(urls, dataInfo, cat, driver, top, isImgSave, isLimit):
	if(isLimit and isLimit < len(urls)):
		tempUrl = urls
		urls = []
		for i in range(isLimit):
			urls.append(tempUrl[i])
		print("[item] {} / {}".format(len(urls), len(tempUrl)))

	gender = getGender(top, cat)

	#isImgSave = False #True
	print("[item]:{}".format(len(urls)))
	count = 0
	for i, u in enumerate(urls):
		try:
			print("[URL]{}".format(u))
			driver.get(u)
			try:
				time.sleep(2)
				info = neimanmarcus.getInfoBySelenium(u, isImgSave, driver)
				print("getInfoBySelenium > OK")
			except:
				print("error, getInfoBySelenium")
				print("retry!!")
				time.sleep(3)
				info = neimanmarcus.getInfoBySelenium(u, isImgSave, driver)
				

			print("name{:04} : {}".format(i, info["name"]))
			time.sleep(weitTime)

			for color in info["color"]:
				for size in info["size"]:
					dataInfo.at["No.{}".format( int(count) ), "name"] = info["name"]
					dataInfo.at["No.{}".format( int(count) ), "maker"] = info["maker"]
					dataInfo.at["No.{}".format( int(count) ), "code"] = info["code"]
					dataInfo.at["No.{}".format( int(count) ), "price"] = info["price"]
					dataInfo.at["No.{}".format( int(count) ), "sale"] = info["sale"]
					dataInfo.at["No.{}".format( int(count) ), "color"] = color
					dataInfo.at["No.{}".format( int(count) ), "size"] = size
					dataInfo.at["No.{}".format( int(count) ), "stock"] = info["stock"]
					dataInfo.at["No.{}".format( int(count) ), "gender"] = gender

					for j, img in enumerate(info['image']):
						dataInfo.at["No.{}".format( int(count) ), "image{:02}".format(j)] = img

					count = count + 1
		except:
			fname = "ErrorInfoLog.txt"
			getErrorMag(cat, "None", u, "runInfo", fname)

	return driver


if __name__ == '__main__':
	start = time.time()

	if(len(sys.argv) < 4):
		print("Not enough arguments [{}]".format(len(sys.argv)))
		sys.exit()

	tool.removeLog()

	isImgSave = int( sys.argv[1] )
	print(type(isImgSave), isImgSave)

	limitPage = int( sys.argv[2] )
	print(type(limitPage), limitPage)

	isLimit = int( sys.argv[3] )
	print(type(isLimit), isLimit)

	weitTime = 1
	neimanmarcus = neimanmarcusClass.Neimanmarcus

	makeDir("../nm_origin_csv")
	if(isImgSave):
		makeDir("../saveImage")

	driver = neimanmarcus.getDriver()
	time.sleep(weitTime)

	topicsList, topicsUrlList = neimanmarcus.getTopics()

	topicsList, topicsUrlList = checkList(topicsList, topicsUrlList, "./target/targetTopics.csv")
	#print(topicsList)
	
	print("isImgSave = {}".format(isImgSave))
	runCategory(topicsList, topicsUrlList, driver, isImgSave, limitPage, isLimit)
	
	elapsed_time = time.time() - start
	print ("elapsed_time : {0}".format(elapsed_time/3600) + " [h]")