import numpy
import fileOut
import const
import fileIn
import listController
import dictController

class Hero(object):
	def __init__(self,name,heroID,safe,mid,off,sup,abilities):
		self.name = name
		self.heroid = heroID
		self.PlayerJsonList = []
		self.safe = safe
		self.mid = mid
		self.off = off
		self.sup = sup
	
		self.allpb = 0
	
		self.pick = 0
		self.ban = 0
		self.all1 = 0
		self.all2 = 0
		self.all3 = 0

		self.ban1 = 0
		self.ban2 = 0
		self.ban3 = 0
	
		self.pick1 = 0
		self.pick2 = 0
		self.pick3 = 0

		self.abilities = abilities
##usePlayerNameList###########################################
		self.usePlayerNameList = []
		self.usePlayerNameDict = {}

##Role#######################################################
		self.laneRoleDict = {1:0,2:0,3:0,4:0}
##Skill####################################################
		self.skillList=[]
		self.skillDict={}
		self.skillStatisticsList=[{}]
##item####################################################
		self.itemDict={} # id , num
		self.startItemDict={} # id , num

		self.startItemPatternDict=[] # idList , num,
		self.startItemList=[]

		self.purchaseLogList=[]
		self.purchaseLogDict=[{}]
		self.purchaseLogDictCreated=[{}]
		self.purchaseLogDictCreatedFix=[{}]

###avg#########################################################
		self.goldreason_others = []
		self.goldreason_death = []
		self.goldreason_bb = []
		self.goldreason_building = []
		self.goldreason_hero = []
		self.goldreason_creep = []
		self.goldreason_rosh = []

###LHTIME######################################################
		self.lhtimeList = [[]]
		self.lhtempList = [[]]
		self.avglhtimeList = []
		self.maxlhtimeList = []
		self.medlhtimeList = []
		self.minlhtimeList = []

		self.xptimeList = [[]]
		self.avgxptimeList = []
		self.maxxptimeList = []
		self.medxptimeList = []
		self.minxptimeList = []

###json#######################################################
		self.itemidjson = fileIn.readItemOdotaJson()
		self.xpleveljson = fileIn.readXPOdotaJson()

############################################################
	def AddHeroPlayerJsonList(self,PlayerJson):
		self.PlayerJsonList.append(PlayerJson)

	def calcPlayerNameList(self):
		for PlayerJson in self.PlayerJsonList:
			if "name" in PlayerJson:
				if isinstance(PlayerJson["name"],type(None)) == False:
					##List no hou iranai?
					self.usePlayerNameList.append(PlayerJson["name"])
					self.usePlayerNameDict = dictController.addCounterKey(self.usePlayerNameDict,PlayerJson["name"])

	def addLaneRole(self):
		for PlayerJson in self.PlayerJsonList:
			if "lane_role" in PlayerJson:
				self.laneRoleDict[PlayerJson["lane_role"]] += 1

	def addSkillList(self):
		#refactor kansuu
		for PlayerJson in self.PlayerJsonList:
			if "ability_upgrades_arr" in PlayerJson:
				self.skillList.append(PlayerJson["ability_upgrades_arr"])

                ##toukei torutameni shoki abi list tukuru
		#refactor kansuu
		for i in range(const.MAXLEVEL):
			self.skillStatisticsList.append({})
			for initSkill in self.abilities:
				self.skillStatisticsList[i][initSkill]=0

		###level statistics
		#refactor kansuu
		for skillArr in self.skillList:
			if isinstance(skillArr,type(None)) == False:
				for (cnt,skill) in enumerate(skillArr):
					self.skillStatisticsList=listController.addAttributeCounter(self.skillStatisticsList,cnt,skill)


	def addItemDict(self):
		itemlist=[]
		for PlayerJson in self.PlayerJsonList:
			for key in const.HEROITEMKEY:
				itemlist.append(PlayerJson[key])

		for item in itemlist:
			self.itemDict = dictController.addCounterKey(self.itemDict,item)


	def addLhTime(self):
		tempList=[]
		self.lhtempList=listController.initListJson(self.PlayerJsonList,"lh_t")
		tempList=listController.initListJson(self.PlayerJsonList,"lh_t")

		maxlen = listController.checkMaxLen(tempList)
		self.lhtimeList=[[] for j in range(maxlen)]

		self.lhtimeList = listController.addAttributeTrancepose(tempList,self.lhtimeList)

		#refactor dounika sitaine 
		for lhlist in self.lhtimeList:
			self.avglhtimeList.append(numpy.mean(lhlist))
			self.maxlhtimeList.append(numpy.max(lhlist))
			self.minlhtimeList.append(numpy.min(lhlist))
			self.medlhtimeList.append(numpy.median(lhlist))

			
	def addExpTime(self):
		tempList=[]
		tempList=listController.initListJson(self.PlayerJsonList,"xp_t")

		maxlen = listController.checkMaxLen(tempList)
		self.xptimeList=[[] for j in range(maxlen)]


		self.xptimeList = listController.addXpTimeTrancepose(tempList,self.xptimeList,self.xpleveljson)
#		for xptime in tempList:
#			i = 0
#			if isinstance(xptime,type(None)) == False:
#				for xp in xptime:
#					##exp -> level
#					level = 0
#					for j in range(0,const.MAXLEVEL):
#						if self.xpleveljson[j] <= xp:
#							level = j + 1
#					self.xptimeList[i].append(level)
#					i+=1
#
		for xplist in self.xptimeList:
			self.avgxptimeList.append(numpy.mean(xplist))
			self.maxxptimeList.append(numpy.max(xplist))
			self.minxptimeList.append(numpy.min(xplist))
			self.medxptimeList.append(numpy.median(xplist))

						
	def addPurchaseLog(self):
		for PlayerJson in self.PlayerJsonList:
			self.purchaseLogList.append(PlayerJson["purchase_log"])

		for purchaseLog in self.purchaseLogList:
			count=0
			if isinstance(purchaseLog,type(None)) == False:
				for purchase in purchaseLog:
					itemid=self.itemidjson[purchase["key"]]["id"]
					##kokode core item senbetsu wo suru
					if int(self.itemidjson[purchase["key"]]["cost"]) > const.ITEM_THRESHOLD:
						if count >= len(self.purchaseLogDict):
							self.purchaseLogDict.append({itemid: 0})
							
						if itemid in self.purchaseLogDict[count]:
							self.purchaseLogDict[count][itemid] += 1
						else:
							self.purchaseLogDict[count][itemid] = 1
						count+=1

		#tenuki sugiru
		for purchaseLog in self.purchaseLogList:
			count=0
			if isinstance(purchaseLog,type(None)) == False:
				for purchase in purchaseLog:
					itemid=self.itemidjson[purchase["key"]]["id"]
					##kokode core item senbetsu wo suru
					if int(self.itemidjson[purchase["key"]]["created"]) == True:
						if count >= len(self.purchaseLogDictCreated):
							self.purchaseLogDictCreated.append({itemid: 0})
							
						if itemid in self.purchaseLogDictCreated[count]:
							self.purchaseLogDictCreated[count][itemid] += 1
						else:
							self.purchaseLogDictCreated[count][itemid] = 1
						count+=1

		#tenuki sugiru
		for purchaseLog in self.purchaseLogList:
			count=0
			if isinstance(purchaseLog,type(None)) == False:
				for purchase in purchaseLog:
					itemid=self.itemidjson[purchase["key"]]["id"]
					##kokode core item senbetsu wo suru
					if int(self.itemidjson[purchase["key"]]["created_fix"]) == True:
						if count >= len(self.purchaseLogDictCreatedFix):
							self.purchaseLogDictCreatedFix.append({itemid: 0})
							
						if itemid in self.purchaseLogDictCreatedFix[count]:
							self.purchaseLogDictCreatedFix[count][itemid] += 1
						else:
							self.purchaseLogDictCreatedFix[count][itemid] = 1
						count+=1
		#kansuu wakeya #kokokara satart item
		startitemlist=[]

		for purchaseLog in self.purchaseLogList:
			if isinstance(purchaseLog,type(None)) == False:
				for purchase in purchaseLog:
					itemid=self.itemidjson[purchase["key"]]["id"]
					if purchase["time"] <= const.STARTITEMTIME:
						itemid=self.itemidjson[purchase["key"]]["id"]
						if itemid in self.startItemDict:
							self.startItemDict[itemid]+=1
						else:
							self.startItemDict[itemid]=1

					
		#kokokara satart item patter list

		for purchaseLog in self.purchaseLogList:
			if isinstance(purchaseLog,type(None)) == False:
				tempitemList=[]
				for purchase in purchaseLog:
					itemid=self.itemidjson[purchase["key"]]["id"]
					if purchase["time"] <= const.STARTITEMTIME:
						itemid=self.itemidjson[purchase["key"]]["id"]
						tempitemList.append(itemid)

				if len(tempitemList) > 0:
					if len(self.startItemPatternDict) == 0:
						self.startItemPatternDict.append({"itemPattern":sorted(tempitemList), "num":1})
					else:
						for cnt,selfdict in enumerate(self.startItemPatternDict):
							if selfdict["itemPattern"] == sorted(tempitemList):
								self.startItemPatternDict[cnt]["num"]+=1
								break
						else:
							self.startItemPatternDict.append({"itemPattern":sorted(tempitemList), "num":1})
			

	def AddPickBan(self,order):
		## add pickban number from order number
		if order in {0,1,2,3}:
			self.allpb += 1
			self.all1 += 1

			self.ban += 1
			self.ban1 += 1
		if order in {4,5,6,7}:
			self.allpb += 1
			self.all1 += 1

			self.pick += 1
			self.pick1 += 1
		if order in {8,9,10,11}:
			self.allpb += 1
			self.all2 += 1
			self.ban += 1
			self.ban2 += 1
		if order in {12,13,14,15}:
			self.allpb += 1
			self.all2 += 1
			self.pick += 1
			self.pick2 += 1
		if order in {16,17}:
			self.allpb += 1
			self.all3 += 1
			self.ban += 1
			self.ban3 += 1
		if order in {18,19}:
			self.allpb += 1
			self.all3 += 1
			self.pick += 1
			self.pick3 += 1

	def calcHeroPickBan(self):
		print("calctest")

	def calcHeroPos(self):
		for PlayerJson in self.PlayerJsonList:
			print(PlayerJson["lane_pos"])

	def calcHeroItem(self):
		for PlayerJson in self.PlayerJsonList:
			print(PlayerJson["item_1"])

	def calcHeroGoldReason(self):
		for PlayerJson in self.PlayerJsonList:
			goldreasons=PlayerJson["gold_reasons"]
			if goldreasons == None:
				break
			
			if "0" in goldreasons:
				self.goldreason_others.append(int(goldreasons["0"]))
			else:
				self.goldreason_others.append(0)
			if "1" in goldreasons:
				self.goldreason_death.append(int(goldreasons["1"]))
			else:
				self.goldreason_death.append(0)
			if "2" in goldreasons:
				self.goldreason_bb.append(int(goldreasons["2"]))
			else:
				self.goldreason_bb.append(0)
			if "11" in goldreasons:
				self.goldreason_building.append(int(goldreasons["11"]))
			else:
				self.goldreason_building.append(0)
			if "12" in goldreasons:
				self.goldreason_hero.append(int(goldreasons["12"]))
			else:
				self.goldreason_hero.append(0)
			if "13" in goldreasons:
				self.goldreason_creep.append(int(goldreasons["13"]))
			else:
				self.goldreason_creep.append(0)
			if "14" in goldreasons:
				self.goldreason_rosh.append(int(goldreasons["14"]))
			else:
				self.goldreason_rosh.append(0)

	def calcHeroTest(self):
		for PlayerJson in self.PlayerJsonList:
			if "lane_role" in PlayerJson:
				debuglane=0	

	def outputStatistics(self,filename):
		strlist=[]
                ##gol reason
		if len(self.goldreason_building) != 0:
			val=numpy.mean(self.goldreason_building);
	
			fileOut.outputHeroStatistics(self.name,filename,"goldreason",val)
		else:
			fileOut.outputHeroStatistics(self.name,filename,"goldreason","None")
		##debug name
		if len(self.usePlayerNameList) != 0:
			fileOut.outputHeroStatisticsList(self.name,filename,"playerdiv",self.usePlayerNameList)

##skillDiv
		strlist=[]
		strlist2=[]
		if len(self.skillStatisticsList) != 0:
			outstr2=""
			#first row
			for skillStat in self.skillStatisticsList:
				outstr1=""
				for skill,num in skillStat.items():
					outstr1 += str(skill)
					outstr1 += ":"
					if len(self.PlayerJsonList) != 0 : 
						percent=int((num / len(self.PlayerJsonList)) * 100)
					else:
						percent=0
					outstr1 += str(percent)
					outstr1 += "%"
					outstr1 += " \\\\ "
				outstr2+=outstr1
				outstr2+="|"
			fileOut.outputHeroStatistics(self.name,filename,"skillStatistics_doku",outstr2)

##skilldiv test

		strlist=[]
		strlist2=[]
		#itigyoume wo kaku
		outstr=""
		outstr += "|"
		outstr += "-|"
		for i in range(25):
			outstr += str(i+1)
			outstr += "|"

		strlist.append(outstr)

		#kaku skillset row printout
		for abilityid in self.abilities:
			outstr=""
			outstr += "|"
			## image output
			outstr += fileOut.makeDokuAbilityImage(abilityid)
			outstr += "|"
			for level in range(25):
				#get sum number
				abilitysum=0
				for val in (self.skillStatisticsList[level].values()):
					abilitysum += val
		
				if (abilitysum) != 0 : 
					percent=int((self.skillStatisticsList[level][abilityid] / abilitysum) * 100)
				else:
					percent=0
				outstr += str(percent)
				outstr += "%|"
			strlist.append(outstr)
		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_SKILLDIV,strlist)

##debug skilldiv araidasiyou
		strlist=[]
		strlist2=[]
		#itigyoume wo kaku
		outstr=""
		outstr += "|"
		outstr += "-|"
		for i in range(25):
			outstr += str(i+1)
			outstr += "|"

		strlist.append(outstr)

		#debug kokode skillset wo hirou
		tempabiList=[]
		for skillStat in self.skillStatisticsList:
			for val in skillStat.items():
				tempabiList.append(val[0])
				uniqtempabiList=sorted(list(set(tempabiList)))

		#kaku skillset row
		for abilityid in uniqtempabiList:
			outstr=""
			outstr += "|"
			## image output
			outstr += fileOut.makeDokuAbilityImage(abilityid)
			outstr += "|"
			for level in range(25):
				#get sum number
				abilitysum=0
				for val in (self.skillStatisticsList[level].values()):
					abilitysum += val
		
				if (abilitysum) != 0 : 
					if abilityid in self.skillStatisticsList[level]:
						percent=int((self.skillStatisticsList[level][abilityid] / abilitysum) * 100)
					else:
						percent=0
				else:
					percent=0
				outstr += str(percent)
				outstr += "%|"
			strlist.append(outstr)
		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_SKILLDIV_TEST,strlist)

#itemDict
		strlist=[]
		strlist2=[]
		if len(self.itemDict) != 0:
			sortedDict = sorted(self.itemDict.items(), key=lambda x:x[1], reverse=True)

			for dic in sortedDict:
				percent = int(dic[1] / len(self.PlayerJsonList) * 100)

				outstr=""
				outstr+="|"
				img=""
				outstr+=str(fileOut.makeDokuItemImage(dic[0]))
				outstr+="|"
				outstr+=str(percent)
				outstr+="%|"
				outstr+="|"
				if dic[0] != 0:
					strlist.append(outstr)
		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_ITEMDIV,strlist)

#startItemDict
		strlist=[]
		strlist2=[]
		if len(self.startItemDict) != 0:
			sortedDict = sorted(self.startItemDict.items(), key=lambda x:x[1], reverse=True)

			for dic in sortedDict:
				percent = int(dic[1] / len(self.PlayerJsonList) * 100)

				outstr=""
				outstr+="|"
				img=""
				outstr+=str(fileOut.makeDokuItemImage(dic[0]))
				outstr+="|"
				outstr+=str(percent)
				outstr+="%|"
				outstr+="|"
				if dic[0] != 0:
					strlist.append(outstr)
		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_STARTITEMDIV,strlist)

#startItemPatternDict
		strlist=[]
		strlist2=[]
		if len(self.startItemPatternDict) != 0:
			sortedDict = sorted(self.startItemPatternDict, key=lambda x:x["num"], reverse=True)

			for dic in sortedDict:
				outstr=""
				outstr+="|"
				outstr+=str(dic["num"])
				outstr+="|"
				for itemid in dic["itemPattern"]:
					outstr+=str(fileOut.makeDokuItemImage(itemid))
					outstr+="|"
				strlist.append(outstr)
		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_STARTITEMPATTERNDIV,strlist)

#purchase log
		strlist=[]
		for purchaseDict in self.purchaseLogDict:
			outstr=""
			outstr+="|"
			sortDict=sorted(purchaseDict.items(), key=lambda x:x[1], reverse=True)
			for val in sortDict:
				iid=val[0]
				num=val[1]
				percent = int(num / len(self.PlayerJsonList) * 100)

				outstr+=str(fileOut.makeDokuItemImage(iid))
				outstr+="|"
				outstr+=str(percent)
				outstr+="%|"
			strlist.append(outstr)
		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_PURCHASEDIV,strlist)

#purchase log created
		strlist=[]
		for purchaseDict in self.purchaseLogDictCreated:
			outstr=""
			outstr+="|"
			sortDict=sorted(purchaseDict.items(), key=lambda x:x[1], reverse=True)
			for val in sortDict:
				iid=val[0]
				num=val[1]
				percent = int(num / len(self.PlayerJsonList) * 100)

				outstr+=str(fileOut.makeDokuItemImage(iid))
				outstr+="|"
				outstr+=str(percent)
				outstr+="%|"
			strlist.append(outstr)
		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_PURCHASEDIV_CREATED,strlist)

#purchase log created Fix
		strlist=[]
		for purchaseDict in self.purchaseLogDictCreatedFix:
			outstr=""
			outstr+="|"
			sortDict=sorted(purchaseDict.items(), key=lambda x:x[1], reverse=True)
			for val in sortDict:
				iid=val[0]
				num=val[1]
				percent = int(num / len(self.PlayerJsonList) * 100)

				outstr+=str(fileOut.makeDokuItemImage(iid))
				outstr+="|"
				outstr+=str(percent)
				outstr+="%|"
			strlist.append(outstr)
		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_PURCHASEDIV_CREATED_FIX,strlist)

#lhtime
		strlist=[]
		
		outstr=""
		outstr+="|"
		outstr+="LH"
		outstr+="|"
		for val in range(0,len(self.avglhtimeList)):
			outstr+=str(val)
			outstr+="|"
		strlist.append(outstr)

		
		outstr=""
		outstr+="|"
		outstr+="avg"
		outstr+="|"
		for val in self.avglhtimeList:
			outstr+=str(int(val))
			outstr+="|"
		strlist.append(outstr)

		outstr=""
		outstr+="|"
		outstr+="med"
		outstr+="|"
		for val in self.medlhtimeList:
			outstr+=str(int(val))
			outstr+="|"
		strlist.append(outstr)

		outstr=""
		outstr+="|"
		outstr+="max"
		outstr+="|"
		for val in self.maxlhtimeList:
			outstr+=str(int(val))
			outstr+="|"
		strlist.append(outstr)

		outstr=""
		outstr+="|"
		outstr+="min"
		outstr+="|"
		for val in self.minlhtimeList:
			outstr+=str(int(val))
			outstr+="|"
		strlist.append(outstr)

		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_LHTIME,strlist)
		
		
#lhtime
		strlist=[]
		
		outstr=""
		outstr+="|"
		outstr+="LV"
		outstr+="|"
		for val in range(0,len(self.avgxptimeList)):
			outstr+=str(val)
			outstr+="|"
		strlist.append(outstr)

		
		outstr=""
		outstr+="|"
		outstr+="avg"
		outstr+="|"
		for val in self.avgxptimeList:
			outstr+=str(int(val))
			outstr+="|"
		strlist.append(outstr)

		outstr=""
		outstr+="|"
		outstr+="med"
		outstr+="|"
		for val in self.medxptimeList:
			outstr+=str(int(val))
			outstr+="|"
		strlist.append(outstr)

		outstr=""
		outstr+="|"
		outstr+="max"
		outstr+="|"
		for val in self.maxxptimeList:
			outstr+=str(int(val))
			outstr+="|"
		strlist.append(outstr)

		outstr=""
		outstr+="|"
		outstr+="min"
		outstr+="|"
		for val in self.minxptimeList:
			outstr+=str(int(val))
			outstr+="|"
		strlist.append(outstr)

		fileOut.outputHeroStatisticsList(self.name,filename,const.SUFFIX_XPTIME,strlist)


