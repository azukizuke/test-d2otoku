import urlLoad
import fileOut
import const

def getMatchData(matchid):
	url=urlLoad.makeOpenDotaMatchDataUrl(matchid)
	
	print("request matchDataOpenDota url : " + url)
	
	root = urlLoad.convertJson(const.TIMEOUT,url)
	return root

#test=root["players"]
#result = root["result"]
#matches = result["matches"]
#for match in matches:
#	matchIDList.append(match["match_id"]);
#fileOut.outputMatchList(filename,matchIDList)
