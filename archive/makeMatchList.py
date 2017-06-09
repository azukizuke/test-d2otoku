import urllib.request
import urllib.error
import time
import json

def outputMatchList(filename,matchIDList):
	FOLDERPATH="testoutput/"
	#fixFilename = "data/" + filename + "/" + filename + "_matchList.csv"
	fixFilename = FOLDERPATH + filename + "_matchList.csv"

	f = open(fixFilename,"w",encoding="UTF-8")

	for matchID in matchIDList:
		f.write(str(matchID))
		f.write("\n")
	f.close

def convertJson(timeout,url):
	urlreq=urllib.request.Request(url)
	while True:
		try:
			url_reader = urllib.request.urlopen(urlreq)
			if url_reader.getcode() == 200:
				break
		except urllib.error.HTTPError:
			time.sleep(timeout)
		except urllib.error.URLError:
			time.sleep(timeout)
	root = json.loads(url_reader.read().decode('utf-8'))
	return root

APIKEY="A7ECA29C017C44E0E6328A4775F768BA"
MAXNUM = 300
TIMEOUT = 30

leagueid=5115
filename="test"
matchIDList = []

if leagueid != None:
	url="http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1?league_id=" + str(leagueid) +"&key=" + APIKEY + "&matches_requested=" + str(MAXNUM)
	print(url)

	root = convertJson(TIMEOUT,url)
	result = root["result"]
	matches = result["matches"]
	for match in matches:
		matchIDList.append(match["match_id"]);
	outputMatchList(filename,matchIDList)

