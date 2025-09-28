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
