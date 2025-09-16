####################################
## Data Container
####################################


# %%
numbers = [1, 2, 3]
print(numbers)
# output: [1, 2, 3]

numbers.insert(0, 0) # index, value
print(numbers)
# output: [0, 1, 2, 3]

numbers.append(4)
print(numbers)
# output: [0, 1, 2, 3, 4]

numbers.extend([5, 6, 7])
print(numbers)
# output: [0, 1, 2, 3, 4, 5, 6, 7]

numbers.remove(5)
print(numbers)
# output: [0, 1, 2, 3, 4, 6, 7]

del numbers[3]
print(numbers)
# output: [0, 1, 2, 4, 6, 7]


# %%
integers_tuple = (1, 2, 3)
integers_tuple.append(4)
# output: AttributeError: 'tuple' has no attribute 'append'

integers_tuple[0] = 'zero'
# output: TypeError: 'tuple' object does not support item assignment


# %%
numbers = ([1, 2], [1, 2])

numbers[0].append(3)

print(numbers)
# output: ([1, 2, 3], [1, 2])


# %%
tasks = [
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
    {'title': 'Homework', 'desc': 'Physics', 'urgency': 5},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]

tasks.sort()
# TypeError: '<' not supported between instances of 'dict' and 'dict'


# %%
numbers = [12, 4, 1, 3, 7, 5, 9, 8]
numbers.sort() 
print(numbers)
# output: [1, 3, 4, 5, 7, 8, 9, 12]

names = ['Danny', 'Aaron', 'Zack', 'Jennifer', 'Mike', 'David']
names.sort(reverse=True)
print(names)
# output: ['Zack', 'Mike', 'Jennifer', 'David', 'Danny', 'Aaron']

mixed = [3, 1, 2, 'John', ['c', 'd'], ['a', 'b']]
mixed.sort()
# output: '<' not supported beween instances of 'str' and 'int'


# %%
mixed = [3, 1, 2, 'John', ['c', 'd'], ['a', 'b']]

mixed.sort(key=str)

print(mixed)
# output: [1, 2, 3, 'John', ['a', 'b'], ['c', 'd']]


# %%
tasks = [
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
    {'title': 'Homework', 'desc': 'Physics', 'urgency': 5},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]

def using_urgency_level(task):
    return task['urgency']

tasks.sort(key=using_urgency_level, reverse=True)
print(tasks)
# output: [{'title': 'Homework', 'desc': 'Physics', 'urgency': 5}, {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}, {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}]


# %%
tasks.sort(key=lambda x: x['urgency'], reverse=True)
print(tasks)
# output: [{'title': 'Homework', 'desc': 'Physics', 'urgency': 5}, {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}, {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}]


# %%
