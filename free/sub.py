# %%
test = [2, 3, 4, 5]
test_list = map(float, test)
test_list
# output: <map at 0x23c3575ec40>


# %%
test_list = []

for i in test:
    i = float(i)
    test_list.append(i)
print(test_list)
# output: [2.0, 3.0, 4.0, 5.0]

test = [2, 3, 4, 5]
test_list = list(map(float, test))
print(test_list)
# output: [2.0, 3.0, 4.0, 5.0]


# %%
tst = [1, 2, 3, 4, 5]
test_list = list(map(lambda x: x * 567, tst))   # 1 * 567, 2 * 567, 3 * 567, ...
print(test_list)
# output: [567, 1134, 1701, 2268, 2835]


# %%
li = [lambda x: x * 567 for x in range(8)]      # can't access to a 'x'
li
# # output: 
# [<function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>]


# %%
li = [x * 567 for x in range(8)]
li
# output: [0, 567, 1134, 1701, 2268, 2835, 3402, 3969]


# %%
[i * 10.0 for i in range(5)]
# output: [0.0, 10.0, 20.0, 30.0, 40.0]


# %%
def test(x):
    x = int(x) + 5
    return x

[test(i) for i in range(6)]
# output: [5, 6, 7, 8, 9, 10]


# %%
def test(x):
    # check constraint 
    if not isinstance(x, int): raise TypeError 

    # operation
    x += 5
    return x

[test(i) for i in range('str')]
# output: TypeError: 'str' object cannot be interpreted as an integer

[test(i) for i in range(10)]
# output: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


# %%
[i for i in range(10) if i % 2 == 0]
# output: [0, 2, 4, 6, 8]


# %%
[i for i in range(31) if i % 2 == 0 if i % 6 == 0]
# output: [0, 5, 12, 18, 24, 30]


# %%
[(i, j) for i in range(2) for j in range(4)]
# output: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]


# %%
[(i, j) for i in range(5) if i % 2 == 0 for j in range(10) if j % 3 == 0]
# # output: 
# [(0, 0),
#  (0, 3),
#  (0, 6),
#  (0, 9),
#  (2, 0),
#  (2, 3),
#  (2, 6),
#  (2, 9),
#  (4, 0),
#  (4, 3),
#  (4, 6),
#  (4, 9)]


# %%
li = []

for i in range(5):
    for j in range(10):
        if i % 2 == 0 and j % 3 == 0:
            li.append((i, j))

print(li)
# # output: 
# [(0, 0), (0, 3), (0, 6), (0, 9), (2, 0), (2, 3), (2, 6), (2, 9), (4, 0), (4, 3), (4, 6), (4, 9)]


# %%
enumerate(li, 0)
# output: <enumerate at 0x23c36b836c0>


# %%
enumerate(li, end=0)
# output: TypeError: 'end' is an invalid keyword argument for enumerate()


# %%
for i, v in enumerate(li):
    print(i, v)

# # output: 
# 0 (0, 0)
# 1 (0, 3)
# 2 (0, 6)
# 3 (0, 9)
# 4 (2, 0)
# 5 (2, 3)
# 6 (2, 6)
# 7 (2, 9)
# 8 (4, 0)
# 9 (4, 3)
# 10 (4, 6)
# 11 (4, 9)


# %%
alp = ['a', 'b', 'c', 'd', 'e']

idx = 0
for v in alp:
    print(idx, v)
    idx += 1

# # output: 
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e


# %%
for i, v in enumerate(li, start=1):
    print(i, v)

# # output: 
# 1 (0, 0)
# 2 (0, 3)
# 3 (0, 6)
# 4 (0, 9)
# 5 (2, 0)
# 6 (2, 3)
# 7 (2, 6)
# 8 (2, 9)
# 9 (4, 0)
# 10 (4, 3)
# 11 (4, 6)
# 12 (4, 9)


# %%
nums = [1, 2, 3]
letters = ["A", "B", "C"]

for pair in zip(nums, letters):     # yields n-length tuple
    print(pair)

# # output: 
# (1, 'A')
# (2, 'B')
# (3, 'C')


# %%
# non-zip case:
nums = [1, 2, 3]
letters = ["A", "B", "C"]

for i in range(3):
    pair = (nums[i], letters[i])
    print(pair)

# # output: 
# (1, 'A')
# (2, 'B')
# (3, 'C')


# %%
for num, upper, lower in zip("12345", "ABCDE", "abcde"):    # unpacking
    print(num, upper, lower)

# # output: 
# 1 A a
# 2 B b
# 3 C c
# 4 D d
# 5 E e


# %%
num = [1, 2, 3, 4, 5]
upper = ["A", "B", "C", "D", "E"]
lower = ["a", "b", "c", "d", "e"]

for i in range(5):
    pair = (num[i], upper[i], lower[i])
    print(pair)

# # output: 
# (1, 'A', 'a')
# (2, 'B', 'b')
# (3, 'C', 'c')
# (4, 'D', 'd')
# (5, 'E', 'e')


# %%
# unzip
nums = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(nums, letters))
print(pairs)
# # output: 
# [(1, 'A'), (2, 'B'), (3, 'C')]


# %%
nums, letters = zip(*pairs)
print(nums)
# output: (1, 2, 3)

print(letters)
# output: ('A', 'B', 'C')


# %%
nums = ["1", "2", "3"]
letters = ["A"]

list(zip(nums, letters))
# output: [('1', 'A')]


# %%
def plus(x, y):
    return x * y

plus(1, 10) # 10
print((lambda x, y: x * y)(1, 10))  # 10


# %%
_list = [1, 2, 3, 4, 5]
_list = map(lambda x: x * 10, _list)    # iterable: _list

for i in _list:
    print(i)    # 10, 20, 30, 40, 50


# %%
# filter
users = [
    {'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'gender': 'M'},
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'gender': 'F'},
    {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'gender': 'M'},
    {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'gender': 'F'},
    {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'gender': 'F'}
]

def check_if_the_user_is_a_man(user):
    return user["gender"] == "M"

for man in filter(check_if_the_user_is_a_man, users):
    print(man)

# # output: 
# {'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'gender': 'M'}
# {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'gender': 'M'}


# %%
# Counter
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import Counter

total_shares = Counter()

for name, shares, price in portfolio:
    total_shares[name] += shares

total_shares['IBM']     # 150


# %%
# defaultdict
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import defaultdict

holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))

holdings['IBM'] # [(50, 91.1), (100, 45.23)]


# %%
def mul(x, y):
    return x * y

li1 = [1, 2, 3]
li2 = [10, 20, 30]

result = map(mul, li1, li2)
list(result)
# output: [10, 40, 90]


# %%
a = [1, 2, 3]
b = [2, 4, 6, 8, 10]

rst = map(lambda x, y: x * y, a, b)
print(list(rst))
# output: [2, 8, 18]


# %%
logs_example = [
	"INFO:User logged in",
	"ERROR:Not authorized user",
	"INFO:Data processed",
	"ERROR:Timeout occurred",
	"INFO:Data processed",
	"INFO:Data processed",
	"ERROR:File not found",
]

for line_number, log in enumerate(logs_example, start=1):
    if "ERROR" in log:
        print(f"Error found at lien {line_number}: {log}")

# # output: 
# Error found at lien 2: ERROR:Not authorized user
# Error found at lien 4: ERROR:Timeout occurred
# Error found at lien 7: ERROR:File not found


# %%
