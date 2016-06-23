#!/bin/sh

case "$1" in
	session)
		cat tmp.xml |grep sessionId |head -1|awk -F"'" '{print $4}'
		;;
	address)
		cat tmp.xml |grep addressID_ |head -1|awk -F"\"" '{print $10}'
  		;;
	id)
		cat tmp.xml |grep addressID_ |head -1|awk -F"\"" '{print $10}'|awk -F"_" '{print $2}'
		;;
	payment)
		cat tmp2.html |grep "type=\"radio\" name=\"paymentMethod\" id=\""|awk -F"\"" '{print $6}'|awk -F"." '{print $2}'
		;;
	monnum)
		ps aux | grep "python amazon" |grep pts |grep -v grep | wc -l
		;;
	monasin)
		asin=`ps aux | grep "python amazon" |grep pts |grep -v grep | awk '{print $13}' | sed ':a;N;s/\n/;/;ta'`
		if [ -n "$asin" ] ;then
			echo $asin
		else
			echo "NULL"
		fi
		;;
	killasin)
		kill -9 `ps aux|grep "python amazon"|grep -v grep|grep pts|grep $2|awk -F" " '{print $2}'`
		echo $?
		;;
	asinpriceDE)
		cat DE.ail |grep $2|awk -F";" '{print $3}'
		;;
	asinpriceJP)
		cat JP.ail |grep $2|awk -F";" '{print $3}'
		;;
	getprice)
		cat data|grep priceblock_ourprice|grep "￥" | awk -F">" '{print $2}'|awk -F"<" '{print $1}'|awk '{print $2}'|sed 's/,//g'

esac
