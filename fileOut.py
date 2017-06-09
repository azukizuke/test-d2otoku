import const
import os
import fileIn
import json

def outputMatchList(filename,matchIDList):
	fixFilename = const.PATH + filename + "/" + filename + const.SUFFIX_MATCHIDLIST
	print ("debug filename : " + fixFilename)
	f = open(fixFilename,"w",encoding="UTF-8")

	for matchID in matchIDList:
		f.write(str(matchID))
		f.write("\n")
	f.close

def initMakeFolder(leaguename):
	FolderPath=const.PATH + leaguename
	if not os.path.isdir(FolderPath):
		os.mkdir(FolderPath)

	jsonHeroes = fileIn.readHeroJson()
	jsonHeroes = jsonHeroes["heroes"]
	for json in jsonHeroes:
		FolderPath=const.PATH + leaguename + "/" + json["shotname"]
		if not os.path.isdir(FolderPath):
			os.mkdir(FolderPath)


def outputHeroStatistics(heroname,leaguename,statname,val):
	fixFilename=const.PATH + leaguename + "/" + heroname + "/" + statname

	f = open(fixFilename,"w",encoding="UTF-8")

	f.write(str(val))
	f.write("\n")

	f.close

def outputHeroStatisticsList(heroname,leaguename,statname,statlist):
	fixFilename=const.PATH + leaguename + "/" + heroname + "/" + statname

	f = open(fixFilename,"w",encoding="UTF-8")

	for val in statlist:
		f.write(str(val))
		f.write("\n")

	f.close

def outputLeagueData(pbstrlist,leaguename,suffix):
	fixFilename = const.PATH + leaguename + "/" + leaguename + suffix
	f = open(fixFilename,"w",encoding="UTF-8")

	for val in pbstrlist:
		f.write(str(val))
		f.write("\n")

	f.close
	
def makeDokuImage(heroid):
	imgsize =50 
	outstr = "{{:hero:" + str(heroid) + ".png?nolink&" + str(imgsize) + "|}}"
	return outstr

def makeDokuAbilityImage(abilityid):
	imgsize =20
	outstr = "{{:abilities:" + str(abilityid) + ".png?nolink&" + str(imgsize) + "|}}"
	return outstr

def makeDokuItemImage(itemid):
	imgsize =40
	outstr = "{{:item:" + str(itemid) + ".png?nolink&" + str(imgsize) + "|}}"
	return outstr

def makeOtokuPBstr(heroid,role,pbpercent):
	imgsize =50 
	outstr = "| {{:hero:" + str(heroid) + ".png?nolink&" + str(imgsize) + "|}} |" + str(pbpercent) + "%"
	return outstr

def makeLaneRoleStr(NameDict):
	j = 0
	outstr1 = ""
	for pname in NameDict:
		outstr1 += const.DICT_ROLE[pname[0]]
		outstr1  += " : " 
		outstr1  += str(pname[1])
		if j < len(NameDict):
			outstr1 += " "
			outstr1 += "\\\\"
			outstr1 += " "
		j += 1
	outstr1 += "|"
	return outstr1

def makePlayerDevStr(NameDict):
	j = 0
	outstr1 = ""
	for pname in NameDict:
		outstr1 += str(pname[0])
		outstr1  += " : " 
		outstr1  += str(pname[1])
		if j < len(NameDict):
			outstr1 += " "
			outstr1 += "\\\\"
			outstr1 += " "
		j += 1
	outstr1 += "|"
	return outstr1
