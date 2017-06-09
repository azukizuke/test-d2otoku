import const
import fileIn
import fileOut


def compLeaguePickban(league1,league2):
	pblist1 = fileIn.readLeagueDict(league1,const.SUFFIX_PBCOMP)
	pblist2 = fileIn.readLeagueDict(league2,const.SUFFIX_PBCOMP)

	pblist3 = [{}]
	pblist3.clear()
	i=0

	for hero1 in pblist1:
		diff = hero1["pb"] - pblist2[i]["pb"]
		pblist3.append({"heroid" : hero1['heroid'],"pb" : diff})
		i+=1	

	##big10 + less10 de iika
	sortedDict = sorted(pblist3, key=lambda x:x['pb'], reverse=True)
	
	strlist=[]
	outstr1="comp:" + league2
	strlist.append(outstr1)
	for i in range(10):
		outstr1 = ""

		j = len(sortedDict) - i - 1

		outstr1 += "|"	
		outstr1 += fileOut.makeDokuImage(sortedDict[i]["heroid"])
		outstr1 += "|+"	
		outstr1 += str(sortedDict[i]["pb"])
		outstr1 += "%|"	
		outstr1 += fileOut.makeDokuImage(sortedDict[j]["heroid"])
		outstr1 += "|"	
		outstr1 += str(sortedDict[j]["pb"])
		outstr1 += "%|"	
		strlist.append(outstr1)

	fileOut.outputLeagueData(strlist,league1,const.SUFFIX_PBCOMP_DOKU)
		
