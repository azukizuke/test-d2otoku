#!/bin/sh
leaguename=$1

cat leaguedata/$leaguename/${leaguename}_pickban.txt
echo ""
echo ""
cat leaguedata/$leaguename/${leaguename}_pbCompDoku.csv
echo ""
echo ""
cat leaguedata/$leaguename/${leaguename}_roleDivDoku.txt
echo ""
echo ""
cat leaguedata/$leaguename/${leaguename}_playerDivkDoku.txt | sed -e "s/\^//g"
