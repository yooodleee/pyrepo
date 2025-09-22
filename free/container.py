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
failed_dict = {[0, 2]: "even"}
# output: TypeError: unhashable type: 'list' 

failed_set = {{"a": 0}}
# output: TypeError: unhashable type: 'dict'


# %%
from timeit import timeit

for count in [10, 100, 1000, 10000, 100000]:
    # setup string for check exec time 
    setup_str = f"""from random import randint; n = {count}; numbers_set = set(range(n)); numbers_list = list(range(n))"""

    stmt_set = "randint(0, n - 1) in numbers_set" 
    stmt_list = "randint(0, n - 1) in numbers_list"

    t_set = timeit(stmt_set, setup=setup_str, number=10000)     # time complexity -> O(1) -> hash table(better)
    t_list = timeit(stmt_list, setup=setup_str, number=10000)   # time complexity -> O(n) -> List 

    print(f"{count: >6}: {t_set:e} VS. {t_list:e}")

# # output: 
#     10: 2.616400e-03 VS. 2.748100e-03
#    100: 2.515300e-03 VS. 4.859400e-03
#   1000: 2.777400e-03 VS. 2.555810e-02
#  10000: 3.149900e-03 VS. 2.169713e-01
# 100000: 3.178300e-03 VS. 2.213404e+00


# %%
hash("Hello World!")
# output: -718917682246089082

hash(100)
# output: 100

hash([1, 2, 3])
# output: TypeError: unhashable type: 'list'

hash({1: 'one', 2: 'two', 3: 'three'})
# output: TypeError: unhashable type: 'dict'

hash((1, 2, 3))
# output: 529344067295497451

hash({1, 2, 3})
# output: TypeError: unhashable type: 'set'


# %%
from collections.abc import Hashable

def check_hashability():
    # dict, list, set, int, float, str, tuple, bool, None => Multiple type in items
    items = [{"a": 1}, [1], {1}, 1, 1.2, "test", (1, 2), True, None]

    for item in items:
        # return boolean 
        print(f"{str(type(item)): <18} | {isinstance(item, Hashable)}")


print(f"{'Data Type': <18} {'Hashable'}")
check_hashability()

# # output: 
# Data Type          Hashable
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
text = "Hello, World!"  # str also immutable data

text[-1] = "."
# output: TypeError: 'str' object doest not support item assignment

text.replace("!", ".")
# output: 'Hello, World.'


# %%
good_stocks = ["APPL", "GOOG", "AMZN", "NDVA"]
client0 = ["GOOG", "AMZN"]
client1 = ["AMZN", "SNAP"]

def all_contained_in_recommended(recommended, personal):
    print(f"Is {personal} contained in {recommended}")

    for stock in personal:
        if stock not in recommended:    # bad case -> Time Complexity: O(n)
            return False
    
    return True


print(all_contained_in_recommended(good_stocks, client0))
# output: Is ['GOOG', 'AMZN'] contained in ['APPL', 'GOOG', 'AMZN', 'NDVA'] True

print(all_contained_in_recommended(good_stocks, client1))
# output: Is ['AMZN', 'SNAP'] contained in ['APPL', 'GOOG', 'AMZN', 'NDVA'] False


# %%
good_stocks_set = set(good_stocks)  # generate set instance => better case -> Time Compleixty(O(1))

contained = good_stocks_set.issuperset(client0) # whether this set contains another set.
print(f"Is {client0} contained in {good_stocks}? {contained}")
# output: Is ['GOOG', 'AMZN'] contained in ['APPL', 'GOOG', 'AMZN', 'NDVA']? True

contained1 = good_stocks_set.issuperset(client1)
print(f"Is {client1} contained in {good_stocks}? {contained1}")
# output: Is ['AMZN', 'SNAP'] contained in ['APPL', 'GOOG', 'AMZN', 'NDVA']? False


# %%
def contained_any_in_recommended(recommended, personal):
    print(f"Does {personal} contain any in {recommended}")

    for stock in personal:
        if stock in recommended:
            return True
    
    return False


print(contained_any_in_recommended(good_stocks, client0))
# output: Does ['GOOG', 'AMZN'] contain any in ['APPL', 'GOOG', 'AMZN', 'NDVA'] True

print(contained_any_in_recommended(good_stocks, client1))
# output: Does ['AMZN', 'SNAP'] contain any in ['APPL', 'GOOG', 'AMZN', 'NDVA'] True
 
 
# %%
good_stocks_set & set(client0)
# output: {'AMZN','GOOG'}

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
