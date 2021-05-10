def spam():
	global eggs
	eggs = 'spam' # this is the global

def bacon():
	eggs = 'bacon' # this is a local

def ham():
	print(eggs) # this is the global

eggs = 42 # this is the global

spam()
print(eggs)

bacon() # bacon调用并不会改变global eggs的值, eggs == 'spam'

print(eggs, end = '\n\n')

ham() # still ham() only print the current global eggs == 'spam'
