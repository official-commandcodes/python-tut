# list = [2,7,'Bako',9,'Musa']
# list.append(30)
# list.append('Yam')
# list.append('Cool')
# list.prepend(30)

# print(list)

# numbers =list(range(5))
# number = (2,7,'Bako',9,'Musa')


# print(number[3])

# dictionary

# keys = [1,2,3,4,5,6,7]
# values = ['Bako','Musa','Adekunle','Ayofe']

# dict = {}

# for key, value in zip(keys,values):
#     dict[key] = value

# print(dict)

# MIVA EXERCISE
# TASK 1
# 1
COVID_19 = {
    "Burundi": 694,
    "Ethiopia": 113295,
    "Ghana": 52198,
    "Kenya": 88380,
    "Nigeria": 68937,
    "Rwanda": 6129,
    "Somalia": 4525,
    "South_Sudan": 3166,
    "Sudan": 19196,
    "Uganda": 22499,
}

# print(COVID_19)

# 2
num_keys = len(COVID_19.keys())

# 3
del COVID_19["Nigeria"]

# print(COVID_19)

# 4
COVID_19["Tanzania"] = 509

# print(COVID_19)

# TASK 2
# 1
food = {
    "fruits": ["apples", "oranges", "pears", "mangoes"],
    "vegetables": ["tomatoes", "lettuce", "spinach", "green peppers"],
    "meat": ["chicken", "fish", "beef", "ostrich"],
    "dairy": ["yogurt", "milk", "cheese", "ice-cream"],
}

# 2
len(food.keys())

# 3
for value in food.values():
    print(value)

# 4
spin = food["vegetables"][2]

# 5 
food['fruits'].append('grapes')
