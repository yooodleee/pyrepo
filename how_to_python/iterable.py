######################################################
## create common data containers using iterables
######################################################


# %%
id_numbers = [101, 102, 103]
titles = ["Laundry", "Homework", "Soccer"]

desired_output = {101: "Laundry", 102: "Homework", 103: "Soccer"}


# %%
desired_output = []
for item in range(len(id_numbers)):     # time compleixty: O(n) -> bad case
    desired_output[id_numbers[item]] = titles[item]


# %%
desired_output = {key: value for key, value in zip(id_numbers, titles)}     # dictionary comprehension


# %%
tasks = ["task0", "task1", "task2"] # iterable(tasks list)

tasks_iterator = iter(tasks)    # iter() -> generate iterator
tasks_iterator
# output: <list_iterator at 0x259268892e0>


# %%
next(tasks_iterator)
# output: 'task0'

next(tasks_iterator)
# output: 'task1'

next(tasks_iterator)
# output: 'task2'

next(tasks_iterator)
# output: StopIteration 


# %%
for task in tasks:  # auto except StopIteration
    print(task)

# output: 
# task0
# task1
# task2


# %%
