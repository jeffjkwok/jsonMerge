import json, os, os.path, glob;
from datetime import datetime

allData = [];
devDict = {};

jsonLength = len(glob.glob1("./data", "*.json"))

for x in xrange (1, jsonLength + 1):
    path = "./data/JSON" + str(x) + ".json"
    with open(path) as json_data:
        data = json.load(json_data)
        # creates key in dictionary for each device with a different Serial Number
        if data['SerialNumber'] not in devDict:
            devDict[data['SerialNumber']] = [data];
        else:
            devDict[data['SerialNumber']].append(data);
        allData.append(data)

sortedData = sorted(allData, key = lambda x: datetime.strptime(x['TimeCreated'][:-6], '%Y-%m-%dT%H:%M:%S.%f'))

def createFoldersAndFiles(folderName, sortedData, devDict):
    path = "./" + folderName
    if not os.path.exists(path):
        os.makedirs(path)
    createJSONFiles(sortedData, devDict, path)
    createImpactFiles(sortedData, path)
    print "Finished Printing"

def createJSONFiles(sortedData, devDict, path):
    f = open( path + '/sorted.json', 'w+')
    f.write(json.dumps(sortedData, ensure_ascii = False))
    f.close();
    # prints dictionary for each device with different serial number
    for key in devDict:
        f = open(path + '/' + key + '.json', 'w+')
        f.write(json.dumps(devDict[key], ensure_ascii=False));
        f.close();

def createImpactFiles(sortedData, path):
    impact = 0;
    count = 1;
    lastCut = 0;
    lastTime = datetime.strptime(sortedData[lastCut]['TimeCreated'][:-6], '%Y-%m-%dT%H:%M:%S.%f')
    while count < len(sortedData):
        currentTime = datetime.strptime(sortedData[count]['TimeCreated'][:-6], '%Y-%m-%dT%H:%M:%S.%f')
        diff = currentTime-lastTime
        if diff.total_seconds() > 1:
            impact += 1
            f = open( path + '/impact' + str(impact) + '.json', 'w+')
            f.write(json.dumps(sortedData[lastCut:count], ensure_ascii = False))
            f.close()
            # print count, "index"
            # print sortedData[lastCut:count]
        lastCut = count;
        count += 1
        lastTime = currentTime

createFoldersAndFiles('testfolder', sortedData, devDict)
