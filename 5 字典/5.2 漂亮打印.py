import pprint #short for Pretty-print

message = 'I like cats and girls. They better be pretty, but that does not REALLY matter'
count = {}
count1 = {1: 'First', 2: 'Second'}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1 # or count[character]+=1

print(count)
pprint.pprint(count) #帮你做了改行，排序
print(count1)
pprint.pprint(count1)
#print(pprint.pformat(count1)) #

