import copy

spam = [1, 2, 3]
ham = copy.copy(spam)

ham[1] = 100

print(spam) #[1, 2, 3]
print(ham) #[1, 100, 3]
