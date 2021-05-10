import random

print('I am thinking a number between 1 and 20. Take a guess.')

mynumber = random.randint(1,5)
guesstimes = 1 #用来控制可猜次数
a = 4 #用来控制可猜次数
while guesstimes <= a:
	print('Take a guess. This is Time '+ str(guesstimes)+'.')
	try : #为了防止用户输入非数字
		num = int(input())
	except :
		print('Enter a number, Dud!')
		continue #用户如果输入非数字，就返回开头，则guesstime = guesstime+1不会执行，即可猜次数不会减少
	if num < mynumber:
		print('Your guess is too low.\n')
	elif num > mynumber:
		print('Your guess is too high.\n')
	elif num == mynumber:
		break
	guesstimes = guesstimes+1

if num == mynumber:
	print('Good Job! You guessed my number in '+ str(guesstimes) + ' times')
else :
	print('You misses it!')
