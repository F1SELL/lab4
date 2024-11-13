import re
json_ind = 0
text = ''.join(open('schedule.json', 'r', encoding='utf-8').readlines())
text = re.sub(r'\"(.+)\": \"(.+)\"', r'<\1>\2</\1>', text)
text = text.replace(',','')
words = re.findall(r'\"(.+)\": {', text)
lists = re.findall(r'\"(.+)\": \[(.+)\]', text)
text = re.sub(r'\"(.+)\": {', r'<\1>', text)

def list_to_xml(data):
	global text
	t = ''
	if data != None:
		name = data[0]
		listik = data[1].split(' ')
		l = re.findall(r'(\s+)\"'+name+'\"', text)[0]
		tabs1 = l.count('\t')
		tabs2 = l.count(' ')
		if tabs1!=0:
			tabs = tabs1*'\t'
		elif tabs2 != 0:
			tabs = tabs2*' '
		t += f"<{name}>\n"
		for i in listik:
			t += tabs + f"\t<item>{i}</item>\n"
		t += tabs + f"</{name}>"
		return t
	else:
		return False
for i in words:
	tab = re.findall(r'(\s+)<'+i+'>', text)[0]
	tabs1 = tab.count('\t')
	tabs2 = tab.count(' ')
	if tabs1!=0:
		tabs = tabs1*'\t'
	elif tabs2 != 0:
		tabs = tabs2*' '
	text = text.replace('\n'+tabs+'}', '\n'+tabs+f"</{i}>", 1)
for i in lists:
	t = list_to_xml(i)
	if t != False:
		text = re.sub(r'\"' + i[0] + r'\": \[.+\]', t, text)
text = re.sub(r'{', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<root>', text)
text = text.replace('}', '</root>')
with open('scheduledop2.xml', 'w', encoding='utf-8') as f:
	f.write(text)




