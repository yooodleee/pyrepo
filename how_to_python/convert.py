####################################################
## Convert strings to retrieve the represented data
####################################################

#%%
float("3.25")
# output: 3.25

float("-2")
# output: -2.0

# %%
int("-5")
# output: -5

int("123")
# output: 123


#%%
float("3.5a")
# output: ValueError: could not convert string to floag: '3.5a'

int("one")
# output: ValueError: invalid literal for int() with base 10: 'one'


# %%
def cast_number(number_str):
    try:
        casted_number = float(number_str)
    except ValueError:
        print(f"Couldn't cast {repr(number_str)} to a number") # repr()
    else:
        print(f"Casting {repr(number_str)} to {casted_number}")

cast_number("1.5")
# output: Casting '1.5' to 1.5

cast_number("2.3a")
# output: Couldn't cast '2.3a' to a number


# %%
