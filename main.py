#print(''.join(open('schedule.json', 'r', encoding='utf-8').readlines()))
json_file = [i.strip().rstrip(',').replace('"', '') for i in open('schedule.json', 'r', encoding='utf-8').readlines()]
#print(json_file)
json_len = len(json_file)
json_ind = 0

def read_dict():
	global json_ind

	result = {}
	while json_ind < json_len:
		json_ind +=1
		if json_file[json_ind] == '}':
			return result
		key, value = json_file[json_ind].split(": ")

		if '[' in value:
			value = value.replace('[', '').replace(']', '').split(', ')
			result[key] = value
		elif value == '{':
			result[key] = read_dict()
		else:
			result[key] = value

xml_f = open('schedule.xml', 'w', encoding='utf-8')
xml_tabs = 1

t = ''

def list_to_xml(name, listy):
	global t, xml_tabs
	t += "\t"*xml_tabs + f"<{name}>\n"
	xml_tabs += 1
	for i in listy:
		t += "\t"*xml_tabs + f"<item>{i}</item>\n"
	xml_tabs -=1 
	t += "\t"*xml_tabs + f"</{name}>\n"


		
def dict_to_xml(dicty):
	global xml_tabs, t

	for key, value in dicty.items():
		if type(value) is str:
			t += '\t' * xml_tabs + f"<{key}>{value}</{key}>\n"
		elif type(value) is dict:
			t += '\t' * xml_tabs + f"<{key}>\n"
			xml_tabs +=1
			dict_to_xml(value)
			xml_tabs -=1 
			t += '\t' * xml_tabs + f'</{key}>\n'
		else:
			list_to_xml(key, value)
t += '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<root>\n'
dict_to_xml(read_dict())
t+= "</root>"
xml_f.write(t)





