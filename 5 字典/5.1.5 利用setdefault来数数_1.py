spam = { 'name': 'Pooka', 'age': 5 }
if 'color' not in spam:
	spam['color'] = 'black'
print(spam)

spam = { 'name': 'Pooka', 'age': 5 }
spam.setdefault('color', 'Black')
print(spam)

spam.setdefault('color', 'WHITE')
print(spam)
