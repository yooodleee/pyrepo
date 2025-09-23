######################################################
## create common data containers using iterables
######################################################


# %%
id_numbers = [101, 102, 103]
titles = ["Laundry", "Homework", "Soccer"]

desired_output = {101: "Laundry", 102: "Homework", 103: "Soccer"}


# %%
desired_output = []
for item in range(len(id_numbers)):     # time compleixty: O(n) -> bad case
    desired_output[id_numbers[item]] = titles[item]


# %%
desired_output = {key: value for key, value in zip(id_numbers, titles)}     # dictionary comprehension


# %%
