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
