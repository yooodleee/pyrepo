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
