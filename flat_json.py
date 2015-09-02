#! /usr/bin/python3

import json, re, collections, pyperclip

objs = []

def walk(node, props = []):
    for key, item in node.items():
        if type(item) is dict:
            walk(item, props + [key])
        elif type(item) is list:
            for i in range(3):
                walk(item[0], props + [key, str(i)])
        else:
            name = ' '.join(props + [key]).title()
            name = re.sub('_+', ' ', name)
            name = re.sub('Id', 'ID', name)
            name = re.sub('Url', 'URL', name)
            # If a numeric value is found, adds 1 and move to end
            name = re.sub(
                '(.+)(\s\d)(\s.+)',
                lambda m: m.groups()[0] + m.groups()[2] + ' ' + str((int(m.groups()[1]) + 1)),
                name
            )

            newObj = {}
            newObj['key'] = '__'.join(props + [key])
            newObj['name'] = name

            objs.append(newObj);

txt = pyperclip.paste()            
data = json.loads(txt)
for node in data:
    walk(node)

pyperclip.copy(json.dumps(objs, indent = 2, sort_keys = True))
