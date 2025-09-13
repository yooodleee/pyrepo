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
assert f"Square: {number * number}" == 'Square: 25' # 


#%%
summary_text = f"Your Average Score: {sum([95, 98, 97, 96, 97, 93]) / len(95, 98, 97, 96, 97, 93)}."


#%%
scores = [95, 98, 97, 96, 97, 93]

total_score = sum(scores)
subject_count = len(scores)
average_score = total_score / subject_count

summary_text = f"Your Average Score: {average_score}."


#%%
task_ids = [1, 2, 3]
task_names = ['Do homework', 'Laundary', 'Pay bills']
task_urgencies = [5, 3, 4]

for i in range(3):
    print(f'{task_ids[i]:^12}{task_names[i]:^12}{task_urgencies[i]:^12}') # use format specifier

# # output
#      1      Do homework      5      
#      2        Laundary       3      
#      3       Pay bills       4     


#%%
def create_formatted_records(fmt):
    for i in range(3):
        task_id = task_ids[i]
        name = task_names[i]
        urgency = task_urgencies[i]
        print(f'{task_id:{fmt}}{name:{fmt}}{urgency:{fmt}}')


# %%
create_formatted_records('^15')

# # output
#        1         Do homework         5       
#        2          Laundary           3       
#        3          Pay bills          4    

# %%
create_formatted_records('^18')

# # output
#        1         Do homework         5       
#        2          Laundary           3       
#        3          Pay bills          4    


#%%
large_prime_number = 1000000007

print(f"Use commas: {large_prime_number:,d}")
# output: Use commas: 1,000,000,007


#%%
decimal_number = 1.23456

print(f"Two digits: {decimal_number:.2f}")
# output: Two digits: 1.23

print(f"Four dogots: {decimal_number:.4f}")
# output: Four dogots: 1.2346


#%%
sci_number = 0.00000000412733

print(f"Sci number: {sci_number:e}")
# output: Sci number: 4.127330e-09

print(f"Sci number: {sci_number:.2e}")
# output: Sci number: 4.13e-09


# %%
pct_number = 0.179323

print(f"Percentage: {pct_number:%}")
# output: Percentage: 17.932300%

print(f"Percentage two digits: {pct_number:.2%}")
# output: Percentage two digits: 17.93%


# %%
bad_username0 = "123!@#"
assert bad_username0.isalnum() == False

bad_username1 = "abc..."
assert bad_username1.isalnum() == False

good_username = "1a2b3c"
assert good_username.isalnum() == True 


# %%
assert "Homework".isalpha() == True

assert "Homework123".isalpha() == False


# %%
assert "123".isnumeric() == True

assert "a123".isnumeric() == False 


# %%
