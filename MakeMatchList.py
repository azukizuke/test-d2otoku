import urlLoad
import fileOut
import const
def makeMatchIdListFile(leagueid,leaguename,startid,endid):
	matchIDList = []
	print("make file" + str(leagueid))

	while True:
		url=urlLoad.makeMatchHistroyUrl(leagueid,const.APIKEY,const.MAXNUM,startid)
		print("request league url : " + url)
		root = urlLoad.convertJson(const.TIMEOUT,url)
		result = root["result"]
		matches = result["matches"]

		for match in matches:
			#list
			if startid <= match["match_id"] :
				if match["match_id"] <= endid:
			 		matchIDList.append(match["match_id"]);
			
		break
	fileOut.outputMatchList(leaguename,matchIDList)

