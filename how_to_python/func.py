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
