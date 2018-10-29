import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import subprocess
import os
import json,csv,time
import tool
from convert import *
import glob
from toolReplace import *


class MyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()
		self.show()


	def makeObj(self, layout, boxName):
		cb = QCheckBox(boxName, self)
		layout.addWidget(cb)

		return cb


	def setObjs(self, layout, names):
		name = {}
		for i,n in enumerate(names):
			name[i] = self.makeObj(layout, n)

		return name

	def setWidget(self, li):
		layout = QVBoxLayout()
		cbs = self.setObjs(layout, li)

		self.topicList.append(li)
		self.cbList.append(cbs)
		self.layoutList.append(layout)

		return cbs, layout


	def addlist(self, name_cb, names):
		li = []
		if(name_cb[0].isChecked()):
			for i in range(1, len(name_cb)):
				if(name_cb[i].isChecked()):
					li.append(names[i])

			return 1, li

		else:
			return 0, li


	def getConvert(self):
		files = glob.glob("../nm_origin_csv/*.csv")
		funcList = [ amazon_fa, amazon_out, our_clo, wow_item, wow_stock ]
		for i,func in enumerate(funcList):
			if(self.convert_cb[i].isChecked()):
				for file in files:
					n = os.path.basename(file)
					print(func,n)
					func(n)


	def goReplacemant(self):
		headers = []
		pathReplceList = []
		for i,func in enumerate(self.replaceList):
			if(self.replace_cb[i].isChecked()):
				headers.append(self.replaceList[i])
				path = 'replace/{}.csv'.format(self.replaceList[i])
				pathReplceList.append(path)

		csvPathList = glob.glob("{}/*.csv".format("../nm_origin_csv"))
		runCsvList(csvPathList, pathReplceList, headers)


	def runScript(self):
		if(self.img_cb.isChecked()):
			isImage = 1
		else:
			isImage = 0

		LimitPage = self.limitPageBox.text()
		LimitItem = self.limitItemBox.text()
		cmd = "python main.py {0} {1} {2}".format(isImage, LimitPage, LimitItem)
		print(cmd)
		process = subprocess.run(cmd.split())

		return process.returncode


	def runScrape(self):
		if(len(self.cbList) != len(self.topicList)):
			sys.exit()

		tool.removeFiles("target")
		tool.makeDir("target")

		checkTopics = []
		for cb, top in zip(self.cbList, self.topicList):
			isCheck, li = self.addlist(cb, top)
			print(top[0])
			print(li)

			if(isCheck):
				checkTopics.append(top[0])

			with open('target/target_{}.csv'.format(top[0]), mode='w') as f:
				f.write('\n'.join(li))

		with open('target/targetTopics.csv', mode='w') as f:
				f.write('\n'.join(checkTopics))

		if( self.runScript() ):
			print("ERROR mian.py")
		else:
			print("Successful main.py")

		## Replace
		self.goReplacemant()

		## 整形を行う
		tool.makeDir("../created_csv")
		self.getConvert()

		print("<< Finish >>")


	def setOption(self):
		self.optLayout = QHBoxLayout()
		self.optLayout.addSpacing(30)
		# exe btn
		self.exe_btn = QPushButton('実行')
		self.exe_btn.clicked.connect(self.runScrape)
		self.optLayout.addWidget(self.exe_btn)
		self.optLayout.addSpacing(30)
		# image cb
		self.img_cb = QCheckBox('画像保存')
		self.optLayout.addWidget(self.img_cb)
		self.optLayout.addSpacing(30)
		# Limit Page
		self.limitPageLabel = QLabel('ページ制限')
		self.limitPageBox = QLineEdit()
		self.limitPageBox.setText("1")
		self.optLayout.addWidget(self.limitPageLabel)
		self.optLayout.addWidget(self.limitPageBox)
		self.optLayout.addSpacing(30)
		# Limit item
		self.limitItemLabel = QLabel('商品制限')
		self.limitItemBox = QLineEdit()
		self.limitItemBox.setText("120")
		self.optLayout.addWidget(self.limitItemLabel)
		self.optLayout.addWidget(self.limitItemBox)
		self.optLayout.addSpacing(350)


	def setFlag(self, flagList):
		flagLayout = QHBoxLayout()
		return self.setObjs(flagLayout, flagList), flagLayout

	
	def init_ui(self):
		self.setWindowTitle('Neimanmarcus')
		self.setGeometry(500, 200, 600, 500)

		itemLayout = QHBoxLayout()
		main = QVBoxLayout()

		# setting option
		self.setOption()

		## settting convert
		convertList = [ "amazon_fa", "amazon_out", "our_clothes", "wowma_item", "wowma_stock" ]
		self.convert_cb, convertLayout = self.setFlag(convertList)

		## setting replace
		self.replaceList = [ "name", "maker", "price", "size", "color" ]
		self.replace_cb, replaceLayout = self.setFlag(self.replaceList)


		# def List 
		self.cbList = []
		self.topicList = []
		self.layoutList = []

		# woman -------------------------------------------------------------
		WomanList = tool.readcsv("./gui_header/women.csv")
		self.Woman_cb, self.WomenLayout = self.setWidget(WomanList)

		# Shoes -------------------------------------------------------------
		shoesList = tool.readcsv("./gui_header/shoes.csv")
		self.Shoes_cb, self.ShoesLayout = self.setWidget(shoesList)

		# Handbags ----------------------------------------------------------
		HandbagsList = tool.readcsv("./gui_header/handbags.csv")
		self.Handbags_cb, self.HandbagsLayout = self.setWidget(HandbagsList)

		# Jewelry&Accessories------------------------------------------------
		jandA = tool.readcsv("./gui_header/jewelry&accessories.csv")
		self.jandA_cb, self.jandALayout = self.setWidget(jandA)

		# Men ---------------------------------------------------------------
		ManList = tool.readcsv("./gui_header/men.csv")
		self.Man_cb, self.MenLayout = self.setWidget(ManList)

		# Kids --------------------------------------------------------------
		KidsList = tool.readcsv("./gui_header/kids.csv")
		self.Kids_cb, self.KidsLayout = self.setWidget(KidsList)


		# main
		for l in self.layoutList:
			itemLayout.addLayout(l)

		main.addLayout(self.optLayout)
		main.addLayout(convertLayout)
		main.addLayout(replaceLayout)
		main.addLayout(itemLayout)
		self.setLayout(main)

    
if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = MyWidget()

	sys.exit(app.exec_())