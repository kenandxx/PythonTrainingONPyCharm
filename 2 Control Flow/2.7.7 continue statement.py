while True:
	print('Who are you?')
	name = input()
	if name != 'Master':
		continue
	print('Hi Master, please enter password')
	password = input()
	if password == '123':
		break
print('Access granted')
