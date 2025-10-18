######################
## Object
######################


# %%
def filter_tasks(tasks, by_urgency):
    pass


# %%
# modified case: introspection(x.urgency == by_urgency)
def filter_tasks(tasks, by_urgency):
    filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered


# %%
# modified case: introspection(x.urgency in by_urgency)
def filter_tasks(tasks, by_urgency):
    filtered = [x for x in tasks if x.urgency in by_urgency]
    return filtered


# %%
# modified case: type
def filter_tasks(tasks, by_urgency):
    if type(by_urgency) is list:
        filtered = [x for x in tasks if x.urgency in by_urgency]
    else:
        filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered

# %%
# modified case: isinstance
def filter_tasks(tasks, by_urgency):
    if isinstance(by_urgency, list):
        filtered = [x for x in tasks if x.urgency in by_urgency]
    else:
        filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered


# %%
# comparison type with isinstance
class User:     # parent class
    pass

class Supervisor(User): # child class
    pass

supervisor = Supervisor()

comparisons = [
    type(supervisor) is User,
    type(supervisor) is Supervisor,
    isinstance(supervisor, User),
    isinstance(supervisor, Supervisor) 
]

comparisons
# output: [False, True, True, True]


# %%
# bad case: NonCollection(abc module)
def filter_tasks(tasks, by_urgency):
    if isinstance(by_urgency, (list, tuple)):
        filtered = [x for x in tasks if x.urgency in by_urgency]
    else:
        filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered


# %%
# better case: Collection(abc module)
from collections.abc import Collection

def filter_tasks(tasks, by_urgency):
    if isinstance(by_urgency, Collection):
        filtered = [x for x in tasks if x.urgency in by_urgency]
    else:
        filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered


# %%
class Task:
    def __new__(cls, *args):
        new_task = object.__new__(cls)
        print(f"__new__ is called, creating an instance at {id(new_task)}")
        return new_task
    
    def __init__(self, title):
        self.title = title
        print(f"__init__ is called, initializing an instance at {id(self)}")


# %%
task = Task("Laundry")

# # output: 
# __new__ is called, creating an instance at 1297088208464
# __init__ is called, initializing an instance at 1297088208464

print(f"task memory address: {id(task)}")
# output: task memory address: 1297088208464


# %%
title_output = f"Title: {task.title}"


# %%
print(globals())    # Return the dictionary containing the current scope's global variables
# output: 


# %%
assert Task is globals()["Task"]    # Task: class object

assert task is globals()["task"]    # task: instance object


# %%
import sys

task = Task("Laundry")

assert sys.getrefcount(task) == 2


# %%
work = {"to_do": task}
assert sys.getrefcount(task) == 3

tasks = [task]
assert sys.getrefcount(task) == 4


# %%
del tasks

assert sys.getrefcount(task) == 3


# %%
work["to_do"] = "nothing"

assert sys.getrefcount(task) == 2


# %%
class Task:
    def __init__(self, title):
        print(f"__init__ is called, initializing an instance at {id(self)}")
        self.title = title
    
    def __del__(self):
        print(f"__del__ is called, destructing an instance at {id(self)}")

task = Task("Homework")
# output: __init__ is called, initializing an instance at 1297106915680

assert "task" in globals()

# %%
del task
# output: __del__ is called, destructing an instance at 1297106915680

assert "task" not in globals()


# %%
title_output = f"Title: {task.title}"
# output: NameError: name 'task' is not defined


# %%
# bad case: 
class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
    
    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r})"
    
    def save_data(self):
        pass

task = Task("Homework", "Math and physics")
task_dict = task.__dict__
task_dict_copied = task_dict.copy() # shallow copy of task_dict

print(task_dict_copied)
# output: {'title': 'Homework', 'desc': 'Math and physics'}


# %%
# better case: copy
from copy import copy

task_copied = copy(task)

print(task_copied)
# output: Task('Homework', 'Math and physics')


# %%
# shallow copy
class Task:
    def __init__(self, title, desc, tags = None):
        self.title = title 
        self.desc = desc
        self.tags = [] if tags is None else tags    # ternary expression
    
    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r}, {self.tags})"
    
    def save_data(self):
        pass

task = Task("Homework", "Math and physics", ["school", "urgent"])
task_copied = copy(task)
print(task_copied)
# output: Task('Homework', 'Math and physics', ['school', 'urgent'])


# %%
task_copied.tags.append("red")
task_copied
# output: Task('Homework', 'Math and physics', ['school', 'urgent', 'red'])


# %%
print(task) 
# expected result: Task('Homework', 'Math and physics', ['school', 'urgent'])
# output: Task('Homework', 'Math and physics', ['school', 'urgent', 'red'])


# %%
# identity test
assert task.tags is task_copied.tags

assert id(task.tags) == id(task_copied.tags)


# %%
# deep copy
from copy import deepcopy

task = Task("Homework", "Math and physics", ["school", "urgent"])
task_deepcopied = deepcopy(task)
task_deepcopied
# output: Task('Homework', 'Math and physics', ['school', 'urgent'])


# %%
task_deepcopied.tags.append("red")
task_deepcopied
# output: Task('Homework', 'Math and physics', ['school', 'urgent', 'red'])

task
# output: Task('Homework', 'Math and physics', ['school', 'urgent'])


# %%
db_filename = "N/A"         # global scope

def set_database(db_name):
    db_filename = db_name   # local scope: db_filename
    print(list(locals()))

print(list(globals()))      # print local scope's instance
# output: 
# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtin__', '__builtins__', '_ih', '_oh', '_dh', 'In', 'Out', 'get_ipython', 'exit', 'quit', 'open', '_', '__', '___', '_VSCODE_types', 'os', '_VSCODE_hashlib', '__VSCODE_wrapped_run_cell', '__VSCODE_compute_hash', '__VSCODE_wrap_run_cell', '__vsc_ipynb_file__', '__file__', '_i', '_ii', '_iii', '_i1', 'db_filename', 'set_database']


# %%
set_database("tasks.sqlite")
# output: ['db_name', 'db_filename']


# %%
# modified case: global keyword
db_filename = "N/A"     # global scope

def set_database(db_name):
    global db_filename  # not local scope's variable
    db_filename = db_name
    print(list(locals()))   # LEGB(global scope: db_name)

set_database("tasks.sqlite")
# output: ['db_name']

print(db_filename)
# output: tasks.sqlite


# %%
# change nonlocal variable
def change_text(using_nonlocal: bool):
    text = "N/A"

    def inner_fun0():
        text = "No nonlocal"        # local scope
    
    def inner_fun1():
        nonlocal text               # nonlocal 
        text = "Using nonlocal"     # enclosing scope variable
    
    inner_fun1() if using_nonlocal else inner_fun0()
    return text

change_text(using_nonlocal=False)   # inner_fun0()
# output: 'N/A'

change_text(using_nonlocal=True)    # inner_fun1()
# output: 'Using nonlocal'


# %%
# class vs. function
def doubler(x):
    return x * 2

assert callable(doubler)    # check callability


# %%
def do_smoething():
    pass

print(do_smoething)
# output:<function do_smoething at 0x0000017DE24473A0>

print(sum)  # built-in function
# output: <built-in function sum>

print(map)
# output: <class 'map'>


# %%
print(map(int, ["1", "2.0", "3"]))
# output: <map object at 0x0000017DE145AA90>


# %%
# bad case: 
cards = [10, 1, "J", "A"]

print(sorted(cards))
# output: '<' not supported between instances of 'str' and 'int'

print(sorted(cards, key=str))
# output: [1, 10, 'A', 'J']


# %%
# better case: user defined class
class PokerOrder(int):
    def __new__(cls, x):    # modified PokerOrder's default operation
        numbers_mapping = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        casted_number = numbers_mapping.get(x, x)
        return super().__new__(PokerOrder, casted_number)   # generate proxy instance

print(sorted(cards, key=PokerOrder))
# output: [1, 10, 'J', 'A']


# %%
import time

def logging_time(func):
    def logger(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")
        return result

    return logger


# %%
# modified case: 
import time

class TimeLogger:
    def __init__(self, func):
        def logger(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f"Calling {func.__name__}: {time.time() - start:.5f}")
            return result
        self._logger = logger       # protected attribute: save logger(inner func)
    
    def __call__(self, *args, **kwargs):    # call dacorated func -> callable class's instance
        return self._logger(*args, **kwargs)

@TimeLogger
def calculate_sum(n):
    return sum(range(n))

result = calculate_sum(100_000)
# output: Calling calculate_sum: 0.00181


# %%
print(calculate_sum)    # class's instance(TimeLogger)
# output: <__main__.TimeLogger object at 0x00000238C9620400>


# %%
