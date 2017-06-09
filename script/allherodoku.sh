#!/bin/sh
leaguename=$1
heroname=$2
dokuwikiname=$3
year=$4
FILEPATH="/var/lib/var/lib/dokuwiki/data/pages/statistics/league/${year}/${year}/${dokuwikiname}/${heroname}.txt"

script/herodoku.sh ${leaguename} $2 > ${FILEPATH}
