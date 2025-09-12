###############################################
## f-strings for interpolation and formatting
###############################################


#%%
# Existing variables
name = "Homework"
urgency = 5

# desired ouput:
# Name: Homework; Urgency Level: 5

# Note: the abote line isn't supposed to run as Python code, as it's text output.

#%%
task = "Name: " + name + "; Urgency Level:" + str(urgency)
print(task)
# output: Name: Homework; Urgency Level: 5


#%%
task1 = "Home: %s; Urgency Level: %d" % (name, urgency)
task2 = "Name: {}; Urgency Level: {}".format(name, urgency)


#%%
task_f = f"Name: {name}; Urgency Level: {urgency}"
assert task == task_f == "Name: Homework; Urgency Level: 5"


#%%
tasks = ["homework", "laundry"]
assert f"Tasks: {tasks}" == "Tasks: ['homework', 'laundry']" # List object interpolation

task_hwk = ("Homework", "Complete physics work")
assert f"Task: {task_hwk}" == "Task: ('Homework', 'Complete physics work')" # Tuple object interpolation

task = {"name": "Laundry", "unrgency": 3}
assert f"Task: {task}" == "Task: {'name': 'Laundry', 'urgency': 3}" # Dictionary object interpolation


#%%
tasks = ["homework", "laundary", "grocery shopping"]
assert f"First Task: {tasks[0]}" == 'First Task: homework' # A

task_name = "grocery shopping"
assert f"Task Name: {task_name.title()}" == 'Task Name: Grocery Shopping' # B

number = 5
assert f"Square: {number * number}" == 'Square: 25' # C