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
