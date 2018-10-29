import os
import glob

def makeDir(name):
	if( os.path.exists(name) ):
		print("exists [{}]".format(name))
	else:
		os.mkdir(name)

def removeFiles(d):
	files = glob.glob(d + "/*.csv")
	for f in files:
		os.remove(f)

def removeLog():
	files = glob.glob("*.txt")
	for f in files:
		os.remove(f)

def writeLog(n, s):
	with open(n, 'a') as f:
		f.write(s)

def readcsv(path):
	data = []
	with open(path, 'r', encoding='Shift-JIS') as f:
		for line in f:
			data.append(line.strip())

	return data
