#!/usr/bin/python
# -*- coding: utf-8 -*-

import xmltodict;
import json;
import sys

def pythonConversionXmlAndJson(xmlpath):
    """
        demo Python conversion between xml and json
    """
    #1.Xml to Json
#    xmlStr = """
#"""
    file_object = open(xmlpath)
    try:
        xmlStr = file_object.read()
    finally:
        file_object.close()

    convertedDict = xmltodict.parse(xmlStr);
    jsonStr = json.dumps(convertedDict, indent=1);
    print jsonStr;
    
#    #2.Json to Xml
#    dictVal = {
#        'page': {
#            'title': 'King Crimson',
#            'ns': 0,
#            'revision': {
#                'id': 547909091,
#            }
#        }
#    };
#    convertedXml = xmltodict.unparse(dictVal);
#    print "convertedXml=",convertedXml;

###############################################################################
if __name__=="__main__":
    pythonConversionXmlAndJson(sys.argv[1]);
