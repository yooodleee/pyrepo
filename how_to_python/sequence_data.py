#############################
## Sequence Data
#############################


# %%
text = "Hello, World!"

fruits = ["apple", "orange", "banana", "strawberry"]

vowels = ("a", "b", "i", "o", "u")

assert fruits[1:3] == ["orange", "banana"]


# %%
assert fruits[:3] == ["apple", "orange", "banana"]

assert fruits[1:] == ["orange", "banana", "strawberry"]

assert fruits[:] == ["apple", "orange", "banana", "strawberry"]


# %%
fruits[5]
# output: IndexError: list index out of range 


# %%
# bad case
numbers = [0, 1, 2, 3, 4, 5]

numbers[:20]
# output: [0, 1, 2, 3, 4, 5]

numbers[-1000:2]
# output: [0, 1]


# %%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

assert numbers[2:5:2] == [3, 5]

assert numbers[::3] == [1, 4, 7]

assert numbers[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1]


# %%
slice_obj = slice(1, 10, 2)
range_obj = range(1, 10, 2)

slice_obj.start, slice_obj.stop, slice_obj.step
# output: (1, 10, 2)

range_obj.start, range_obj.stop, range_obj.step
# output: (1, 10, 2)


# %%
list(range(10))
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(slice(10))
# output: TypeError: 'slice' object is not iterable


# %%
numbers = list(range(10))

odd_slice = slice(1, 10, 2)
numbers[odd_slice]
# output: [1, 3, 5, 7, 9]

odd_range = range(1, 10, 2)
numbers[odd_range]
# output: TypeError: list indices must be integers or slices, not range


# %%
tasks = """
0....5..............20..........................48......
1001 Laundry        Wash all clothes            3
1002 Museum Visit   Go to the Egypt exhibit     4
1003 Do Homework    Physics and math            5
1004 Go to Gym      Work out for 1 hour         2
"""

task_id = slice(5)
task_title = slice(5, 20)
task_desc = slice(20, 48)
task_urgency = slice(48, 49)

task_lines = tasks.split("\n")[2:-1]

tasks = []
for line in task_lines:
    task = (line[task_id].strip(),
            line[task_title].strip(),
            line[task_desc].strip(),
            line[task_urgency].strip())
    tasks.append(task)


print(tasks)
# output: 
# [('1001', 'Laundry', 'Wash all clothes', '3'), 
#  ('1002', 'Museum Visit', 'Go to the Egypt exhibit', '4'), 
#  ('1003', 'Do Homework', 'Physics and math', '5'), 
#  ('1004', 'Go to Gym', 'Work out for 1 hour', '2')]


# %%
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers[:3] = [10, 11, 12]
numbers
# output: [10, 11, 12, 3, 4, 5, 6, 7, 8]


# %%
numbers[3:] = [13, 14, 15, 16, 17, 18, 19, 20]
numbers
# output: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# %%
numbers[:5] = [0, 1]
numbers 
# output: [0, 1, 15, 16, 17, 18, 19, 20]


# %%
numbers[::2] = [0, 0, 0, 0]
numbers
# output: [0, 1, 0, 16, 0, 18, 0, 20]


# %%
del numbers[:4]
numbers
# output: [0, 18, 0, 20]


# %%
numbers[-2:] = []
numbers 
# output: [0, 18]


# %%
assert (8 in [1, 2, 3, 4, 5]) == False 

assert ('cool' in 'Python is cool') == True 

assert (404 in (404, 'Page Not Found')) 


# %%
[1, 2, 3, 4, 5].index(4)
# output: 3

(404, 'Page Not Found').index('Page Not Found')
# output: 1

'Python is cool'.index('cool')
# output: 10


# %%
[1, 2, 3, 4, 5].index(8)
# output: ValueError 8 is not in list


# %%
the_list = [1, 2, 3, 4, 5]


def process_item_try(item):
    try:
        item_index = the_list.index(item)
    except ValueError:
        print(f"{item} is not in the_list")
    
    print(f"{item} in {item_index}")


# %%
def process_item_check_first(item):
    if item in the_list:
        item_index = the_list.index(item)
        print(f"{item} in {item_index}")
    
    else:
        print(f"{item} is not in the_list")


# %%
