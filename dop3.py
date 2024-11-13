d = eval(open('schedule.json', 'r', encoding='utf-8').read().replace('false', 'False').replace('null', 'None').replace('true', 'True'))

xml_f = open('scheduledop3.xml', 'w', encoding='utf-8')
xml_tabs = 1

t = ''
def check_item(item):
	if type(item) is str:
		return ('str', item)
	elif item == True and type(item) is not int:
		return ('bool', 'true')
	elif item == False:
		return ('bool', 'false')
	elif item == None:
		return ('null', 'null')
	elif type(item) is int:
		return ('int', item)
	elif type(item) is float:
		return ('float', item)
	elif type(item) is dict:
		return ('dict', item)
	elif type(item) is list:
		return ('list', item)
	elif type(item) is int:
		return ('int', item)
	elif type(item) is float:
		return ('float', item)
def list_to_xml(name, listy):
	global t, xml_tabs
	if name != None: t += "\t"*xml_tabs + f'<{name} type="list">\n'
	xml_tabs += 1
	for i in listy:
		r_i = check_item(i)
		if r_i[0] == 'list':
			t += "\t"*xml_tabs + f'<item type="list">\n'
			list_to_xml(None, i)
			t += "\t"*xml_tabs +'</item>\n'
		elif r_i[0] == 'dict':
			t += "\t"*xml_tabs + f'<item type="dict">\n'
			xml_tabs +=1 
			dict_to_xml(i)
			xml_tabs -=1
			t += "\t"*xml_tabs +'</item>\n'
		else: 
			t += "\t"*xml_tabs + f'<item type="{r_i[0]}">{r_i[1]}</item>\n' if r_i[0] != 'null' else "\t"*xml_tabs + f'<item type="{r_i[1]}"/>\n'
	xml_tabs -=1 
	if name != None: t += "\t"*xml_tabs + f"</{name}>\n"
			
def dict_to_xml(dicty):
	global xml_tabs, t
	for key, value in dicty.items():
		if type(value) is dict:
			t += '\t' * xml_tabs + f'<{key} type="dict">\n'
			xml_tabs +=1
			dict_to_xml(value)
			xml_tabs -=1 
			t += '\t' * xml_tabs + f'</{key}>\n'
		elif type(value) is list:
			list_to_xml(key, value)
		else:
			r_i = check_item(value)
			t += '\t' * xml_tabs + f'<{key} type="{r_i[0]}">{r_i[1]}</{key}>\n' if r_i[0] != 'null' else "\t"*xml_tabs + f'<{key} type="{r_i[1]}"/>\n'
		
t += '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<root>\n'
dict_to_xml(d)
t+= "</root>"
xml_f.write(t)


