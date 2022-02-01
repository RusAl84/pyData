import json

fileObject = open("data.json", "r")
jsonContent = fileObject.read()
ListOfItem = json.loads(jsonContent)

#print(ListOfItem)
mincost=11_000
maxcost=30_000
FoundCost=[]
for item in ListOfItem:
    if int(item['cost'])>=mincost and  int(item['cost'])<=maxcost:
        FoundCost.append(item)
FoundU=[]
# print(FoundCost)
minU=20000
maxU=120000
for item in FoundCost:
    if int(item['U'])>=minU and  int(item['U'])<=maxU:
        FoundU.append(item)

print(FoundU)