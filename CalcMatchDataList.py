import urlLoad
import fileOut
import fileIn
import const
import MakeMatchData

def getMatchDataList(filename):
	matchDataList=[]
	MatchIdList = fileIn.readMatchList(filename)
	for matchID in MatchIdList:
		matchDataList.append(MakeMatchData.getMatchData(matchID))
	return matchDataList

