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
numbers_list_str = "[1, 2]"
numbers_tuple_str = "(1, 2)"
numbers_dict_str = "{1: 'one', 2: 'two'}"

list(numbers_list_str) 
# output: ['[', '1', ',', ', '2', ']']

tuple(numbers_tuple_str)
# output: ('(', '1', ',', ' ', '2', ')')

dict(numbers_dict_str)
# output: ValueError: dictionary update sequence element #0 has length 1; 2 is required


# %%
assert eval(numbers_list_str) == [1, 2]

assert eval(numbers_tuple_str) == (1, 2)

assert eval(numbers_dict_str) == {1: 'one', 2: 'two'}


# %%
list_str = "[1, 2, 3, 4]"
stripped_str = list_str.strip("[]")
number_list = [int(x) for x in stripped_str.split(",")]

print(number_list)
# output: [1, 2, 3, 4]


# %%
fruit0 = "apple"
fruit1 = "banana"
fruit2 = "orange"

# liked_fruits = "apple, banan, orange"


#%%
visited_countries = "United States, China, France, Canada"

# countries = ["United States, China, France, Canada"]

#%%
style_settings = "font-size=large, " "font=Arial, " "color=black, " "align=center"

print(style_settings)
# output: font-size=large, font=Arial, color=black, align=center


# %%
settings = {"font-size": "large", "font": "Arial", "color": "black", "align": "center"}

styles = f"font-size={settings['font-size']}, " \
         f"font={settings['font']}, " \
         f"color={settings['color']}, " \
         f"align={settings['align']}"

print(styles)
# output: font-size=large, font=Arial, color=black, align=center


# %%
style_settings = ["font-size=large", "font=Arial", "color=black", "align=center"]
merged_style = ", ".join(style_settings)

print(merged_style)
# output: font-size=large, font=Arial, color=black, align=center


# %%
tasks = ["Homework", "Grocery", "Laundry", "Museum Trip", "Buy Furniture"]
note = ", ".join(tasks)

print("Remaining Tasks: ", note)
# output: Remaining Tasks: Homework, Grocery, Laundry, Musem Trip, Buy Furniture 


# %%
tasks.remove("Buy Furniture")
tasks.remove("Homework")

print("Remaining Tasks: ", ", ".join(tasks))
# output: Remaining Tasks: Grocery, Laundry, Museum Trip


# %%
