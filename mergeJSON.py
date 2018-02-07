import json, os, os.path;

print len(os.listdir('.'));

with open('1.json') as json_data:
    d = json.load(json_data)
    print (d)
