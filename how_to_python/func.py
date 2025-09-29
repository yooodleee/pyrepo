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
