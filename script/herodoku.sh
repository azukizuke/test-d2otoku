#!/bin/sh
leaguename=$1
heroname=$2

echo "試験的にタレントデータは入れようとしましたが、画像用意してない、indexついていないとぐちゃぐちゃです。"
echo "上からレベル10のtal1,2、そのあと15,20,25と続いています。"
echo "また、レベル20と25のタレントは18と19に押し込まれるので気をつけてください。"
cat leaguedata/${leaguename}/${heroname}/skilldiv.txt
echo ""
echo "合成アイテム購入順序(数種類除外してます)"
cat leaguedata/${leaguename}/${heroname}/purchasediv_created_fix.txt
echo ""
echo "424円以上のアイテム購入順序"
cat leaguedata/${leaguename}/${heroname}/purchasediv.txt
echo ""
echo "試合終了時のアイテム"
cat leaguedata/${leaguename}/${heroname}/itemdiv.txt
echo ""
echo ""
echo "スタート時のアイテム を取ろうとしてますが、現在試合前の購入のアレコレなのかちゃんとれてません。壊れてるので参考しないように"
cat leaguedata/${leaguename}/${heroname}/itemdiv_start_pattern.txt
echo ""
echo "LH distribute"
cat leaguedata/${leaguename}/${heroname}/lhtime.txt
echo ""
echo "XP distribute"
cat leaguedata/${leaguename}/${heroname}/xptime.txt
