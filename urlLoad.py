import urllib.request
import urllib.error
import time
import json

def convertJson(timeout,url):
	headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
	urlreq=urllib.request.Request(url)
	urlreq=urllib.request.Request(url = url, headers=headers)
	while True:
		try:
			url_reader = urllib.request.urlopen(urlreq)
			print("json load : " + str(url_reader.getcode()))
			if url_reader.getcode() == 200:
				break
		except urllib.error.HTTPError as e:
			print("HTTPError : " + str(url))
			print("HTTPError : " + str(e.reason))
			print("HTTPError : " + str(e.code))
			time.sleep(timeout)
		except urllib.error.URLError:
			print("URLError : " + str(url))
			time.sleep(timeout)
	root = json.loads(url_reader.read().decode('utf-8'))
	return root

def makeMatchHistroyUrl(leagueid,APIKEY,MAXNUM,startid):
	if leagueid != None:
		#url="http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1?league_id=" + str(leagueid) +"&key=" + APIKEY + "&matches_requested=" + str(MAXNUM) + "&start_at_match_id=" + str(startid)
		url="http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1?league_id=" + str(leagueid) +"&key=" + APIKEY + "&matches_requested=" + str(MAXNUM)
	return url

def makeOpenDotaMatchDataUrl(matchid):
	if matchid != None:
		url="https://api.opendota.com/api/matches/" + matchid
	return url
