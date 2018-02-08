import json, os, os.path;

length = len(os.listdir('.'));
allData = [];
print length
for x in xrange (1, length + 1):
    print x


with open('1.json') as json_data:
    d = json.load(json_data)
    print (d)
