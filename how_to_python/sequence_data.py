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
# some pseudo code
# def find_string(substr):
#     str_index = the_str.find(substr)    # find -> return -1
#     if str_index >= 0:
#         # do something with the str_index
#     else:
#         # do something when the substr isn't preseont


# %%
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

tasks = [
    Task("Laundry", 3),
    Task("Museum", 4),
    Task("Homework", 5),
    Task("Ticket", 2)
]

needed_urgency = 5
needed_task_index = None

for task_i in range(len(tasks)):
    task = tasks[task_i]
    if task.urgency == needed_urgency:
        needed_task_index = task_i
        break

print(f"Task Index: {needed_task_index}")
# output: Task Index: 2


# %%
tasks.index(Task("Homework", 5))
# output: ValueError: <__main__.Task object at 0x000002817975E790> is not in list


# %%
id(Task("Homework", 5))
# output: 2755092089776

id(tasks)
# output: 2755113601472

id(needed_task_index)
# output: 2755010783568

id(tasks.index(Task("Homework", 5)))
# output: ValueError: <__main__.Task object at 0x00000281784F0AF0> is not in list

id(tasks.index(Task("Laundry", 3)))
# output: ValueError: <__main__.Task object at 0x000002817980E220> is not in list

id(tasks.index(Task("Museum", 4)))
# output: ValueError: <__main__.Task object at 0x0000028179894640> is not in list

id(tasks.index(Task("Ticket", 2)))
# output: ValueError: <__main__.Task object at 0x0000028179776A30> is not in list


# %%
task = (1001, "Laundry", 5)     
task_id, task_title, task_urgency = task    # 1:1 tuple unpacking

print(task_id, task_title, task_urgency)
# output: 1001 Laundry 5


# %%
user_data = ("python_user", 35, "male") 
username, age, gender = user_data           # 1:1 tuple unpacking

print(username, age, gender)
# output: python_user 35 male


# %%
x0, y0 = (90, 20)           # multi assignment technique 
(x1, y1) = 90, 20
(x2, y2) = (90, 20)

assert x0 == x1 == x2 == 90
assert y0 == y1 == y2 == 20


# %%
x3, y3 = 90, 20

assert x3 == 90
assert y3 == 20


# %%
# bad case
player_scores = [6.1, 6.5, 6.8, 7.1, 7.3, 7.6, 8.2, 8.9]

lowest0 = player_scores[0]
middles0 = player_scores[1:-1]
highest0 = player_scores[-1]

final0 = sum(middles0) / len(middles0)
final0
# output: 7.25


# %%
lowest1, middles1, highest1 = player_scores
# output: ValueError: too many values to unpack (expected 3)


# %%
# capture all asterisk
lowest2, *middles2, highest2 = player_scores    # starred expression(*)
final2 = sum(middles2) / len(middles2)

assert lowest0 == lowest2 == player_scores[0]
assert middles0 == middles2 == player_scores[1:-1]
assert highest0 == highest2 == player_scores[-1]


# %%
a, *b, c = "abcdefg"
assert b == ['b', 'c', 'd', 'e', 'f', 'g']


# %%
first_score, *scores, last_scores = [9.1, 8.9]

assert scores == []     # empty list


# %%
# multiple starred expression(wrong case)
score0, *score0, *scores1, score1 = [9.1, 8.8, 9.2, 7.7, 8.4]
# output: SyntaxError: multiple starred expression in assignment


# %%
