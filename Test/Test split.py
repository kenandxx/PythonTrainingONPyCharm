name = "Thomas Winter"
LastName = name.split()[0]
print(LastName)

name = "Qi Zhang"
print(name.split(' '))
FirstName, LastName = name.split(' ', 1)

print(LastName)

FirstName_list = []
LastName_list = []
namelist = ['Qi Zhang', 'David Tao']
for Name in namelist:
    FirstName, LastName = Name.split(' ', 1)
    print(FirstName)
    print(LastName)
    FirstName_list.append(FirstName)
    print(FirstName_list)
    LastName_list.append(LastName)
    print(LastName_list)
