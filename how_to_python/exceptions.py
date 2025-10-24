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
