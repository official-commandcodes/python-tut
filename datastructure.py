############ chechking data type

# print(type('Hello'))
# print(type(40))
# print(type(False))


############ STRING

# print("Aren't shoudn't Can't")

# print('''He said, "Aren't can't"''')

# placeholder
# myAge = 14
# myName = 'My name is Abdulkabir.'
# # message = '%s I am %s years old.'
# message = f'{myName} I am {myAge} years old.'

# print(message)

# STRINGS METHODS
str = 'Welcome to Telemu'

print(str.capitalize()) # Welcome to telemu
print(str.count('e'))  # 4
print(str.upper())  # WELCOME TO TELEMU
print(str.lower())  # welcome to telemu
print(str.index('t'))  # 8
print(str.replace('Telemu', 'Iwo'))  # Welcome to Iwo


# PYTHON LIST
primeNumberAndPeople = [2, 'Lawal', 3, 'Yusuff']

print(primeNumberAndPeople[0]) # selecting value from a list
primeNumberAndPeople.append(10)
primeNumberAndPeople.remove(3)
primeNumberAndPeople.clear()
print(primeNumberAndPeople)

# PYTHON TUPLE
names = ('Musa','Khalid','Abdulkabir','Abdulbaaqi')

print(names)

# converting tuple to list
tupleToList = list(names)

print(tupleToList)
print(type(tupleToList))

# converting list to tuple
listToTuple = tuple(tupleToList)

print(listToTuple)
print(type(listToTuple))
