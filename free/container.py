###############################
## Data Container 
###############################


# %%
nums = [1, 2, 3]        # mutability of list -> memory overhead
nums 
# output: [1, 2, 3]


# %%
nums.insert(0, 6) # index(0), object(6)
nums 
# output: [6, 1, 2, 3]


# %%
nums.append(4)
nums 
# output: [6, 1, 2, 3, 4]


# %%
nums.extend([5, 6, 7])
nums 
# output: [6, 1, 2, 3, 4, 5, 6, 7]


# %%
nums.append([5, 6, 7])
nums 
# output: [6, 1, 2, 3, 4, 5, 6, 7, [5, 6, 7]]


# %%
nums.remove(5)
nums 
# output: [6, 1, 2, 3, 4, 6, 7, [5, 6, 7]]


# %%
del nums[2]
nums 
# output: [6, 1, 3, 4, 6, 7, [5, 6, 7]]


# %%
integers = (1, 2, 3)    # immutability of tuple -> TypeError, AttributeError
integers.append(4)
# output: 'tuple' object has no attribute 'append'


# %%
integers[0] = 'zero'    # allocate new val to tuple instance
# output: 'tuple' object does not support item assignment


# %%
