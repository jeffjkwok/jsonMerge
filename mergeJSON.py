import json, os, os.path, glob;
from datetime import datetime

# length = len(os.listdir('./data'));
allData = [];
devDict = {};

jsonLength = len(glob.glob1("./data", "*.json"))
print jsonLength

for x in xrange (1, jsonLength + 1):
    path = "./data/JSON" + str(x) + ".json"
    with open(path) as json_data:
        data = json.load(json_data)
        # creates key in dictionary for each device
        
        if data['SerialNumber'] not in devDict:
            time = data['TimeCreated'][:-6]
            print datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f')
            
            devDict[data['SerialNumber']] = [data];
        else: 
            devDict[data['SerialNumber']].append(data);
        allData.append(data)

# for each serial number in the dictionary it creates a file with the associated impacts
for key in devDict:
    f = open(key + '.json', "w+")
    f.write(json.dumps(devDict[key], ensure_ascii=False));
    f.close();
print len(allData)
