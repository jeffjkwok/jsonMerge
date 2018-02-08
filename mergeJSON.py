import json, os, os.path, glob;

# length = len(os.listdir('./data'));
allData = [];

jsonLength = len(glob.glob1("./data", "*.json"))
print jsonLength

for x in xrange (1, jsonLength + 1):
    path = "./data/JSON" + str(x) + ".json"
    with open(path) as json_data:
        data = json.load(json_data)
        allData.append(data)

# print allData
print len(allData)

# with open('1.json') as json_data:
#     d = json.load(json_data)
#     print (d)
