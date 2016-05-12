#!/bin/sh
date
rm -rf xmlcache/*
echo '*******************************************************************'
echo 'Svn add new user							 '
echo 'zhuhuijunzhj@126.com						 '
echo '*******************************************************************'
for ID in $(cat numlist)
do
	echo ''
	echo "'***********************************************************'"
	echo "'开始获取$ID物流信息					  '"
	echo "'***********************************************************'"	
	python GetHttp.py http://www.transrush.com/Transport/LogisticsTransferTrace.aspx?code=$ID>>xmlcache/$ID
        echo ''
	b=''
        for ((i=0;$i<=100;i+=2))
                do
                        printf " (～ o ～)~zZ:[%-50s]%d%%\r" $b $i
                        sleep 0.1
                        b=#$b
                done
	echo ''
	rm -rf tmp tmp.xml
 	cat xmlcache/$ID |grep "离开海外仓库">>tmp
	python formatxml.py tmp tmp.xml
	cat tmp.xml |sed 's/ //g'|grep ^[^\<]

	
done
