spam = ['apple', 'banana', 'tofu', 'cats']


def printlist(listin):
	listin = spam 
	i = 0
	for i in range(len(listin)):
		if i == len(listin) -1:
			print('and ' + listin[i])
		else:
			print(listin[i], end = ', ')
		i += 1
		
printlist(spam)


