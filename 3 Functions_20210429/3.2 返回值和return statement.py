#函数调用求值的结果，称为函数的“返回值”

import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is a certain'
	elif answerNumber == 2:
		return 'It is decidely so'
	elif answerNumber == 3:
		return 'Yes'
 
r = random.randint(1,3) #1-3 之间的随机:
fortune = getAnswer(2)
print(fortune)
