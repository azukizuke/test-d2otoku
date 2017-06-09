import fileIn
import fileOut
import Hero
import const

# List of All heroes
class HeroesStatistics(object):
	def __init__(self):
		self.HeroesList=[]
		self.heroMaxNum = -1

	#init Hero list from Hero json data
	def initHeroList(self):
		HeroesJson = fileIn.readHeroJson()
		heroesjson = HeroesJson["heroes"]
	
		for hero in heroesjson:
			#from json
			self.HeroesList.append(Hero.Hero(hero['shotname'],hero['id'],hero['safe'],hero['mid'],hero['off'],hero['sup'],hero["abilities"]))

		self.heroMaxNum = len(self.HeroesList)

	def addHeroesMatchPlayerJson(self,MatchPlayerJsonList):
		for PlayerJson in MatchPlayerJsonList:
			self.addHeroPlayerJson(PlayerJson)
	def addHeroPlayerJson(self,PlayerJson):
		for hero in self.HeroesList:
			if PlayerJson["hero_id"]==hero.heroid:
				hero.AddHeroPlayerJsonList(PlayerJson)

	def addHeroesMatchPickBan(self,MatchData):
		if isinstance(MatchData["picks_bans"],type(None)) == False:
			for pb in MatchData["picks_bans"]:
				self.addHeroPickBan(pb["hero_id"],pb["order"])

	def addHeroPickBan(self,hero_id,order):
		for hero in self.HeroesList:
			if hero_id==hero.heroid:
				hero.AddPickBan(order)
		
	def calcHeroesStatistics(self):
		for hero in self.HeroesList:
			hero.calcHeroGoldReason()
			hero.calcPlayerNameList()
			hero.calcHeroTest()
			hero.addLaneRole()
			hero.addSkillList()
			hero.addItemDict()
			hero.addPurchaseLog()
			hero.addLhTime()
			hero.addExpTime()

	def outleaguePickban(self,leaguename,MatchDataList):
		print(leaguename," of pickban")
		print("matchnunm : " + str(len(MatchDataList)))

		#strlist file output
		strlist=[]

		# get sorted list
		sortedAll = sorted(self.HeroesList, key=lambda Hero: Hero.allpb ,reverse=True)
		sortedPick = sorted(self.HeroesList, key=lambda Hero: Hero.pick ,reverse=True)
		sortedBan = sorted(self.HeroesList, key=lambda Hero: Hero.ban ,reverse=True)
		sortedPick1 = sorted(self.HeroesList, key=lambda Hero: Hero.pick1 ,reverse=True)
		sortedPick2 = sorted(self.HeroesList, key=lambda Hero: Hero.pick2 ,reverse=True)
		sortedPick3 = sorted(self.HeroesList, key=lambda Hero: Hero.pick3 ,reverse=True)
		sortedBan1 = sorted(self.HeroesList, key=lambda Hero: Hero.ban1 ,reverse=True)
		sortedBan2 = sorted(self.HeroesList, key=lambda Hero: Hero.ban2 ,reverse=True)
		sortedBan3 = sorted(self.HeroesList, key=lambda Hero: Hero.ban3 ,reverse=True)

		sortedSafe=[]
		sortedMid=[]
		sortedOff=[]
		sortedSup=[]
		for pick in sortedAll:
			if pick.safe==1:
				sortedSafe.append(pick)				
			if pick.mid==1:
				sortedMid.append(pick)				
			if pick.off==1:
				sortedOff.append(pick)				
			if pick.sup==1:
				sortedSup.append(pick)				

		# visualize
		strlist.append("|all||safe||mid||off||sup||ban1||")
		for i in range(10):
			namePick = sortedAll[i].name

			nameSafe = sortedSafe[i].name
			nameMid = sortedMid[i].name
			nameOff = sortedOff[i].name
			nameSup = sortedSup[i].name
			nameBan1 = sortedBan1[i].name
			
			outstr1 = fileOut.makeOtokuPBstr(sortedAll[i].heroid,1,round(sortedAll[i].allpb / len(MatchDataList) * 100))
			outstr2 = fileOut.makeOtokuPBstr(sortedSafe[i].heroid,1,round(sortedSafe[i].allpb / len(MatchDataList) * 100))
			outstr3 = fileOut.makeOtokuPBstr(sortedMid[i].heroid,1,round(sortedMid[i].allpb / len(MatchDataList) * 100))
			outstr4 = fileOut.makeOtokuPBstr(sortedOff[i].heroid,1,round(sortedOff[i].allpb / len(MatchDataList) * 100))
			outstr5 = fileOut.makeOtokuPBstr(sortedSup[i].heroid,1,round(sortedSup[i].allpb / len(MatchDataList) * 100))
			outstr6 = fileOut.makeOtokuPBstr(sortedBan1[i].heroid,1,round(sortedBan1[i].allpb / len(MatchDataList) * 100))
			outstr7 = "|"

			outstr = outstr1 + outstr2 + outstr3 + outstr4 + outstr5 + outstr6 + outstr7
			strlist.append(outstr)
		fileOut.outputLeagueData(strlist,leaguename,const.SUFFIX_PICKBAN)

		# visualize
		outstr=""
		strlist=[]
		dictlist=[{}]
		for hero in self.HeroesList:
			outdict={}
			outstr1 = hero.heroid
			outstr2 = round(hero.allpb / len(MatchDataList) * 100)

			outstr = str(outstr1) + " : " + str(outstr2)
			outdict = {"heroid" : outstr1,"pb" : outstr2}
			strlist.append(outdict)
		fileOut.outputLeagueData(strlist,leaguename,const.SUFFIX_PBCOMP)

		##player div top 10 wowwow
		strlist=[]
		for i in range(10):
			outlist =[]

			sortedNameDict = sorted(sortedAll[i].usePlayerNameDict.items(), key=lambda name: name[1], reverse=True)
			sortedNameDict2 = sorted(sortedSafe[i].usePlayerNameDict.items(), key=lambda name: name[1], reverse=True)
			sortedNameDict3 = sorted(sortedMid[i].usePlayerNameDict.items(), key=lambda name: name[1], reverse=True)
			sortedNameDict4 = sorted(sortedOff[i].usePlayerNameDict.items(), key=lambda name: name[1], reverse=True)
			sortedNameDict5 = sorted(sortedSup[i].usePlayerNameDict.items(), key=lambda name: name[1], reverse=True)


			outstr1 = "|"
			outstr1 += fileOut.makeDokuImage(sortedAll[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makePlayerDevStr(sortedNameDict)

			outstr1 += "|"
			outstr1 += fileOut.makeDokuImage(sortedSafe[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makePlayerDevStr(sortedNameDict2)

			outstr1 += "|"
			outstr1 += fileOut.makeDokuImage(sortedMid[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makePlayerDevStr(sortedNameDict3)

			outstr1 += "|"
			outstr1 += fileOut.makeDokuImage(sortedOff[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makePlayerDevStr(sortedNameDict4)

			outstr1 += "|"
			outstr1 += fileOut.makeDokuImage(sortedSup[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makePlayerDevStr(sortedNameDict5)

			strlist.append(outstr1)
		fileOut.outputLeagueData(strlist,leaguename,const.SUFFIX_PLAYERDIV_DOKU)

		##hero role divdiv
		strlist=[]
		for i in range(10):
			outlist =[]

			sortedNameDict = sorted(sortedAll[i].laneRoleDict.items(), key=lambda name: name[0], reverse=False)
			sortedNameDict2 = sorted(sortedSafe[i].laneRoleDict.items(), key=lambda name: name[0], reverse=False)
			sortedNameDict3 = sorted(sortedMid[i].laneRoleDict.items(), key=lambda name: name[0], reverse=False)
			sortedNameDict4 = sorted(sortedOff[i].laneRoleDict.items(), key=lambda name: name[0], reverse=False)
			sortedNameDict5 = sorted(sortedSup[i].laneRoleDict.items(), key=lambda name: name[0], reverse=False)
		
			outstr1 = "|"
			outstr1 += fileOut.makeDokuImage(sortedAll[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makeLaneRoleStr(sortedNameDict)

			outstr1 += "|"
			outstr1 += fileOut.makeDokuImage(sortedSafe[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makeLaneRoleStr(sortedNameDict2)

			outstr1 += "|"
			outstr1 += fileOut.makeDokuImage(sortedMid[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makeLaneRoleStr(sortedNameDict3)

			outstr1 += "|"
			outstr1 += fileOut.makeDokuImage(sortedOff[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makeLaneRoleStr(sortedNameDict4)

			outstr1 += "|"
			outstr1 += fileOut.makeDokuImage(sortedSup[i].heroid)
			outstr1 += "|"
			outstr1 += fileOut.makeLaneRoleStr(sortedNameDict5)

			strlist.append(outstr1)
		fileOut.outputLeagueData(strlist,leaguename,const.SUFFIX_ROLEDIV_DOKU)



	def outHeroesStatistics(self,leaguename):
		for hero in self.HeroesList:
			hero.outputStatistics(leaguename)
