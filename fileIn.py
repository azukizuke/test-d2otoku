import const
import json

def readMatchList(filename):
	MatchList=[]
	fixFilename=const.PATH + filename + "/" + filename + const.SUFFIX_MATCHIDLIST

	f = open(fixFilename,"r",encoding="UTF-8")
	line = f.readline()
	while line:
		MatchList.append(line.strip())
		line = f.readline()

	f.close
	return MatchList

def readHeroJson():
	filepath= const.JSONPATH + "heroes.json"
	fjson = open(filepath,'r')
	jsonHeroes = json.load(fjson)
	return jsonHeroes

def readItemIdJson():
	filepath= const.JSONPATH + "item_ids.json"
	fjson = open(filepath,'r')
	jsonHeroes = json.load(fjson)
	return jsonHeroes

def readItemOdotaJson():
	filepath= const.JSONPATH + "itemsodota.json"
	fjson = open(filepath,'r')
	jsonHeroes = json.load(fjson)
	return jsonHeroes

def readXPOdotaJson():
	filepath= const.JSONPATH + "xp_level.json"
	fjson = open(filepath,'r')
	jsonHeroes = json.load(fjson)
	return jsonHeroes

def readLeagueList(filename,SUFFIX):
	outList=[]
	fixFilename=const.PATH + filename + "/" + filename + SUFFIX

	f = open(fixFilename,"r",encoding="UTF-8")
	line = f.readline()
	while line:
		outList.append(line.strip())
		line = f.readline()

	f.close
	return outList

def readLeagueDict(filename,SUFFIX):
	outDict=[{}]
	fixFilename=const.PATH + filename + "/" + filename + SUFFIX

	f = open(fixFilename,"r",encoding="UTF-8")
	line = f.readline()
	while line:
		dic={}	
		instr=line.strip()
		instr=instr.replace('\'','\"')
		instr=json.loads(instr)
		outDict.append(instr)
		line = f.readline()

	f.close
	outDict.pop(0)
	return outDict
