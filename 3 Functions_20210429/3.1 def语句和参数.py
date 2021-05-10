def hello(name):
	print('hello '+ name)

hello('Alice')
hello('Bob')
hello('123')


print('\n')

# error! keep it for future
def hello2(name):
	print('hello '+ int(name))
	
hello('123')

