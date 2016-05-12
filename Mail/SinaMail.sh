#/bin/sh


for ID in $(cat SinaMail|awk -F"----" '{print $1}'|awk -F"@" '{print $1}')
do

	MailPass=`cat SinaMail|grep $ID|awk -F"----" '{print $2}'`
	echo $ID $MailPass
	python SinaMail.py $ID $MailPass

done

