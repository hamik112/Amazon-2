#/bin/sh

for ID in $(cat tracc)
do
	email=`echo $ID | awk -F"," '{print $1}'`
	password=`echo $ID | awk -F"," '{print $2}'`
	rm -rf TransRush/*
	python TransRush.py ${email} ${password}>>TransRush/$email.json
	num=`cat TransRush/$email.json | jq ".ResultList|length" | head -1`
	if [ $num == 0 ] ; then
		echo "" > /dev/null 2>&1
	else
		for((i=1;i<=${num};i++))
		do
			let argnum=$i-1
			ordernum=`cat TransRush/$email.json | jq .ResultList[$argnum].OrderNo | head -1`
			if [ $ordernum != "null" ] ; then
				ProductName=`cat TransRush/$email.json | jq .ResultList[$argnum].ProductName | head -1`
				DeliveryCode=`cat TransRush/$email.json | jq .ResultList[$argnum].DeliveryCode | head -1`
				echo ordernum:$ordernum ProductName:$ProductName DeliveryCode:$DeliveryCode
			fi
		done
	fi
 	#cat TransRush/$email.json | jq ".ResultList"|grep OrderNo |awk -F"\"" '{print $4}'
done
