Masterboxlist = {'SB06':{'packageweight_g': 10, 'cost_JPY': 15 },'SB08':{'packageweight_g': 20, 'cost_JPY': 25 },}

ships = {'SB06': 100, 'SB08': 200}

def printinventory(key, value):
	print('Here are all your BoxIDs:')
	totalweight = 0
	totalcost = 0
	for key, value in Masterboxlist.items():
		for key2, value2 in value.items():
			if key2 == 'packageweight_g':
				totalweight = totalweight + value2 * ships.get(key, 1)
			elif key2 == 'cost_JPY':
				totalcost = totalcost + value2 * ships.get(key, 1)
			print(' Boxid and its information:', key, key2, value2, '. Its ships is:' + str(ships.get(key) ) )
	print("Your Boxid's totalweight is : " + str(totalweight) )
	print("Your Boxid's totalcost is : " + str(totalcost) )

key1 = []
value1 = []
printinventory(key1, value1)
print()

#以下は追加到字典

def addToMasterboxlist():
	for key, value in addboxid.items():
		Masterboxlist.setdefault(key, value)
def addToship():
	for key, value in addships.items():
		ships.setdefault(key, value)

addboxid = {'CB06':{'packageweight_g': 10, 'cost_JPY': 15 }}
addships = {'CB06': 300}

addToMasterboxlist()
addToship()
printinventory(key1,value1)
