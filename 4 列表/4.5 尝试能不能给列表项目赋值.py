import random
import collections

message = [
	'Hussle',
	'Chocola',
	'Both'
	]

time = 1
newlist = []
inner = ''
Winnername = ''
for time in range(len(message)*10):
	lot = message[random.randint(0,len(message)-1)]
	newlist += [lot]

c=collections.Counter(newlist)
print(c)
print(c.most_common())
