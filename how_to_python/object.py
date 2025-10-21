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
text_file = open("tasks.txt")

print(text_file)
# output: <_io.TextIOWrapper name='tasks.txt' mode='r' encoding='cp949'>


# %%
text_data = text_file.read()

print(type(text_data))
# output: <class 'str'>

print(text_data)
# # output: 
# 1001,Homework,5
# 1002,Laundry,3
# 1003,Grocery,4


# %%
text_file.close()       # should

assert text_file.closed


# %%
# more pythonic: context management(with)
with open("tasks.txt") as file:     # close x
    print(f"file object: {file}")
    data = file.read()
    print(data)

# # output: 
# file object: <_io.TextIOWrapper name='tasks.txt' mode='r' encoding='cp949'>
# 1001,Homework,5
# 1002,Laundry,3
# 1003,Grocery,4

assert file.closed


# %%
# case: generator
from collections import namedtuple

Task = namedtuple("Task", "task_id title urgency")

with open("tasks.txt") as file:
    for line in file:
        stripped_line = line.strip()
        task_id, title, urgency = stripped_line.split(",")
        task = Task(task_id, title, urgency)
        print(f"{stripped_line}: {task}")

# # output: 
# 1001,Homework,5: Task(task_id='1001', title='Homework', urgency='5')
# 1002,Laundry,3: Task(task_id='1002', title='Laundry', urgency='3')
# 1003,Grocery,4: Task(task_id='1003', title='Grocery', urgency='4')


# %%
# case: generate list unit
desired_output = [
    '#1: 1001,Homework,5',
    '#2: 1002,Laundry,3',
    '#3: 1003,Grocery,4'
]

with open("tasks.txt") as file:
    lines = file.readlines()
    updated_lines = [f"#{row}: {line.strip()}" 
                     for row, line in enumerate(lines, start=1)]   # enumerate(): generate counter

assert desired_output == updated_lines


# %%
# case: readline()
with open("tasks.txt") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5)) # maximum readable size
    print(file.readline(8))
    print(file.readline())

# output: 
# 1001,Homework,5

# 1002,Laundry,3

# 1003,
# Grocery,
# 4
# %%
# correct case: allocate write mode
data = """1001,Homework,5
1002,Laundry,3
1003,Grocery,4"""

with open("tasks_new.txt", "w") as file:
    print('File: ', file)
    result = file.write(data)
    print("Writing result: ", result)

# # output: 
# File:  <_io.TextIOWrapper name='tasks_new.txt' mode='w' encoding='cp949'>
# Writing result:  45


# %%
# wrong case: allocate default mode(read)
with open("tasks_new.txt") as file:     # default mode: r(read)
    print("File: ", file)
    result = file.write(data)
    print("Writing result: ", result)

# output: io.UnsupportedOperation: not writable


# %%
new_task = "1004,Museum,3"

with open("tasks.txt", "a") as file:    # append mode
    file.write(f"\n{new_task}")


# %%
import csv

with open("tasks.txt", newline="") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# # output: 
# ['1001', 'Homework', '5']
# ['1002', 'Laundry', '3']
# ['1003', 'Grocery', '4']
# ['1004', 'Museum', '3']


# %%
with open("tasks.txt", newline="") as file:
    csv_reader = csv.reader(file)
    tasks_row = list(csv_reader)
    print(tasks_row)

# # output:
# [['1001', 'Homework', '5'], ['1002', 'Laundry', '3'], ['1003', 'Grocery', '4'], ['1004', 'Museum', '3']]


# %%
with open("tasks.txt", newline="") as file:
    csv_reader = csv.reader(file)
    fields = next(csv_reader)       # get next item
    print("Field: ", fields)
    for row in csv_reader:
        task_dict = dict(zip(fields, row))  # generate dict instace
        print(task_dict)

# # output: 
# Field:  ['task_id', 'title', 'urgency']
# {'task_id': '1001', 'title': 'Homework', 'urgency': '5'}
# {'task_id': '1002', 'title': 'Laundry', 'urgency': '3'}
# {'task_id': '1003', 'title': 'Grocery', 'urgency': '4'}
# {'task_id': '1004', 'title': 'Museum', 'urgency': '3'}


# %%
with open("tasks.txt", newline="") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

# # output: 
# {'task_id': '1001', 'title': 'Homework', 'urgency': '5'}
# {'task_id': '1002', 'title': 'Laundry', 'urgency': '3'}
# {'task_id': '1003', 'title': 'Grocery', 'urgency': '4'}
# {'task_id': '1004', 'title': 'Museum', 'urgency': '3'}


# %%
new_task = "1005,Study,7"

with open("tasks.txt", "a", newline="") as file:
    file.write("\n")
    csv_writer = csv.writer(file)
    csv_writer.writerow(new_task.split(","))    # split: generate list


# %%
tasks = [
    {'task_id': '1001', 'title': 'Homework', 'urgency': '5'},
    {'task_id': '1002', 'title': 'Laundry', 'urgency': '3'},
    {'task_id': '1003', 'title': 'Grocery', 'urgency': '4'},
    {'task_id': '1004', 'title': 'Museum', 'urgency': '3'},
]

fields = ['task_id', 'title', 'urgency']

with open("tasks_dict.txt", "w", newline="") as file:
    csv_writer = csv.DictWriter(file, fieldnames=fields)
    csv_writer.writeheader()        # records header
    csv_writer.writerows(tasks)     # record multiple rows


# %%
import pickle

task_tuple = (1001, "Homework", 5)
task_dict = {'task_id': '1002', 'task_title': 'Laundry', 'urgency': 3}

with open("task_tuple_saved.pickle", "wb") as file:
    pickle.dump(task_tuple, file)       # dump(): task_tuple -> pickle file

with open("task_dict_saved.pickle", "wb") as file:
    pickle.dump(task_dict, file)        # dump(): task_dict -> pickle file


# %%
# unpickling
with open("task_tuple_saved.pickle", "rb") as file:
    task_tuple_loaded = pickle.load(file)

with open("task_dict_saved.pickle", "rb") as file:
    task_dict_loaded = pickle.load(file)


# %%
assert task_tuple == task_tuple_loaded

assert task_dict == task_dict_loaded


# %%
# case: pickled class(user defined class's instance)
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

task = Task("Laundry", 3)

with open("task_class_saved.pickle", "wb") as file:     # pickling
    pickle.dump(task, file)

with open("task_class_saved.pickle", "rb") as file:     # unpickling
    task_class_loaded = pickle.load(file)

assert task.__dict__ == task_class_loaded.__dict__

assert task is not task_class_loaded


# %%
del Task    # delete Task in global scope namespace

with open("task_class_saved.pickle", "rb") as file:
    task_class_loaded = pickle.load(file)

# output: AttributeError: can't get attribute 'Task' on <module '__main__' (built-in)>


# %%
# case: pickling function 
def doubler(x):
    return x * 2

doubler_pickle = pickle.dumps(doubler)
doubler_pickle
# output: b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x07doubler\x94\x93\x94.'


# %%
doubler_loaded = pickle.loads(doubler_pickle)

assert doubler_loaded(5) == doubler(5)


# %%
# pickling module
import os

os_dumped = pickle.dumps(os)
# output: TypeError: cannot pickle 'module' object


# %%
# data security
import os

class MaliciousTask:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency
    
    def __reduce__(self):
        print("__reduce__ is called")
        return os.system, ('touch hacking.txt',)


# %%
# pickling user defined class's instance
malicious_task = MaliciousTask("Set fire", 5)

with open("test_malicious.pickle", "wb") as file:
    pickle.dump(malicious_task, file)

# output: __reduce__ is called


# %%
with open("test_malicious.pickle", "rb") as file:
    pickle.load(file)


# %%
from pathlib import Path

data_folder = Path("data")
data_folder.mkdir()     # make directory


# %%
assert data_folder.exists()


# %%
subject_ids = [123, 124, 125]
extensions = ["config", "dat", "txt"]

for subject_id in subject_ids:
    for extension in extensions:
        filename = f"subject_{subject_id}.{extension}"
        filepath = data_folder / filename
        with open(filepath, "w") as file:
            file.write(f"It's the file {filename}.")


# %%
data_folder = Path("data")

data_files = data_folder.glob("*.dat")
print("Data files: ", data_files)   # generator instance

for data_file in data_files:
    print(f"Processing file: {data_file}")

# # output: 
# Data files:  <generator object Path.glob at 0x00000126D95FE890>
# Processing file: data\subject_123.dat
# Processing file: data\subject_124.dat
# Processing file: data\subject_125.dat


# %%
data_files = data_folder.glob("*.dat")

for data_file in sorted(data_files):    # sorted generator and return a new list
    print(f"Processing file: {data_file}")

# # output: 
# Processing file: data\subject_123.dat
# Processing file: data\subject_124.dat
# Processing file: data\subject_125.dat


# %%
subject_ids = [123, 124, 125]
data_folder = Path("data")

for subject_id in subject_ids:
    subject_folder = Path(f"subjects/subject_{subject_id}")
    subject_folder.mkdir(parents=True, exist_ok=True)
    for subject_file in data_folder.glob(f"*{subject_id}*"):
        filename = subject_file.name
        target_path = subject_folder / filename
        _ = subject_file.rename(target_path)
        print(f"Moving {filename} to {target_path}")

# # output: 
# Moving subject_123.config to subjects\subject_123\subject_123.config
# Moving subject_123.dat to subjects\subject_123\subject_123.dat
# Moving subject_123.txt to subjects\subject_123\subject_123.txt
# Moving subject_124.config to subjects\subject_124\subject_124.config
# Moving subject_124.dat to subjects\subject_124\subject_124.dat
# Moving subject_124.txt to subjects\subject_124\subject_124.txt
# Moving subject_125.config to subjects\subject_125\subject_125.config
# Moving subject_125.dat to subjects\subject_125\subject_125.dat
# Moving subject_125.txt to subjects\subject_125\subject_125.txt


# %%
import shutil

shutil.rmtree("subjects")   # remove directory, file, sub directory

subject_ids = [123, 124, 125]
data_folder = Path("data")

for subject_id in subject_ids:
    subject_folder = Path(f"subjects/subject_{subject_id}")
    subject_folder.mkdir(parents=True, exist_ok=True)

    for subject_file in data_folder.glob(f"*{subject_id}*"):
        filename = subject_file.name
        target_path = subject_folder / filename
        _ = shutil.copy(subject_file, target_path)

        print(f"Copying {filename} to {target_path}")

# # # output: 
# Copying subject_123.config to subjects/subject_123/subject_123.config
# Copying subject_123.dat to subjects/subject_123/subject_123.dat
# Copying subject_123.txt to subjects/subject_123/subject_123.txt
# Copying subject_124.config to subjects/subject_124/subject_124.config
# Copying subject_124.dat to subjects/subject_124.subject_124.dat
# Copying sujbect_124.txt to subjects/subject_124.subject_124.txt
# Copying subject_125.config to subjects/subject_125/subject_125.config
# Copying subject_125.dat to subjects/subject_125/subject_125.dat
# Copying subject_125.txt to subjects/subject_125/subject_125.tx


# %%
Path("subjects").rmdir()
# output: OSError: [Errno 66] Directory not empty: 'subjects'


# %%
data_folder = Path("data")

for file in data_folder.glob("*.txt"):
    before = file.exists()
    file.unlink()
    after = file.exists()
    print(f"Deleting {file}, existing? {before} -> {after}")

# # output: 
# Deleting data/subject_123.txt, existing? True -> False
# Deleting data/subject_124.txt, existing? True -> False
# Deleting data/subject_125.txt, existing? True -> False


# %%
from pathlib import Path

subjects_folder = Path("subjects")

for dat_path in subjects_folder.glob("**/*.dat"):
    subject_dir = dat_path.parent       # get file's directory name
    filename = dat_path.stem            # filename excepted extension
    config_path = subject_dir / f"{filename}.config"
    print(f"{subject_dir} & {filename} -> {config_path}")

    dat_exists = dat_path.exists()
    config_exists = config_path.exists()

    with open(dat_path) as dat_file, open(config_path) as config_file:
        print(f"Process {filename}: dat? {dat_exists}, config? {config_exists}\n")

# # output: 
# subjects/subject_125 & subject_125 -> subjects/subject_125/subject_125.config
# Process subject_125: dat? True, config? True

# subjects/subject_124 & subject_124 -> subjects/subject_124/subject_124.config
# Process subject_124: dat? True, config? True

# subjects/subject_123 & subject_123 -> subjects/subject_123/subject_123.config
# Process subject_123: dat? True, config? Tru


# %%
dat_path = Path("subjects/subject/subject_123.dat")

assert dat_path.suffix == ".dat"


# %%
def process_data_using_sizze_cutoff(min_size, max_size):
    data_folder = Path("data")
    for dat_path in data_folder.glob("*.dat"):
        filename = dat_path.name
        size = dat_path.stat().st_size  # file size
        if min_size < size < max_size:
            print(f"{filename}, Good; {size}, within [{min_size}, {max_size}]")
        else:
            print(f"{filename}, Bad; {size}, outside [{min_size}, {max_size}]")


process_data_using_sizze_cutoff(20, 40)
# # output: 
# subject_124.dat, Good; 30, within [20, 40]
# subject_125.dat, Good; 30, within [20, 40]
# subject_123.dat, Good; 30, within [20, 40

process_data_using_sizze_cutoff(40, 60)
# # output: 
# subject_124.dat, Bad; 30, outside [40, 60]
# subject_125.dat, Bad; 30, outside [40, 60]
# subject_123.dat, Bad; 30, outisde [40, 60]


# %%
import time 

subject_dat_path = Path("data/subject_123.dat")
modified_time = subject_dat_path.stat().st_mtime
readable_time = time.ctime(modified_time)

print(f"Modification time: {modified_time} -> {readable_time}")
# output: Modification time: 1652123144.9999998 -> Mon May 9 14:05:44 2022


# %%
