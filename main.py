import urlLoad
import fileOut
import fileIn
import const
import MakeMatchData
import CalcMatchDataList
import Hero
import HeroesStatistics
import MakeMatchList
import CompLeague

leagueid=5353
leaguename="epicenter2017"
startid=3225048663
endid=9999999999

comp_leaguename="zotac"

#Initialize Folder
fileOut.initMakeFolder(leaguename)

#Get MatchIdList
if leagueid != 0:
	MakeMatchList.makeMatchIdListFile(leagueid,leaguename,startid,endid)

#Get MatchDataList
MatchDataList=[]
MatchDataList=CalcMatchDataList.getMatchDataList(leaguename)

###Heroes List Class Init
heroesStatistics = HeroesStatistics.HeroesStatistics()
heroesStatistics.initHeroList()

for MatchData in MatchDataList:
	#MatchData内にあるplyersdata
	heroesStatistics.addHeroesMatchPlayerJson(MatchData["players"])
	#pickban data keisan
	heroesStatistics.addHeroesMatchPickBan(MatchData)

#######HeroStat Calc
heroesStatistics.calcHeroesStatistics()

#######Output Calc
heroesStatistics.outHeroesStatistics(leaguename)
heroesStatistics.outleaguePickban(leaguename,MatchDataList)

###comp mo tuideni
CompLeague.compLeaguePickban(leaguename,comp_leaguename)
