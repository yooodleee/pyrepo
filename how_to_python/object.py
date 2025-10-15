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
