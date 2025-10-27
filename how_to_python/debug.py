##########################
## Debugging
##########################


# %%
# case: pdb module
def create_task():
    import pdb; pdb.set_trace()     # add a breakpoint

create_task()
# # output: 
# --Return--
# None
# > <ipython-input-1-b86f578029b2>(4)create_task()
#       2 # case: pdb module
#       3 def create_task():
# ----> 4     import pdb; pdb.set_trace()     # add a breakpoint
#       5 
#       6 create_task()


# %%
# case: breakpoint() method
def create_task():
    breakpoint()

create_task()
# output: 


# %%
from collections import namedtuple
Task = namedtuple("Task", "title urgency")  # generate a namedtuple class

def obtain_text_data(want_bad):
    text = "Laundry,3#" if want_bad else "Laundry,3"
    return text

def create_task(inject_bug: bool):
    breakpoint()    # add a breakpoint
    task_text = obtain_text_data(inject_bug)    # line: 10
    title, urgency_text = task_text.split(",")
    urgency = int(urgency_text)
    task = Task(title, urgency)
    return task

if __name__ == "__main__":
    create_task(inject_bug=False)

# output: 
# execute a script.
# > /full_path/task_debug.py(10)create_task()
# -> task_text = obtain_text_data(inject_bug)
# (Pdb)

# press a n(next) key
# > /full_path/task_debug.py(11)create_task()
# -> title, urgency_text = task_text.split(",")
# (Pdb)

# press a Enter(Windows) or Return(macOS) key
# > /full_path/task_debug.py(12)create_task()
# -> urgency = int(urgency_text)
# (Pdb)


# %%
# option: l(list) key
# (Pdb) l
# 7
# 8  def create_task(inject_bug: bool):
# 9      breakpoint()
# 10     task_text = obtain_text_data(inject_bug)
# 11     title, urgency_text = task_text.split(",")
# 12 ->  urgency = int(urgency_text)
# 13     task = Task(title, urgency)
# 14     return task
# 15
# 16    if __name__ == "__main__":
# 17       create_task(inject_bug=False)
# (Pdb)


# %%
# option: s(step) key
# (Pdb) s
# --Call--
# > /full_path/task_debug.py(4)obtain_text_data()
# -> def obtain_text_data(want_bad):

# (Pdb) s
# --Call--
# > /full_path/task_debug.py(5)obtain_text_data()
# -> text = "Laundry,3#" if want_bad else "Laundry,3"
# (Pdb) s
# > /full_path/task_debug.py(6)obtain_text_data()
# -> return text
# (Pdb) s
# --Return--
# > /full_path/task_debug.py(6)obtain_text_data()->'Laundry,3'
# -> return text

# (Pdb) s
# > /full_path/task_debug.py(11)create_task()
# -> title, urgency_text = task_text.split(",")


# %%
