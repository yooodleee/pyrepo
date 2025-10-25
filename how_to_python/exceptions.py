###################################
## Exceptions
###################################


# %%
from collections import namedtuple

Task = namedtuple("Task", ["title", "urgency"])     # namedtuple
task_text0 = "Laundry,3"

def process_task_string0(text):
    title, urgency_str = text.split(",")            # unpacking generated list instance
    urgency = int(urgency_str)
    task = Task(title, urgency)
    return task

processed_task0 = process_task_string0(task_text0)

assert processed_task0 == Task(title='Laundry', urgency=3)


# %%
task_text1 = "Laundry,3#"

processed_task1 = process_task_string0(task_text1)
# output: ValueError: invalid literal for int() with base 10: '3#'


# %%
# try... except...
def process_task_string1(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)          # task_text1 = "Laundry,3#"
    except:
        print("Couldn't cast the number")
        return None
    task = Task(title, urgency)
    return task

processed_task1 = process_task_string1(task_text1)
# output: Couldn't cast the number

assert processed_task1 is None


# %%
processed_task0 = process_task_string1(task_text0)

assert processed_task0 == Task(title='Laundry', urgency=3)


# %%
def process_task_string2(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        pending_task.urgency = urgency
    except:
        print("Coudln't cast the number")
        return None
    task = Task(title, urgency)
    return task

pending_task.urgency = 3
# output: NameError: name 'pending_task' is not defined


# %%
process_task_string2("Laundry,3")
# output: Couldn't cast the number


# %%
def process_task_string3(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        pending_task.urgency = urgency
    except ValueError:
        print("Couldn't cast the number")
        return None
    task = Task(title, urgency)
    return task

process_task_string3("Laundry,3#")
# output: Coudln't cast the number


# %%
process_task_string3("Laundry,3")
# output: NameError: name 'pending_task' is not defined


# %%
def process_task_string4(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        pending_task.urgency = urgency
    except ValueError:
        print("Couldn't cast the number")
        return None
    except NameError:
        print("You're referencing an undefined name")
        return None
    task = Task(title, urgency)
    return task

process_task_string4("Laundry,3")
# output: You're referencing an undefined name

process_task_string4("laundry,3#")
# output: Couldn't cast the number


# %%
def process_task_string5(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        pending_task.urgency = urgency
    except (ValueError, NameError):
        print("Couldn't process the task string")
        return None
    task = Task(title, urgency)
    return task

process_task_string5("Laundry,3")   # NameError
# output: Couldn't process the task string

process_task_string5("Laundry,3#")  # ValueError
# output: Couldn't process the task string


# %%
def process_task_string6(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
    except ValueError as ex:
        print(f"Couldn't cast the number. Description: {ex}")
        return None
    task = Task(title, urgency)
    return task

process_task_string6("Laundry,3#")
# # output: 
# Couldn't cast the number. Description: invalid literal for int() with base 10: '3#'


# %%
def process_task_string7(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
    except ValueError as e:
        print(f"Couldn't cast the number. Description: {e}")
        return None
    else:
        task = Task(title, urgency)
        return task

processed_task7 = process_task_string7("Laundry,3")

assert processed_task7 == Task("Laundry", 3)


# %%
processed_task = process_task_string7("Laundry,3#")
# # output: 
# Couldn't cast the number. Description: invalid literal for int() with base 10: '3#'

print(processed_task)
# output: None


# %%
def process_task_string9(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        task = Task(title, urgency)
        return task
    except ValueError as e:
        print(f"Couldn't cast the number. Description: {e}")
        return None
    finally:
        print(f"Done processing text: {text}")

task = process_task_string9("Laundry,3")
# output: Done processing text: Laundry,3

assert task == Task("Laundry", 3)


# %%
# syntactic sugar
raise ValueError
# # output: 
# Traceback (most recent call last)
#     File "<stdin>", line 1, in <module>
# ValueError

raise ZeroDivisionError
# # output: 
# Traceback (most recent call last)
#     File "<stdin>", line 1, in <module>
# ZeroDivisionError


# %%
try:
    1 / 0
except ZeroDivisionError as e:  # ZeroDivisionError class's instance 
    print(f"Type: {type(e)}")
print(f"Is an instance of ZeroDivisionError? {isinstance(e, ZeroDivisionError)}")
# # output: 
# Type: <class 'ZeroDivisionError'>
# Is an instance of ZeroDivisionError? True


# %%
# user defined message
raise ValueError("Please use the correct parameter.")
# output: ValueError: Please use the correct parameter.

code_used = "3#"

raise ValueError(f"You used a wrong parameter: {code_used!r}")  # !r
# output: ValueError: You used a wrong parameter: '3#'


# %%
# inner exception class first
class Task:
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("Please instantiate the Task using string as its title")

task = Task(100)
# output: TypeError: Please instantiate the Task using string as its title


# %%
# user defined exception class
class TaskierError(Exception):
    pass

class FileExtensionError(TaskierError):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
    
    def __str__(self):
        return f"The file ({self.file_path}) doesn't apper to be a CSV file."

# package's other code
from pathlib import Path

def upload_file(file_path):
    path = Path(file_path)
    if path.suffix.lower() != ".csv":
        raise FileExtenError(file_path)
    else:
        print(f"Processing the file at {file_path}")


# %%
def custom_upload_file(file_path):
    try:
        upload_file(file_path)
    except FileExtensionError as e:
        print(e)
    else:
        print("Custom upload file is done.")

custom_upload_file("tasks.csv")
# # output: 
# Processing the file at tasks.csv
# Custom upload file is done.

custom_upload_file("tasks.docx")
# # output: 
# The file at tasks.docx doesn't appear to be a CSV file.


# %%
