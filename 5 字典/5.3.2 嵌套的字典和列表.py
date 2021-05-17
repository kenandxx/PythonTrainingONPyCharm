itemdic = {'Lisa':{'Apple':3, 'Pear':5}, 'Ken':{'Cake':1, 'Coke':5} }
print(itemdic['Lisa']) #must be [ ]
print(itemdic.keys())
print(itemdic.values())
print(itemdic.items())
print()
print(itemdic['Lisa'].keys())
print(itemdic['Lisa'].values())
print(itemdic['Lisa'].items())

#print('Lisa items' + str(itemdic['Lisa'].items()))
print(itemdic['Lisa'].get('Apple'))

itemnum = 0
itemnum = itemdic['Lisa'].get('Apple') + itemdic['Lisa'].get('Pear')
print(itemnum)
dicname = {}

def getnum(keyname, valuename):
    num = 0
    for i, v in keyname.items():
        num = v.get(valuename)
    return num

#print('Lisa bring' + str(getnum('Lisa','Apple')))






