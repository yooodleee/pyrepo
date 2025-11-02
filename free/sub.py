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
