from collections import namedtuple

Task = namedtuple("Task", "title urgency")      # generate a named tuple class

def obtain_text_data(want_bad):
    text = "Laundry,3#" if want_bad else "Laundry,3"
    return text

def create_task(inject_bug: bool):
    breakpoint()        # add a breakpoint
    task_text = obtain_text_data(inject_bug)    # line: 10
    title, urgency_text = task_text.split(",")
    urgency = int(urgency_text)
    task = Task(title, urgency)
    return task

if __name__ == "__main__":
    create_task(inject_bug=False)

# # output: 
# $ python3 task_debug.py
# > /full_path/task_debug.py(10)create_task()
# -> task_text = obtain_text_data(inject_bug)
# (Pdb)

# > /full_path/task_debug.py(11)create_task()
# -> title, urgency_text = task_text.split(",")
# (Pdb)

# > /full_path/task_debug.py(12)create_task()
# -> urgency = int(urgency_text)
# (Pdb)