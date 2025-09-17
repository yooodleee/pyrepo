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
task_list = ['Laundry', 'Wash Clothes', 3]                              # List
task_tuple = ('Laundry', 'Wash Clothes', 3)                             # tuple
task_dict = {'title': 'Laundry', 'desc': 'Wash Clothes', 'urgency': 3}  # dictionary


class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

task_class = Task('Laundry', 'Wash Clothes', 3)


# %%
from collections import namedtuple

Task = namedtuple('Task', 'title desc urgency') # generate named tuple class
task_nt = Task('Laundry', 'Wash Clothes', 3)    # generate named tuple instance

assert task_nt.title == 'Laundry'
assert task_nt.desc == 'Wash Clothes'


# %%
Task = namedtuple('Task', 'title, dsec, urgency')
Task = namedtuple('Task', ['title', 'desc', 'urgency'])


# %%
task_data = '''Laundry,Wash Clothes,3
Homework,Physics + Math,5
Museum,Epyptian things,2'''

for task_text in task_data.split('\n'):
    title, desc, urgency = task_text.split(',')
    task_nt = Task(title, desc, int(urgency))
    print(f"--> {task_nt}")

# # output: 
# --> Task(title='Laundry', desc='Wash Clothes', urgency=3)
# --> Task(title='Homework', desc='Physics + Math', urgency=5)
# --> Task(title='Museum', desc='Epyptian things', urgency=2)


# %%
for task_text in task_data.split('\n'):
    task_nt = Task._make(task_text.split(','))


# %%
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}
urgen_keys = urgencies.keys()
urgen_values = urgencies.values()
urgen_items = urgencies.items()

print(urgen_keys, urgen_values, urgen_items, sep="\n")
# # output: 
# dict_keys(['Laundry', 'Homework', 'Museum'])
# dict_values([3, 5, 2])
# dict_items([('Laundry', 3), ('Homework', 5), ('Museum', 2)])


# %%
urgencies["Grocery Shopping"] = 4

print(urgen_keys)
# output: dict_keys(['Laundry', 'Homework', 'Museum', 'Grocery Shopping'])

print(urgen_values)
# output: dict_values([3, 5, 2, 4])

print(urgen_items)
# output: dict_items([('Laundry', 3), ('Homework', 5), ('Museum', 2), ('Grocery Shopping', 4)])


# %%
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}

urgen_keys_list = list(urgencies.keys())
print(urgen_keys_list)
# output: ['Laundry', 'Homework', 'Museum']


# %%
urgencies["Grocery"] = 4
print(urgen_keys_list)
# output: ['Laundry', 'Homework', 'Museum']


# %%
