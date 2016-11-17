#!/bin/sh
for ID in $(cat Ross_acc|awk -F"---" '{print $1}')
do
	#python Rossman_getcookie.py $ID 564549024Zmm
	python Rossman_AddCart.py $ID 564549024Zmm 379924 12
	sleep 10s
done
