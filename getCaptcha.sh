#!/bin/sh
xmlfile=$1
python xml2json.py $xmlfile|jq ".Root.Result"|awk -F"\"" '{print $2}'
