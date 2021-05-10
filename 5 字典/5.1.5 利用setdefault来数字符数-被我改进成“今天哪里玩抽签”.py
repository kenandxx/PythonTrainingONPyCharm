#zifu = 'I like young and beautiful girls. Big tits, tiny tits do not really matter. Play with them, look at thier faces when being touched and licked is kinda a exciting experience'

"""
import random

print(random.randint(0, 1))

zifu = ['Hussle', 'Chocola']
lot = []
i = 0
while i <= 6: #限定次数的抽签循环，每次抽出的结果都放进lot列表
	lot += [zifu[random.randint(0, 1)]]
	print(lot)
	i += 1

count = {} #创造字典以数数

for num in lot:
	count.setdefault(num, 0)
	count[num] += 100
	print(count, end='\n')
"""	
#再简化
import random
zifu = ['Hussle', 'Chocola']
num = []
count = {}
h = 1
while h <= 6:
	for num in [zifu[random.randint(0,1)] ]: #最外层括号是往列表里面添加列表项的命令
		count.setdefault(num, 0)
		count[num] += 1
		print(count)
	h += 1
print('\n' + 'Here is where you should go today:')

keylist = list(count.keys() )
valuelist = list(count.values() )
maxvalue = max(count.values())
maxkeyposition = valuelist.index(maxvalue)
print(' ' + keylist[maxkeyposition] + '!! Its lot number is ' + str(maxvalue) + '.')


	
