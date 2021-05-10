
"""
print('Enter the name of cat 1:')
Cat1 = input()
print('Enter the name of cat 2:')
Cat2 = input()
print('Enter the name of cat 3:')
Cat3 = input()

print('Here are my cats names:', Cat1, Cat2, Cat3)
"""

Catnum =3
Catnamelist = []
times = ''
for times in range(Catnum):
	print('Enter the name of your cat:')
	name = input()
	Catnamelist = Catnamelist + [name] #list concatenation
	
print('Here are my cats names:')
print(Catnamelist) # this would make your print like a list.

for nameprint in Catnamelist:
	print('',nameprint)
