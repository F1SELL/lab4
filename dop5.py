d = eval(open('schedule.json', 'r', encoding='utf-8').read().replace('false', 'False').replace('null', 'None').replace('true', 'True'))

xml_f = open('scheduledop5.wml', 'w', encoding='utf-8')
xml_tabs = 2

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
    if name != None: t += "\t"*xml_tabs + f'<{name}>\n'
    xml_tabs += 1
    for i in listy:
        r_i = check_item(i)
        if r_i[0] == 'list':
            t += "\t"*xml_tabs + f'<item>\n'
            list_to_xml(None, i)
            t += "\t"*xml_tabs +'</item>\n'
        elif r_i[0] == 'dict':
            t += "\t"*xml_tabs + f'<item>\n'
            xml_tabs +=1 
            dict_to_xml(i)
            xml_tabs -=1
            t += "\t"*xml_tabs +'</item>\n'
        else: 
            t += "\t"*xml_tabs + f'<item>{r_i[1]}</item>\n' if r_i[0] != 'null' else "\t"*xml_tabs + f'<item/>\n'
    xml_tabs -=1 
    if name != None: t += "\t"*xml_tabs + f"</{name}>\n"
            
def dict_to_xml(dicty):
    global xml_tabs, t
    for key, value in dicty.items():
        if type(value) is dict:
            t += '\t' * xml_tabs + f'<{key}>\n'
            xml_tabs +=1
            dict_to_xml(value)
            xml_tabs -=1 
            t += '\t' * xml_tabs + f'</{key}>\n'
        elif type(value) is list:
            list_to_xml(key, value)
        else:
            r_i = check_item(value)
            t += '\t' * xml_tabs + f'<{key}>{r_i[1]}</{key}>\n' if r_i[0] != 'null' else "\t"*xml_tabs + f'<{key}/>\n'
        
t += '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<!DOCTYPE wml PUBLIC "-//WAPFORUM//DTD WML 1.1//EN"\n\t"http://www.wapforum.org/DTD/wml_1.1.xml">\n<wml>\n<card id="schedule">\n'
dict_to_xml(d)
t+= "</card>\n</wml>"
xml_f.write(t)


