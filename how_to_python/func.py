################################
## User Friendly Function
################################


# %%
numbers = [4, 5, 7, 2]
numbers.sort()

assert numbers == [2, 4, 5, 7]


# %%
# setting keyword only key, reverse arguments -> *
numbers.sort(reverse=True)  # reverse(*, key=None, reverse=False) -> default arguments

assert numbers == [7, 5, 4, 2]


# %%
# wrong case 
numbers.sort(True)  # setting keyword only arguments


# %%
class Task:
    def __init__(self, title, description, urgency):
        self.title = title
        self.description = description
        self.urgency = urgency


def complete_task(task):
    task.title = "completed"
    print(f"{task.title}'s status: completed")


task = Task("Homework", "Physics and math", 5)
complete_task(task)
# output: Homework's status: completed


# %%
# bad case
def complete_task(task, note):
    task.status = "completed"
    task.note = note
    print(f"{task.title}'s status: completed; note: {note}")

# empty string -> DRY
complete_task(task, "")


# %%
# better case -> set default arguments(note)
def complete_task(task, note=""):
    task.status = "completed"
    task.note = note
    print(f"{task.title}'s status: completed; note: {note}")


# %%
# eval func when definition function. -> generate mutable default instance.
# generate list instance with eval function. -> side effect.
def complete_task(task, grouped_tasks=[]):
    task.status = "completed"
    grouped_tasks.append(task.title)
    
    return grouped_tasks


# %%
task0 = Task("Homework", "Physics and math", 5)
task1 = Task("Fishing", "Fishing at the late", 3)

work_tasks = complete_task(task0)
play_tasks = complete_task(task1)

print("Work Tasks:", work_tasks)
print("Play Tasks:", play_tasks)
# # output: 
# Work Tasks: ['Homework', 'Fishing']
# Play Tasks: ['Homework', 'Fishing']


# %%
assert work_tasks == play_tasks

assert work_tasks is play_tasks


# %%
def append_task(task, tasks=[]):
    tasks.append(task)
    print(f"Tasks: {tasks}; id: {id(tasks)}") # id(): return identity of object.


append_task.__defaults__    # search default object.
# output: ([],)

id(append_task.__defaults__[0])
# output: 2382810160960

append_task("Homework")
# output: Tasks: ['Homework']; id: 238210160960

append_task("Laundry")
# output: Tasks: ['Homework', 'Laundry']; id: 2382809796800

append_task.__defaults__
# output: (['Homework', 'Laundry'])


# %%
def complete_task(task, grouped_tasks=None):    # set mutable argument to None.
    task.status = "completed"
    if grouped_tasks is None:
        grouped_tasks = []
    
    grouped_tasks.append(task.title)
    return grouped_tasks

complete_task.__defaults__
# output: (None,)


# %%
numbers = list(range(5))

sum_numbers = sum(numbers)

print(f"Sum of {numbers} is {sum_numbers}")
# output: Sum of [0, 1, 2, 3, 4] is 10


# %%
primes = [5, 7, 2, 3, 11]

sort_return_value = primes.sort()

print(f"Return value of sort: {sort_return_value}")
# output: Return value of sort: None


# %%
primes.sort().append(13)
# output: AttributeError: 'NoneType' object has no attribute 'append'


# %%
# Case 1: no return value
def append_task(task, grouped_tasks):
    grouped_tasks.append(task)
    
    # no return 

appended_no_return = append_task("Homework", [])

print(f"Appended: {appended_no_return}")
# output: Appended: None


# %%
def append_task(task, grouped_tasks=[]):    # mutable argument to empty list
    grouped_tasks.append(task)

    # no return 

appended_no_return = append_task("Homework")

print(f"Appended: {appended_no_return}")
# output: Appended: None


# %%
# Case 2
def append_task(task, grouped_tasks):
    grouped_tasks.append(task)
    
    return

appended_no_return = append_task("Homework", [])

print(f"Appended: {appended_no_return}")
# output: Appended: None


# %%
# one return value(general case)
def say_hello(person):
    hello = f"Hello, {person}"
    return hello

greeting = say_hello("Rocky")   # allocate return value in greeting(variable)


# %%
# multiple return value 
from statistics import mean, stdev

def generate_stats(measures):
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std

# %%
# bad case(not pythonic)
def calculate_mean(measures):
    measure_mean = mean(measures)
    return measure_mean

def calculate_std(measures):
    measure_std = stdev(measures)
    return measure_std


# %%
# bad case: specify purpose of function 
def process_ddata(measures):
    formatted_measures = [f"{x} mg/L" for x in measures]
    measure_mean = mean(measures)
    return formatted_measures, measure_mean     # no association between formatted_measures and measure_mean.


# %%
# better case: separated function 
def format_measures(measures):
    formatted_measures = [f"{x} mg/L" for x in measures]
    return formatted_measures

def calculate_mean(measures):
    measure_mean = mean(measures)
    return measure_mean


# %%
measures = [5.6, 7.0, 5.7, 5.8, 4.3, 5.2]

measures_stats = generate_stats(measures)

print(type(measures_stats), measures_stats)
# output: <class 'tuple'> (5.6, 0.8786353054595518)


# %%
# unpacking formatted tuple object 
m_mean, m_std = generate_stats(measures)

print(f"Mean: {m_mean}; SD: {m_std}")
# output: Mean: 5.6; SD: 0.8786353054595518


# %%
# wrong case:
m_mean = generate_stats(measures)

print(f"Mean: {m_mean}")
# output: Mean: (5.6, 0.8786353054595518)


# %%
# correct case
m_mean, _ = generate_stats(measures)    # no m_std

print(f"Mean: {m_mean}")
# output: Mean: 5.6


# %%
# correct case
_, m_std = generate_stats(measures)     # no m_mean

print(f"SD: {m_std}")
# output: SD: 0.8786353054595518


# %%
number = 1

print(type(number))
# output: <class 'int'>


# %%
number = "one"      # dynamically typed language(Python)

print(type(number))
# output: <class 'str'>


# %%
number: int = 3             # type hint(int)

name: str = "John"          # type hint(str)

primes: list = [1, 2, 3]    # type hint(list)


# %%
numbers: tuple = (1, 2, 3)  # dynamically typed language

numbers = [1, 2, 3]


# %%
from statistics import mean, stdev

def generate_stats(measures: list) -> tuple:
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std


help(generate_stats)
# output: 
# Help on function generate_stats in module __main__:

# generate_stats(measures: list) -> tuple


# %%
def calculate_sum(a: int, b: int) -> int:
    c = a + b
    return c 


calculate_sum()
# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'

calculate_sum("1", 2)
# output: TypeError: can only concatenate str (not "int") to str


# %%
# Case 1: default value 
def calculate_product(a: int, b: int, multiplier: int = 1) -> int:
    c = a * b * multiplier
    return c 


# %%
# Case 2: namedtuple(user defined class)
from collections import namedtuple

Task = namedtuple("Task", "title description urgency")

class User: 
    pass

def assign_task(pending_task: Task, user: User):  # Task, User(type)
    pass


# %%
# bad case
def complete_tasks(tasks: list):
    for task in tasks:
        pass

complete_tasks(["Laundry", "Museum"])

complete_tasks([Task("Laundry", "Wash clothes", 5), Task("Egyptian exhibit", 4)])


# %%
# better case
def complete_tasks(tasks: list[Task]):  # detail info about tasks
    for task in tasks:
        pass

complete_tasks(["Laundry", "Museum"])


# %%
from statistics import mean, stdev

def generate_stats(measures: list[float] | tuple[float, ...]) -> tuple[float, float]:
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std


# %%
from statistics import mean, stdev
from typing import Sequence

def generate_stats(measures: Sequence[float]) -> tuple[float, float]:
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std


# %%
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

word = "Hello"          # object(str)
numbers = [1, 2, 3]     # object(list)
prime_number = 11       # object(int)

print(word, numbers, prime_number)  # *objects-> mutable.
# output: Hello [1, 2, 3] 11


# %%
def multiply_numbers(a, b):
    return a * b


# %%
# Case 1: positional argument
multiply_numbers(1, 2)  # a = 1, b = 2
# output: 2

multiply_numbers(2, 1)  # a = 2, a = 1
# output: 2


# %%
# Case 2: keyword argument
multiply_numbers(a=3, b=4)  # a = 3, b = 4
# output: 12 

multiply_numbers(b=4, a=3)  # a = 3, b = 4
# output: 12


# %%
# Case 3: positional argument + keyword argument
multiply_numbers(5, b=6)    # positional argument(5), keyword argument(b=6)
# output: 

multiply_numbers(b=6, 5)    # SyntaxError
# output: SyntaxError: positional argument follows keyword argument


# %%
def stringify(*items):  # *items(positionarl argument)
    print(f"got {items} in {type(items)}")
    return [str(item) for item in items]


stringify(1, "two", None)
# output:
# got (1, 'two', None) in <class 'tuple'>
# ['1', 'two', 'None']


# %%
# good case
def stringify_a(item0, *items):
    print(item0, items)


stringify_a(0)      # appropriate parsing -> first argument(item0), remain argument(items)
# output: 0 ()

stringify_a(0, 1)   # first argument(0, item0) second argument(1, items)
# output: 0 (1,)


# %%
# wrong case
def stringify_b(*items, item0): # correct definition(item0, *items) 
    print(item0, items)

stringify_b(0, 1)   # can't appropriate parse items and item0
# output: TypeError: stringify_b() missing 1 required keyword-only argument: 'item0'


# %%
def create_report(name, **grades):      # keyword argument(**grades)
    print(f"got {grades} in {type(grades)}")    # packing single dictionary object

    report_items = [f"***** Report Begin for {name} *****"]
    for subject, grade in grades.items():
        report_items.append(f"### {subject}: {grade}")
    
    report_items.append(f"***** Report End for {name} ******")
    print("\n".join(report_items))


create_report("John", math=100, phys=98, bio=95)    # name: "John", grades: math, phys, bio
# # output: 
# got {'math': 100, 'phys': 98, 'bio': 95} in <class 'dict'>
# ***** Report Begin for John *****
# ### math: 100
# ### phys: 98
# ### bio: 95
# ***** Report End for John ******


# %%
def example(arg0, arg1, *args, kwarg0, kwarg1, **kwargs):
    """arg0, arg1, *args: positional argument
    kwarg0, kwarg1, **kwargs: keyword argument"""
    
    pass


# %%
