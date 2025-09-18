#####################
## Range
#####################


# %%
letters = ['a', 'b', 'c', 'd', 'e']

for idx in range(len(letters)):
    print(letters[idx])


# %%
for num in range(10):
    print(num)


# %%
[num for num in range(10)]


# %%
for nm in range(3, 10):
    print(nm)


# %%
test = [1, 2, 3, 4]
test_list = map(float, test)
print(test_list)
# output: <map object at 0x000001121CEC80D0>


# %%
test = [2, 3, 4, 5]
test_list = []

for i in test:
    i = float(i)
    test_list.append(i)  # O(n)

print(test_list)
# output: [2.0, 3.0, 4.0, 5.0]


# %%
test_list = list(map(float, test))

print(test_list)
# output: [2.0, 3.0, 4.0, 5.0]


# %%
test_list = list(map(lambda x: x + 567, test))

print(test_list)
# output: [569, 570, 571, 572]


# %%
test = [1, 2, 3, 4, 5]
test_list = []

for i in test:
    i = float(i)
    test_list.append(i)

print(test_list)
# output: [1.0, 2.0, 3.0, 4.0, 5.0]


# %%
test = [1, 2, 3, 4, 5]
test_list = list(map(float, test))

print(test_list)


# %%
[i for i in range(3)]
# output: [0, 1, 2]


# %%
list(range(3))
# output: [0, 1, 2]


# %%
[i + 10 for i in range(10)]
# output: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# %%
def test(x):
    x = str(x) + 'ab'
    return x

[test(i) for i in range(5)]
# output: ['0ab', '1ab', '2ab', '3ab', '4ab']


# %%
[str(i) + 'ab'  for i in range(5)]
# output: ['0ab', '1ab', '2ab', '3ab', '4ab']


# %%
li = []

for i in range(2):
    for j in range(3):
        li.append((i, j))

print(li)
# output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]


# %%
[(i, j) for i in range(2) for j in range(3)]
# output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]


# %%
