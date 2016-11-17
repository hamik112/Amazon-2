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
	getloginT)
		lasttime=`cat LoginStatus |tail -1|awk -F";" '{print $1}'`
		nowtime=`date '+%s'`
		num=$[ $nowtime - $lasttime ]
		echo $num
		;;
	getofferid)
		cat $2 |grep 'id="offerListingID" name="offerListingID"'|awk -F"\"" '{print $8}'
		;;
	mob_de_getprice)
		cat $2 |grep "</b>&nbsp;EUR"|awk -F"EUR " '{print $2}'|awk -F"&nbsp;" '{print $1}'|sed 's/,/./g'
		;;
	mob_jp_getprice)
		cat $2 |grep "i:&nbsp;" |awk -F"\\" '{print $2}'|awk -F"<" '{print $1}'|sed 's/,//g'
		;;
	getjsonofferid)
		cat $2 | grep offerListingID | sed 's/\\//g' | awk -F"'" '{print $4}'
		;;
	getJPoffid)
		cat $2 | sed "s/'+String.fromCharCode(0x27)+'//g" | sed "s/'+String.fromCharCode(0x0A)+'//g" | sed 's/ //g' | grep offerListingID |awk -F":" '{print $2}' |awk -F"," '{print $1}'
		;;
	getPriceStatus)
		cat $2 | grep "submit.addToCart"
		;;
	getListOid)
		cat $2 | grep -C 5 "/gp/aw/c.html/ref=olp_atc_new_1" | grep oid | head -n 1 | awk -F'"' '{print $ 6}'
		;;
	getTigerStatus)
		cat $2|grep spec_stock_msg | awk -F">" '{print $2}' | awk -F"<" '{print $1}'
		;;
	sendmail)
		echo "狮子上货---虎牌官网" | mail -s "Tiger in Stock" 2438622910@qq.com,159945@qq.com
		;;
	sendmailRosman)
		case "$2" in
		aptamil1+)
			echo "徳爱1+上货---R家" | mail -s "Aptamil 1+ (5*600g) in Stock" 2438622910@qq.com,719203291@qq.com,1918025591@qq.com,728066927@qq.com,1046839810@qq.com,553465002@qq.com,317847903@qq.com
			;;
		aptamil2+)
			echo "徳爱2+上货---R家" | mail -s "Aptamil 2+ (5*600g) in Stock" 2438622910@qq.com,719203291@qq.com,1918025591@qq.com,728066927@qq.com,1046839810@qq.com,553465002@qq.com,317847903@qq.com
			;;
		HA3)
			echo "徳爱HA3上货---R家" | mail -s "Aptamil HA3 (4*600g) in Stock" 2438622910@qq.com,305911192@qq.com
			;;
		esac
		;;
	getajax)
		cat $2 |grep "ajaxUrlParams"
		;;
	getprice)
		cat $2|grep priceblock_ourprice|grep "￥" | awk -F">" '{print $2}'|awk -F"<" '{print $1}'|awk '{print $2}'|sed 's/,//g'

esac
