#! /usr/bin/python3

import json, re, collections, pyperclip

objs = []

def walk(node, props = []):
    for key, item in node.items():
        if type(item) is dict:
            walk(item, props + [key])
        else:
            name = ' '.join(props + [key]).title()
            name = re.sub('_+', ' ', name)
            name = re.sub('Id', 'ID', name)
            name = re.sub('Url', 'URL', name)

            newObj = {}
            newObj['key'] = '__'.join(props + [key])
            newObj['name'] = name

            objs.append(newObj);

txt = pyperclip.paste()            
data = json.loads(txt)
for node in data:
    walk(node)

pyperclip.copy(json.dumps(objs, indent = 2, sort_keys = True))
