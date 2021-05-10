def bacon():
	eggs = 'bacon local'
	print(eggs)
bacon() 
	
def spam():
	eggs = 'spam local'
	bacon() # bacon local
	print(eggs) # spam local
	
spam()

eggs = 'global'
print(eggs)

print()

def testgolableggs ():
	print(eggs)

testgolableggs()
