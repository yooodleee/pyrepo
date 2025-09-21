###############################
## Data Container 
###############################


# %%
nums = [1, 2, 3]        # mutability of list -> memory overhead
nums 
# output: [1, 2, 3]


# %%
nums.insert(0, 6) # index(0), object(6)
nums 
# output: [6, 1, 2, 3]


# %%
nums.append(4)
nums 
# output: [6, 1, 2, 3, 4]


# %%
nums.extend([5, 6, 7])
nums 
# output: [6, 1, 2, 3, 4, 5, 6, 7]


# %%
nums.append([5, 6, 7])
nums 
# output: [6, 1, 2, 3, 4, 5, 6, 7, [5, 6, 7]]


# %%
nums.remove(5)
nums 
# output: [6, 1, 2, 3, 4, 6, 7, [5, 6, 7]]


# %%
del nums[2]
nums 
# output: [6, 1, 3, 4, 6, 7, [5, 6, 7]]


# %%
integers = (1, 2, 3)    # immutability of tuple -> TypeError, AttributeError
integers.append(4)
# output: 'tuple' object has no attribute 'append'


# %%
integers[0] = 'zero'    # allocate new val to tuple instance
# output: 'tuple' object does not support item assignment


# %%
nums = ([1, 2], [1, 2])
nums[0].append(3)
nums 
# output: ([1, 2, 3], [1, 2])


# %%
nums = ((1, 2), (1, 2))
nums[0].append(3)
nums 
# output: AttributeError: 'tuple' object has no attribute 'append'


# %%
tasks = [
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
    {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]

tasks.sort()
# output: TypeError: '<' not supported between instances of 'dict' and 'dict'


# %%
nums = [5, 7, 1, 2, 4, 8, 6, 9]
nums.sort()     # inplace sorting -> return None
nums 
# output: [1, 2, 4, 5, 6, 7, 8, 9]


# %%
names = ['Danny', 'Aaron', 'Zack', 'Jennifer', 'Mike', 'David']
names.sort(reverse=True)    # inplace sorting -> return None 
names 
# output: ['Zack', 'Mike', 'Jennifer', 'David', 'Danny', 'Aaron']


# %%
mixed = [3, 1, 2, 'John', 'David', 'Danny', 'Aaron']
mixed.sort()
mixed 
# output: '<' not supported between instances of 'str' and 'int'


# %%
# ascending or descending, according to their key function values.
mixed.sort(key=str)
mixed 
# output: [1, 2, 3, 'Aaron', 'Danny', 'David', 'John']


# %%
mixed.sort(key=int)
mixed
# output: ValueError: invalid literal for int() with base 10: 'Aaron'


# %%
mixed = [3, 1, 2, 'John', ['c', 'd'], ['a', 'b']]
mixed.sort(key=str)
mixed 
# output: [1, 2, 3, 'John', ['a', 'b'], ['c', 'd']]


# %%
mixed.sort(key=int)
mixed 
# output: invalid literal for int() with base 10: 'John'


# %%
def using_urgency_level(task):
    return task['urgency']

tasks.sort(key=using_urgency_level, reverse=True)
tasks
# # output: 
# [{'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
#  {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
#  {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}]


# %%
tasks.sort(key=lambda x: x['urgency'], reverse=True)
tasks
# # output: 
# [{'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
#  {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
#  {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}]


# %%
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
    
    # def get_by_title(self):
    #     return self.title
    
    # def get_by_desc(self):
    #     return self.desc
    
    # def get_by_urgency(self):
    #     return self.urgency

task_class = Task('Laundry', 'Wash Clothes', 3) # __dict__
task_class
# output: <__main__.Task at 0x1cd3235ac70>


# %%
from collections import namedtuple

Task = namedtuple('Task', 'title desc urgency') # generate named tuple class
task_nt = Task('Laundry', 'Wash Clothes', 3)    # generate named tuple instance

assert task_nt.title == 'Laundry'               # access to instance's attribute
assert task_nt.desc == 'Wash Clothes'
assert task_nt.urgency == 3


# %%
Task = namedtuple('Task', 'title, desc, urgency')           # better.
Task = namedtuple('Task', ['title', 'desc', 'urgency']) 


# %%
task_data = '''Laundry,Wash Clothes,3
Homework,Physics + Math,5
Museum,Egyptian things,2'''

for task_text in task_data.split('\n'): 
    title, desc, urgency = task_text.split(',')
    task_nt = Task(title, desc, int(urgency))
    print(f"--> {task_nt}")

# # output: 
# --> Task(title='Laundry', desc='Wash Clothes', urgency=3)
# --> Task(title='Homework', desc='Physics + Math', urgency=5)
# --> Task(title='Museum', desc='Egyptian things', urgency=2)


# %%
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}
urgen_keys = urgencies.keys()    # dynamic view instance 
urgen_keys
# output: dict_keys(['Laundry', 'Homework', 'Museum'])

urgen_values = urgencies.values()  # dynamic view instance
urgen_values
# output: dict_values([3, 5, 2])

urgen_items = urgencies.items()   # dynamic view instance
urgen_items
# output: dict_items([('Laundry', 3), ('Homework', 5), ('Museum', 2)])


# %%
urgencies["Park"] = 4
urgen_keys
# output: dict_keys(['Laundry', 'Homework', 'Museum', 'Park'])

urgen_values
# output: dict_values([3, 5, 2, 4])

urgen_items
# output: dict_items([('Laundry', 3), ('Homework', 5), ('Museum', 2), ('Park', 4)])


# %%
# anti-pattern 
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}

urgen_keys_list = list(urgencies.keys())        # not sync with dictionary instance 
urgen_keys_list
# output: ['Laundry', 'Homework', 'Museum'] 

urgencies["Park"] = 4
urgen_keys_list
# output: ['Laundry', 'Homework', 'Museum']


# %%
assert urgencies["Laundry"] == 3
assert urgencies["Homework"] == 5

assert urgencies["Homeworks"] == 4  # wrong access
# output: KeyError: 'Homeworks'


# %%
if "Homework" in urgencies:     # not Pythonic(wrong case)
    urgency = urgencies["Homework"]
else:
    urgency = "N/A"


# %%
def retrieve_urgency(task_title):   
    if task_title in urgencies:
        urgency = urgencies[task_title]
    else:
        urgency = "N/A"
    return urgency

retrieve_urgency('Homework')
# output: 5 

retrieve_urgency('Homeworks')
# output: 'N/A'


# %%
urgencies.get("Homework")   # key: "Homework"
# output: 5

urgencies.get("Homeworks", "N/A")   # key: "Homeworks"(wrong access), default: "N/A"
# output: 'N/A'

urgencies.get("Homeworks") # key: "Homeworks"(wrong access)
# output: None


# %%
def calculate_something(arg0, arg1, **kwargs):  # kwargs: dictionary instance
    kwarg0 = kwargs.get("kwarg0", 0)
    kwarg1 = kwargs.get("kwarg1", "normal")
    kwarg2 = kwargs.get("kwarg2", [])
    kwarg3 = kwargs.get("kwarg3", "text")
    # ...


# calculate_something(arg0, arg1)
# calculate_something(arg0, arg1, kwarg0=5)
# calculate_something(arg0, arg1, kwarg0=5, kwarg3="text")


# %%
