#! /usr/bin/python3

import json, re, collections, pyperclip

objs = []

def walk(node, props = []):
    for key, item in node.items():
        if type(item) is dict:
            walk(item, props + [key])
        elif type(item) is list:
            for i in range(3):
                if item and type(item[0]) is dict:
                    walk(item[0], props + [key, str(i)])
        else:
            label = ' '.join(props + [key])
            label = label[0].upper() + label[1:]
            label = re.sub('_+', ' ', label)
            label = re.sub('Id', 'ID', label)
            label = re.sub('Url', 'URL', label)
            # If a numeric value is found, adds 1 and move to end
            label = re.sub(
                '(.+)(\s\d)(\s.+)',
                lambda m: m.groups()[0] + m.groups()[2] + ' ' + str((int(m.groups()[1]) + 1)),
                label
            )
            # Split camel case
            label = re.sub("([a-z])([A-Z])", "\g<1> \g<2>", label)

            newObj = {}
            newObj['key'] = '__'.join(props + [key])
            newObj['label'] = label

            objs.append(newObj);

txt = pyperclip.paste()            
data = json.loads(txt)
walk(data)

pyperclip.copy(json.dumps(objs, indent = 2, sort_keys = True))
