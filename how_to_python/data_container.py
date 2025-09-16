####################################
## Data Container
####################################


# %%
numbers = [1, 2, 3]
print(numbers)
# output: [1, 2, 3]

numbers.insert(0, 0) # index, value
print(numbers)
# output: [0, 1, 2, 3]

numbers.append(4)
print(numbers)
# output: [0, 1, 2, 3, 4]

numbers.extend([5, 6, 7])
print(numbers)
# output: [0, 1, 2, 3, 4, 5, 6, 7]

numbers.remove(5)
print(numbers)
# output: [0, 1, 2, 3, 4, 6, 7]

del numbers[3]
print(numbers)
# output: [0, 1, 2, 4, 6, 7]


# %%
integers_tuple = (1, 2, 3)
integers_tuple.append(4)
# output: AttributeError: 'tuple' has no attribute 'append'

integers_tuple[0] = 'zero'
# output: TypeError: 'tuple' object does not support item assignment


# %%
