import json
ListOfItems=[]
item1={}
item1['brand']="Samsung"
item1['model']="A1"
item1['cost']="15299"
ListOfItems.append(item1)
item2={}
item2['brand']="Xiaomi"
item2['model']="Note 8 pro"
item2['cost']="11350"
ListOfItems.append(item2)
item3={}
item3['brand']="Apple"
item3['model']="iphone 10x"
item3['cost']="78999"
ListOfItems.append(item3)


jsonString = json.dumps(ListOfItems)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()