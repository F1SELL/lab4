from json2xml import json2xml
from json2xml.utils import readfromjson

xml_f = open('sheduledop1.xml', 'w', encoding='utf-8')
xml_f.write(json2xml.Json2xml(readfromjson('schedule.json')).to_xml())
