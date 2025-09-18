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
assert urgencies["Laundry"] == 3
assert urgencies["Homework"] == 5


# %%
urgencies["Homeworks"]
# output: KeyError: 'Homeworks'


# %%
if "Homework" in urgencies: 
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

retrieve_urgency("Homework")
# output: 5

retrieve_urgency("Homeworks")
# output: 'N/A'


# %%
urgencies.get("Homework")
# output: 5

urgencies.get("Homeworks", "N/A")
# output: 'N/A'

urgencies.get("Homeworks")
# output: None


# %%
def calculate_something(arg0, arg1, **kwargs):
    kwarg0 = kwargs.get("kwarg0", 0)
    kwarg1 = kwargs.get("kwarg1", "normal")
    kwarg2 = kwargs.get("kwarg2", [])
    kwarg3 = kwargs.get("kwarg3", "text")


calculate_something(arg0, arg1)
calculate_something(arg0, arg1, kwarg0=5)
calculate_something(arg0, arg1, kwarg0=5, kwarg3="text")


# %%
from timeit import timeit

for count in [10, 100, 1000, 10000, 100000]:
    setup_str = f"""from random import randint; n = {count}; numbers_set = set(range(n)); numbers_list = list(range(n))"""

    stmt_set = "randint(0, n - 1) in numbers_set"
    stmt_list = "randint(0, n - 1) in numbers_list"

    t_set = timeit(stmt_set, setup=setup_str, number=10000)
    t_list = timeit(stmt_list, setup=setup_str, number=10000)

    print(f"{count: >6}: {t_set:e} VS. {t_list:e}")

# # output:
#     10: 2.965400e-03 VS. 2.833500e-03
#    100: 2.570800e-03 VS. 4.993500e-03
#   1000: 2.921200e-03 VS. 2.558300e-02
#  10000: 3.096000e-03 VS. 2.309046e-01
# 100000: 3.072600e-03 VS. 2.240059e+00


# %%
hash("Hello World!")
# output: 

hash(100)
# output: 

hash([1, 2, 3])
# output: TypeError: unhashable type: 'list'.

hash({1: 'one', 2: 'two'})
# output: TypeError: unhashable type: 'dict'

hash((1, 2, 3))
# output: 


# %%
from collections.abc import Hashable


def check_hashability():
    items = [{"a": 1}, [1], {1}, 1, 1.2, "test", (1, 2), True, None]

    for item in items:
        print(f"{str(type(item)): <18} | {isinstance(item, Hashable)}")


print(f"{'Data Type:': <18} {'Hashable'}")
check_hashability()

# # output: 
# Data Type:         Hashable
# <class 'dict'>     | False
# <class 'list'>     | False
# <class 'set'>      | False
# <class 'int'>      | True
# <class 'float'>    | True
# <class 'str'>      | True
# <class 'tuple'>    | True
# <class 'bool'>     | True
# <class 'NoneType'> | True


# %%
text = "Hello, World."

text[-1] = "!"
# output: TypeError: 'str' object does not support item assignment


# %%
text.replace(".", "!")
# output: 'Hello, World!'


# %%
good_stocks = ["AAPL", "GOOG", "AMZN", "NDVA"]
client0 = ["GOOG", "AMZN"]
client1 = ["AMZN", "SNAP"]


# %%
def all_contained_in_recommended(recommended, personal):
    print(f"Is {personal} contained in {recommended}")

    for stock in personal:
        if stock not in recommended:
            return False
    
    return True

print(all_contained_in_recommended(good_stocks, client0))
# output: Is ['GOOG', 'AMZN'] contained in ['AAPL', 'GOOG', 'AMZN', 'NDVA'] 
True

print(all_contained_in_recommended(good_stocks, client1))
# output: Is ['AMZN', 'SNAP'] contained in ['AAPL', 'GOOG', 'AMZN', 'NDVA']
False


# %%
good_stocks_set = set(good_stocks)

contained0 = good_stocks_set.issuperset(client0)
print(f"Is {client0} conatined in {good_stocks}? {contained0}")
# output: Is ['GOOG', 'AMZN'] conatined in ['AAPL', 'GOOG', 'AMZN', 'NDVA']? True


contained1 = good_stocks_set.issuperset(client1)
print(f"Is {client1} contained in {good_stocks}? {contained1}")
# output: Is ['AMZN', 'SNAP'] contained in ['AAPL', 'GOOG', 'AMZN', 'NDVA']? False


# %%
def contained_any_in_recommended(recommended, personal):
    print(f"Does {personal} contain any in {recommended}?")

    for stock in personal:
        if stock in recommended:
            return True
    
    return False


print(contained_any_in_recommended(good_stocks, client0))
# output: Does ['GOOG', 'AMZN'] contain any in ['AAPL', 'GOOG', 'AMZN', 'NDVA']?
True


print(contained_any_in_recommended(good_stocks, client1))
# output: Does ['AMZN', 'SNAP'] contain any in ['AAPL', 'GOOG', 'AMZN', 'NDVA']?
True


# %%
good_stocks_set & set(client0)
# output: {'AMZN', 'GOOG'}

bool(good_stocks_set & set(client0))
# output: True

good_stocks_set & set(client1)
# output: {'AMZN'}

bool(good_stocks_set & set(client1))
# output: True


# %%
good_stocks_set.intersection(client0)
# output: {'AMZN', 'GOOG'}

good_stocks_set.intersection(client1)
# output: {'AMZN'}


# %%
