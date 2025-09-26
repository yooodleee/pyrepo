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
# generate instance with literal
list_obj = [1, 2, 3]

tuple_obj = (404, "Connection Error")

dict_obj = {"one": 1, "two": 2}

set_obj = {1, 2, 3}


# %%
## generate new collection instance with iterable
integers_list = list(range(10))
assert integers_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

integers_tuple = tuple(integers_list)
assert integers_tuple == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

dict_items = [("zero", 0), ("one", 1), ("two", 2)]
integers_dict = dict(dict_items)
assert integers_dict == {'zero': 0, 'one': 1, 'two': 2}

even_numbers = (-2, 4, 0, 2, 4, 2)
unique_evens = set(even_numbers)
assert unique_evens == {0, 2, 4, -2}


# %%
numbers_str = ["1.23", "4.56", "7.89"]

numbers_float = list(map(float, numbers_str))   # generate map iterator 

assert numbers_float == [1.23, 4.56, 7.89]


# %%
zipped_tasks = dict(zip(id_numbers, titles))    # couple with iterables -> id_numbers: key, titles: value 

assert zipped_tasks == {101: "Laundry", 102: "Homework", 103: "Soccer"}


# %%
from collections import namedtuple

Task = namedtuple("Task", "title, desc, urgency")   # generate use defined class with namedtuple

tasks = [
    Task("Homework", "Physics and math", 5),
    Task("Laundry", "Wash Clothes", 3),
    Task("Museum", "Egypt exhibit", 4)
]


# %%
# bad case
task_titles = []
for task in tasks:
    task_titles.append(task.title)  # time compleixty: O(n)

assert task_titles == ['Homework', 'Laundry', 'Museum']


# %%
# better case(list comprehension)
titles = [task.title for task in tasks]

assert titles == ['Homework', 'Laundry', 'Museum']


# %%
# user defined method -> bad case
def get_title(task):
    return task.title

titles = list(map(get_title, tasks))


# %%
# functional programming -> list() + map()
titles = list(map(lambda x:x.title, tasks))


# %%
# dictionary comprehension
title_dict0 = {}
for task in tasks: 
    title_dict0[task.title] = task.desription

title_dict1 = {task.title: task.description for task in tasks}

assert title_dict0 == title_dict1


# %%
# set comprehension
title_set0 = set()

for task in tasks:
    title_set0.add(task.title)

title_set1 = {task.title for task in tasks}

assert title_set0 == title_set1 == {'Homework', 'laundry', 'Museum'}


# %%
numbers = [-3, -2, -1, 0, 1, 2, 3]

squares = [x * x for x in numbers]

assert squares == {0, 1, 4, 9}


# %%
# bad case -> non comprehension 
filtered_titles0 = []
for task in tasks:
    if task.urgency > 3:
        filtered_titles0.append(task.title)

assert filtered_titles0 == ['Homework', 'Museum']


# %%
# better case -> filtering condition (if)
filtered_titles1 = [task.title for task in tasks if task.urgency > 3]   # if filtering

assert filtered_titles0 == filtered_titles1


# %%
flattened_items0 = []
for task in tasks:
    for item in task:
        flattened_items0.append(item)

assert flattened_items0 == ['Homework', 'Physics and math', 5, 'Laundry',
                            'Wash Clothes', 3, 'Museum', 'Egypt exhibit', 4]


# %%
flattened_items1 = [item for task in tasks for item in task]

assert flattened_items0 == flattened_items1


# %%
from collections import namedtuple

Task = namedtuple("Task", "title description urgency")
tasks = [
    Task("Homework", "Physics and math", 5),
    Task("Laundry", "Wash clothes", 3),
    Task("Museum", "Egypt exhibit", 4)
]

# Task 1: task1_title task1_description task1_urgency
# Task 2: task2_title task2_description task2_urgency
# Task 3: task3_title task3_description task3_urgency

for task_i in range(len(tasks)):
    task = tasks[task_i]
    task_counter = task_i + 1
    print(f"Task {task_counter}: {task.title:<10} {task.description:<18} {task.urgency}")

# # output: 
# Task 1: Homework   Physics and math   5
# Task 2: Laundry    Wash clothes       3
# Task 3: Museum     Egypt exhibit      4


# %%
# tuple unpacking -> task_i, task 
for task_i, task in enumerate(tasks, start=1):  # generate enumerate type iterator
    print(f"Task: {task_i}: {task.title:<10} {task.description:<18} {task.urgency}")

# # output: 
# Task: 1: Homework   Physics and math   5
# Task: 2: Laundry    Wash clothes       3
# Task: 3: Museum     Egypt exhibit      4


# %%
# bad case
for task_i in range(len(tasks)):
    task = tasks[-(task_i + 1)]     # - index 
    print(f"Task: {task}")

# # output: 
# Task: Task(title='Museum', description='Egypt exhibit', urgency=4)
# Task: Task(title='Laundry', description='Wash clothes', urgency=3)
# Task: Task(title='Homework', description='Physics and math', urgency=5)


# %%
# better case
for task in reversed(tasks):    # reversed()
    print(f"Task: {task}")

# # output: 
# Task: Task(title='Museum', description='Egypt exhibit', urgency=4)
# Task: Task(title='Laundry', description='Wash clothes', urgency=3)
# Task: Task(title='Homework', description='Physics and math', urgency=5)


# %%
dates = ["May 5", 'May 9, 2022', "May 11, 2022"]

locations = ["School", "Home", "Downtown"]



# %%
# bad case
for task_i in range(len(tasks)):
    task = tasks[task_i]
    date = dates[task_i]
    location = locations[task_i]
    print(f"{task.title}: by {date} at {location}")

# # output: 
# Homework: by May 5 at School
# Laundry: by May 9, 2022 at Home
# Museum: by May 11, 2022 at Downtown


# %%
# better case -> use zip()
for task, date, location in zip(tasks, dates, locations):
    print(f"{task.title}: by {date} at {location}")

# # output: 
# Homework: by May 5 at School
# Laundry: by May 9, 2022 at Home
# Museum: by May 11, 2022 at Downtown


# %%
# wrong case
for task, date, location in zip(enumerate(tasks, dates, locations)):    # 3 arguments
    print(f"{task.title}: by {date} at {location}")

# output: TypeError: enumerate() takes at most 2 arguments


# %%
for task, date, location in zip(tasks, dates, locations):
    zipped_tasks = task, date, location
    enumerate(zipped_tasks)
    print(zipped_tasks)

# # output: 
# (Task(title='Homework', description='Physics and math', urgency=5), 'May 5', 'School')
# (Task(title='Laundry', description='Wash clothes', urgency=3), 'May 9, 2022', 'Home')
# (Task(title='Museum', description='Egypt exhibit', urgency=4), 'May 11, 2022', 'Downtown')


# %%
from itertools import zip_longest

# the shorter iterables are exhausted, 
# the fillvalue is substituted in their place(None).
list(zip_longest(range(3), range(4), range(5)))

# # output: 
# [(0, 0, 0), (1, 1, 1), (2, 2, 2), (None, 3, 3), (None, None, 4)]


# %%
completed_tasks = [
    Task("Toaster", "Clean the toaster", 2),
    Task("Camera", "Export photos", 4),
    Task("Floor", "Mop the floor", 3)
]


# %%
# bad case
all_tasks = tasks + completed_tasks # generate temporary all_tasks -> memory overhead
for task in all_tasks:
    print(task.title)

# # output: 
# Homework
# Laundry
# Museum
# Toaster
# Camera
# Floor


# %%
# better case -> chaining of iterable
from itertools import chain

for task in chain(tasks, completed_tasks):
    print(task.title)

# # output: 
# Homework
# Laundry
# Museum
# Toaster
# Camera
# Floor


# %%
# bad case
for task in tasks:
    if task.urgency > 3:
        print(task)

# # output: 
# Task(title='Homework', description='Physics and math', urgency=5)
# Task(title='Museum', description='Egypt exhibit', urgency=4)


# %%
# better case -> filter()
for task in filter(lambda x: x.urgency > 3, tasks): # function: lambda, x: per task, tasks: iterable 
    print(task)

# # output: 
# Task(title='Homework', description='Physics and math', urgency=5)
# Task(title='Museum', description='Egypt exhibit', urgency=4)


# %%
n = 1
while n < 3:
    print(f"n's value: {n}")
    n += 1

print(f"n's value after while loop: {n}")
# output: 
# n's value: 1
# n's value: 2
# n's value after while loop: 3


# %%
from collections import namedtuple

# namedtuple class -> Task
Task = namedtuple("Task", "title, description, urgency")

tasks = [
    Task("Toaster", "Clean the toaster", 2),
    Task("Camera", "Export photos", 4),
    Task("Homework", "Physics and math", 5),
    Task("Floor", "Mop the floor", 3),
    Task("Internet", "Upgrade plan", 5),
    Task("Laundry", "Wash clothes", 3),
    Task("Museum", "Egypt exhibit", 4),
    Task("Utility", "Pay bills", 5)
]

first_urgent_task0 = None
for counter, task in enumerate(tasks, 1):
    print(f"---Checking task {counter}: {task.title}")

    # task's urgency = 5 and not allocate any value in first_urgent_task0
    if (task.urgency == 5) and (first_urgent_task0 is None):
        first_urgent_task0 = task

print(f"***first urgent task: {first_urgent_task0}")
# # output: 
# ---Checking task 1: Toaster
# ---Checking task 2: Camera
# ---Checking task 3: Homework
# ---Checking task 4: Floor
# ---Checking task 5: Internet
# ---Checking task 6: Laundry
# ---Checking task 7: Museum
# ---Checking task 8: Utility
# ***first urgent task: Task(title='Homework', description='Physics and math', urgency=5)


# %%
for number in range(5):
    print(f"Number: {number}")
    if number == 2:
        print("Breaking at 2")
        break

# output: 
# Number: 0
# Number: 1
# Breaking at 2


# %%
number = 0

while number < 100:
    if number == 2:
        print("Breaking at 2")
        break
    else:
        number += 1
        print(f"Number: {number}")

# output: 
# Number: 1
# Number: 2
# Breaking at 2


# %%
first_urgent_task1 = None   

for task in tasks:
    if task.urgency == 5:
        first_urgent_task1 = task
        break

assert first_urgent_task0 == first_urgent_task1


# %%
for number in range(5):
    if number < 3:
        continue    # True -> Next Iteration -> number = 0, 1, 2(True)
    print(f"Number: {number}")  # number = 3, continue (x) -> print 

# output: 
# Number: 3
# Number: 4


# %%
# bad case(non continue) -> tab 2
for task in tasks:
    if task.urgency > 4:
        result0 = task.do_something0()
        result1 = task.do_something1()

        if (result0 >= 0) and (result1 == "Hello"):
            task.do_something2()
            task.do_something3()
            task.do_something4()


# %%
# better case(continue) -> tab 1
for tsk in tasks:
    if task.urgency > 4:
        continue    # task.urgency = 4

    result0 = task.do_something0()
    result1 = task.do_something1()

    if (result0 < 0) or (result1 != "Hello"):   # result0 = 0, result1 = "Hello"
        continue

    task.do_something2()
    task.do_something3()
    task.do_something4()


# %%

# break -> stop the iteration -> skip the else statement
# for item in iterable:
#     # ...
# else:
#     # ...

def show_for_else_rule(breaking_number):
    for number in range(2):
        print(f"Iteration: {number}")

        if number == breaking_number:
            print(f"Break: {number}; Skip the else statement")
            break
    
    else:
        print("Running the else statement")
    print("Outside the for...else...")


show_for_else_rule(1)
# # output: 
# Iteration: 0
# Iteration: 1
# Break: 1; Skip the else statement
# Outside the for...else...


show_for_else_rule(3)
# # output: 
# Iteration: 0
# Iteration: 1
# Running the else statement
# Outside the for...else...


# %%
def locate_task(urgency_level):
    for task in tasks:
        if task.urgency == urgency_level:
            working_task = task
            break
    
    else:
        working_task = None
    print(f"Working Task: {working_task}")


locate_task(1)
# output: Working Task: None

locate_task(4)
# output: Working Task: Task(title='Camera', description='Export photos', urgency=4)


# %%
