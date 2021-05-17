spam = {'name': 'Rui', 'age' : 23}

a = 'name' in spam.keys()
print(a)

print('Rui' in spam.values())

print('color' in spam.keys())

print('color' not in spam.keys())

print('name' in spam) #不指明是keys还是values的时候，默认是keys


