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
