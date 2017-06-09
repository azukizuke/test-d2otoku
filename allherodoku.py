import sys
import subprocess
import os
import fileIn

args=sys.argv

leaguename=args[1]
dokuwikiname=args[2]
year=args[3]

HeroesJson = fileIn.readHeroJson()
heroesjson = HeroesJson["heroes"]
	
for hero in heroesjson:
	heroname=hero["shotname"]

	FILEPATH="/var/lib/dokuwiki/data/pages/statistics/league/" + str(year) + "/" + str(year) + "/" + str(dokuwikiname) + "/" + str(heroname) + ".txt"
	cmd = "script/herodoku.sh" + " " + str(leaguename) + " " + str(heroname) + " > " + str(FILEPATH)
	print(cmd)
	outp=subprocess.getoutput(cmd)
	print(outp) 


#script/herodoku.sh ${leaguename} $2 > ${FILEPATH}
