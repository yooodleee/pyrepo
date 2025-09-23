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
iter(5)
# output: TypeError: 'int' object is not iterable

iter([1, 2, 3])
# output: <list_iterator at 0x25926889160>


# %%
def isIterable(obj):
    try:
        _ = iter(obj)
    except TypeError:
        print(type(obj), "is not an iterable")
    else:
        print(type(obj), "is an iterable")


isIterable(5)
# output: <class 'int'> is not an iterable

isIterable([1, 2, 3])
# output: <class 'list'> is an iterable

isIterable("Hello")
# output: <class 'str'> is an iterable

isIterable((1, 2, 3))
# output: <class 'tuple'> is an iterable

isIterable({"one": 1, "two": 2})
# output: <class 'dict'> is an iterable

isIterable(range(3)) 
# output: <class 'range'> is an iterable

isIterable(map(int, ["1", "2"]))
# output: <class 'map'> is an iterable

isIterable(zip([1, 2], [3, 4]))
# output: <class 'zip'> is an iterable

isIterable(filter(bool, [1, None]))
# output: <class 'filter'> is an iterable

isIterable(enumerate([1, 2, 3]))
# output: <class 'enumerate'> is an iterable

isIterable(reversed("Hello")) 
# output: <class 'reversed'> is an iterable


# %%
