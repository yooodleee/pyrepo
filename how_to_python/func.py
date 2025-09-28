################################
## User Friendly Function
################################


# %%
numbers = [4, 5, 7, 2]
numbers.sort()

assert numbers == [2, 4, 5, 7]


# %%
# setting keyword only key, reverse arguments -> *
numbers.sort(reverse=True)  # reverse(*, key=None, reverse=False) -> default arguments

assert numbers == [7, 5, 4, 2]


# %%
# wrong case 
numbers.sort(True)  # setting keyword only arguments


# %%
