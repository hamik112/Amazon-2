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
esac
