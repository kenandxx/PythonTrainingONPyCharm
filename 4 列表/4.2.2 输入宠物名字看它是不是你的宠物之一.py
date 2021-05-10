Girls = ['Kaname', 'Hina', 'Ami', 'Yu', 'Sarina', 'Mero', 'Akari', 'Miria','Nana', 'Hana', 'Mina', 'Natsumi', 'Sarina']


WannaGirl = ['Hinata', 'Ritsuka']

print('Enter a name to check whether she is in your girl list.\nEnter stop if you wanna exit.')

while True:
	girl = input()
	if girl in Girls:
		print('Confirmed that she is your girl!')
	elif girl == 'stop':
		break
	else:
		print('Oh, you have not met her yet!')

		
	
