import pandas as pd
import sys
import glob


def getReplace(org, key, before, after):
	org[key] = org[key].str.replace(before, after)
	return org

def replacePrice(org, key, down, up, a, b):
	org.loc[(org[key]<up)&(org[key]>=down), key] = org.loc[(org[key]<up)&(org[key]>=down),key] * a + b
	return org

def readReplace(path_org, path_replce, key):
	orgData = pd.read_csv(path_org, encoding='Shift-JIS', index_col=0)
	with open(path_replce, 'r', encoding='Shift-JIS') as f:
		for line in f:
			## remove 'Newline character'
			line = line.strip().split(',')
			print(len(line), line)
			if(key != "price"):
				if( len(line) == 2):
					## Before conversion and After conversion
					before = line[0]
					#after = '{0}({1})'.format(line[0], line[1])
					after = line[1]

					newData = getReplace(orgData, key, before, after)
					## Overwrite mode
					newData.to_csv(path_org, encoding='Shift-JIS')
			else:
				if( len(line) == 4):
					## down, up, a, b
					newData = replacePrice( orgData, key, int(line[0]), int(line[1]), int(line[2]), int(line[3]) )
					## Overwrite mode
					newData.to_csv(path_org, encoding='Shift-JIS')


def runHeader(path_org, pathReplceList, headers):
	for head, path_replce in zip(headers, pathReplceList):
		readReplace(path_org, path_replce, head)

def runCsvList(csvPathList, pathReplceList, headers):
	if( len(pathReplceList) == len(headers) ):
		for csvPath in csvPathList:
			runHeader(csvPath, pathReplceList, headers)
	else:
		sys.exit()


if __name__ == '__main__':
	headers = ['name','price']
	csvPathList = ["180710Women'sClothing_Activewear.csv"]
	pathReplceList = ['replace/name.csv', 'replace/price.csv']
	runCsvList(csvPathList, pathReplceList, headers)