####################################
## f-string
####################################


# %%
scores = [score for score in range(90, 100)]

total_scores = sum(scores)
subject_count = len(scores)
average_scores = total_scores / subject_count

summary_text = f"Your Average Score: {average_scores}."


# %%
# not DRY
task_ids = [1, 2, 3, 4, 5]
task_names = ['Get', 'Create', 'Delete', 'Patch', 'Put']
task_urgencies = [5, 4, 3, 2, 1]

for i in range(5):
    print(f'{task_ids[i]:^12}{task_names[i]:^12}{task_urgencies[i]:^12}')

# # output:
#      1          Get          5      
#      2         Create        4      
#      3         Delete        3      
#      4         Patch         2      
#      5          Put          1   


# %%
# not DRY
task_ids = [1, 2, 3, 4, 5]
tasks_names = ["Put", "Patch", "Create", "Do", "Delete"]
tasks_urgencies = [5, 4, 3, 2, 1]

for i in range(5):
    print(f'{task_ids[i]:^10}{task_names[i]:^10}{task_urgencies[i]:^10}')

# # output: 
#     1        Get        5     
#     2       Create      4     
#     3       Delete      3     
#     4       Patch       2     
#     5        Put        1     


# %%
def create_formatted_records(fmt):
    for i in range(5):
        task_id = task_ids[i]
        name = task_names[i]
        urgency = task_urgencies[i]

        print(f'{task_id:{fmt}}{name:{fmt}}{urgency:{fmt}}')


create_formatted_records('^18')
# # output: 
#         1                Get                5         
#         2               Create              4         
#         3               Delete              3         
#         4               Patch               2         
#         5                Put                1  

create_formatted_records('^10')
# # output: 
#     1        Get        5     
#     2       Create      4     
#     3       Delete      3     
#     4       Patch       2     
#     5        Put        1     

create_formatted_records('*^10')
# # output: 
# ****1********Get********5*****
# ****2*******Create******4*****
# ****3*******Delete******3*****
# ****4*******Patch*******2*****
# ****5********Put********1*****


# %%
large_prime_number = 1000000007

print(f"Use commas: {large_prime_number: ,d}")
# output: Use commas: 1,000,000,007
 
 
# %%
decimal_number = 1.23456

print(f"Two digits: {decimal_number:.2f}")
# output: 1.23

print(f"Four digits: {decimal_number:.4f}")
# output: 1.2346


# %%
sci_number = 0.000000004127733

print(f"Sci notation: {sci_number:e}")
# output: 4.127733e-09

print(f"Sci notation: {sci_number:.2e}")
# output: 4.13e-09


# %%
sci_number = 12345

print(f"result: {sci_number:b}")
# output: format: 11000000111001

print(f"result: {sci_number:c}")
# output: result: 〹

print(f"result: {sci_number:d}")
# output: 12345

print(f"result:{sci_number:o}")
# output: 30071

print(f"result:{sci_number:x}")
# output: 3039


# %%
sci_number = 0.123456789

print(f"result: {sci_number:.2e}")
# output: result: 1.23e-01

print(f"result: {sci_number:.2f}")
# output: result: 0.12

print(f"result: {sci_number:2g}")
# output: result: 0.123457

print(f"result: {sci_number:.2%}")
# output: result: 12.35%


# %%
age = input("enter your age: ")

type(age)
# output: <class 'str'>

assert age > 20


# %%
bad_username0 = "123!@#"
assert bad_username0.isalnum() == False # a-z, A-Z, 1-9

bad_username1 = "abc..."
assert bad_username1.isalnum() == False

good_username = "1a2b3c"
assert good_username.isalnum() == True 

assert "abcdefg".isalpha() == True # alphabetic string

assert "12345".isnumeric() == True # numeric string

assert "3.5".isnumeric() == False 
assert "-3".isnumeric() == False 

assert "3.5".isdecimal() == False 
assert "-3".isdecimal() == False

assert "3.5".isdigit() == False
assert "-3".isdigit() == False


# %%
float("7.6b")
# output: ValueError: could not convert string to float: '7.6b'

int("frozen")
# output: ValueError: invalid literal for int() with base 10: 'frozen'


# %%
def cast_number(number_str):
    try:
        casted_number = float(number_str)
    except ValueError:
        print(f"Couldn't cast {repr(number_str)} to a number") # canonical string representation 

    else:
        print(f"Casting {repr(number_str)} to {casted_number}")


cast_number("7.6b")
# output: Couldn't cast '7.6b' to a number

cast_number("frozen")
# output: Couldn't cast 'frozen' to a number

cast_number("7.6")
# output: Casting '7.6' to 7.6 

cast_number("2")
# output: Casting '2' to 2.0



# %%
numbers_list_str = "[1, 2, 3]"          # literal 
numbers_tuple_str = "(1, 2, 3)"
numbers_dict_str = "{1: 'one', 2: 'two', 3: 'three'}"


list(numbers_list_str)
# output: ['[', '1', ',', ' ', '2', ',', ' ', '3', ']']

tuple(numbers_tuple_str)
# output: ('(', '1', ',', ' ', '2', ',', ' ', '3', ')')

dict(numbers_dict_str)
# output: dictionary update sequence element #0 has length 1; 2 is required


# %%
assert eval(numbers_list_str) == [1, 2, 3]      # evaluate the given source(string)

assert eval(numbers_tuple_str) == (1, 2, 3)

assert eval(numbers_dict_str) == {1: 'one', 2: 'two', 3: 'three'}


# %%
numbers_lsit_str = "[1, 2, 3]"
stripped_numbers_str = numbers_list_str.strip("[]")
numbers_list = [int(x) for x in stripped_numbers_str.split(",")]

print(numbers_list)
# output: [1, 2, 3]


# %%
numbers_tuple_str = "(1, 2, 3)"
stripped_numbers_str = numbers_tuple_str.strip("()")

print(stripped_numbers_str)
# output: 1, 2, 3

eval(stripped_numbers_str)
# output: (1, 2, 3)

assert eval(stripped_numbers_str) == (1, 2, 3)


# %%
numbers_dict_str = "{1: 'one', 2: 'two', 3: 'three'}"
stripped_numbers_str = numbers_dict_str.strip("{}")

print(stripped_numbers_str)
# output: 1: 'one', 2: 'two, 3: 'three' 

eval(stripped_numbers_str)
# output: invalid syntax 


# %%
eval("[1, 2")
# output: SyntaxError: unexpected EOF while parsing

eval("[1, 2]")
# output: 

exec("[1, 2]")
# output: 

exec("[1, 2")
# output: SyntaxError: unexpected EOF while parsing


# %%

# Wrong case
given_string = "[1, 2"

try:
    source = given_string.strip("[]")           # "1, 2"
    ls = [int(x) for x in source.split(",")]    # [1, 2]

except SyntaxError:
    print(f"Couldn't strip {given_string}")

else:
    print(f"Success {given_string} to {ls}")

# output: Success [1, 2 to [1, 2]



# %%

# Correct case 1
import ast

given_string = "[1, 2"
# given_string = "[1, 2]"

try:
    ls = ast.literal_eval(given_string) # safely evaluate given string => SyntaxError

except SyntaxError:
    print(f"Couldn't strip {given_string}")

else:
    print(f"Success {given_string} to ls")

# output: Couldn't strip [1, 2


# %%

# Correct case 2
given_string = "[1, 2"

try:
    if not (given_string.startswith("[") and given_string.endswith("]")):
        raise SyntaxError("Invalid list format")
    
    source = given_string.strip("[]")
    ls = [int(x) for x in source.split(",") if x.strip()]

except SyntaxError:
    print(f"Couldn't strip {given_string}")

else:
    print(f"Success {given_string} to {ls}")


# %%
def check_given_string(given_string):
    try:
        if not (given_string.startswith("[") and given_string.endswith("]")):
            raise SyntaxError("Invalid list format")

        source = given_string.strip("[]")
        ls = [int(x) for x in source.split(",") if x.strip()]
    
    except SyntaxError:
        print(f"Couldn't strip {given_string}")
    
    else:
        print(f"Success {given_string} to {ls}")


check_given_string("[1, 2")
# output: Couldn't strip [1, 2

check_given_string("[1, 2]")
# output: Couldn't strip [1, 2]


# %%
style_settings = "font-size=large, " "font=Arial, " "color=balck, " "align=center"

# only auto connected with string literal
print(style_settings)
# output: font-size=large, font=Arial, color=black, align=center


# %%
settings = {"font_size": "large", "font": "Arial", "color": "black", "align": "center"}

# f-string => auto connect
styles = f"font-size={settings['font_size']}, " \
         f"font={settings['font']}, " \
         f"color={settings['color']}, " \
         f"align={settings['align']}"

print(styles)
# output: font-size=large, font=Arial, color=black, align=center


# %%
