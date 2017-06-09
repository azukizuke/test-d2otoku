import const

def initListJson(fromJson,key):
	tempList=[]
	for json in fromJson:
		tempList.append(json[key])
	return tempList

def addAttributeCounter(arglist,counter,key):
	if key in arglist[counter]:
		arglist[counter][key]+=1
	else:
		arglist[counter][key]=1

	return arglist

#二次元配列への操作。転写っぽいことしてます。
def addAttributeTrancepose(fromList,toList):
	for valList in fromList:
		i = 0
		if isinstance(valList,type(None)) == False:
			for val in valList:
				toList[i].append(val)
				i+=1
	return toList


def addXpTimeTrancepose(fromList,toList,leveljson):
	for xptime in fromList:
		i = 0
		if isinstance(xptime,type(None)) == False:
			for xp in xptime:
				toList[i].append(changeXpToLevel(xp,leveljson))
				i+=1
	return toList

def changeXpToLevel(xp,leveljson):
	level = 0
	for j in range(0,const.MAXLEVEL):
		if leveljson[j] <= xp:
			level = j + 1
	return level

def checkMaxLen(arglist):
	maxlen = 0
	for vallist in arglist:
		if isinstance(vallist,type(None)) == False:
			if maxlen < len(vallist):
				maxlen = len(vallist)
	return maxlen

