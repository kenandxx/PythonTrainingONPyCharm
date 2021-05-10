import random

message = [
	'Hussle',
	'Chocola',
	'Both'
	]

time = 1
newlist = []
timelist = []
HussleTime = 0
ChocolaTime = 0
BothTime = 0
inner = ''
Winnername = ''
while time <= len(message)*2:
	lot = message[random.randint(0,len(message)-1)]
	if lot == 'Hussle':
		HussleTime +=1
	elif lot == 'Chocola':
		ChocolaTime += 1
	elif lot == 'Both':
		BothTime += 1
	
	
			
	newlist = newlist + [lot]
	newlist.sort()
	print('Lot time', time, 'is :', lot)
	print(newlist, end = '\n\n')
	time += 1

# 找出赢家：但是这个方法在出现等值的时候会优先到Hussle
winner = max(HussleTime, ChocolaTime, BothTime)
while True:  
	if winner == HussleTime:
		Winnername = 'Hussle'
		break
	if winner == ChocolaTime:
		Winnername = 'Chocola'	
		break
	if winner == BothTime:
		Winnername = 'Both'
		break

#建立抽签次数合计后的list以便简单打印
timelist = [HussleTime]+[ChocolaTime]+[BothTime]


print('Here is your TODAY GIRL LOT resule:')

printtime = ''
for printtime in range(len(message)): #range(3) outputs 0,1,2
	print(message[printtime], 'lot time is:', timelist[printtime])

	
	# print('Chocola lot time is:', ChocolaTime)
	# print('Both lot time is:', BothTime)

print('Today, you will go to:', Winnername)
	

	
	
