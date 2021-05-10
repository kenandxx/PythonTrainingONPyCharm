catname = []

while True:
	print('Enter your cats name:')
	print('Now you are inputing Cat'+str(len(catname)+1) + ':')
	print("Enter 'stop' when you need to")
	name = input()
	if name == 'stop':
		break
	catname = catname + [name]

print('Here are all your cats names')	
for name in catname:
	print(' ' + name)
	
	
