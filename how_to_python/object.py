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
