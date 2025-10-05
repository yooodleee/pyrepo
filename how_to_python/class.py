##############################
## User Defined Class
##############################


# %%
class Task:
    def __init__(self): # initialization 
        print("Creating an instance of Task class")

task = Task()
# output: Creating an instance of Task class


# %%
class Task:
    def __init__(self):
        print(f"Memory address (self): {id(self)}") # self address

task = Task()
# output: Memory address (self): 2056529553392

task_address = f"Memory address (self):{id(task)}"  # task address -> same instance object
# output: Memory address (self): 2056529553392


# %%
class Task:
    def __init__(self):     # ref __new__'s new_task(return)
        print(f"Memory address (self): {id(self)}")
    
    def __new__(cls):       # __new__() -> __init__()
        new_task = object.__new__(cls)
        print(f"__new__ gets called, creating object at {id(new_task)}")
        return new_task     # return new instance object(new_task)

task = Task()
# # output: 
# __new__ gets called, creating object at 2056529552192
# __init__ gets called, creating object at 2056529552192


# %%
task = Task.__new__(Task)
# # output: 
# __new__ gets called, creating object at 2056529552192


Task.__init__(task)
# # output: 
# __init__ gets called, creating object at 2056529552192


# %%
# self is not a keyword 
def = 5
# output: SyntaxError: invalid syntax

class = 7
# output: SyntaxError: invalid syntax

self = 9


# %%
# iskeyword?
import keyword

words_to_check = ["def", "class", "self", "lambda"]
for word in words_to_check:
    print(f"Is {word:^8} a keyword? {keyword.iskeyword(word)}")

# # output: 
# Is   def    a keyword? True
# Is  class   a keyword? True
# Is   self   a keyword? False
# Is  lambda  a keyword? True


# %%
class Task:
    def __init__(this):
        print("An instance is created with this instead of self.")

task = Task()
# output: An instance is created with this instead of self.


# %%
