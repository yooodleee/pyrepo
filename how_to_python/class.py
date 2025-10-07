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
from collections import namedtuple

Task = namedtuple("Task", "title desc urgency")

task = Task("Laundry", "Wash clothes", 3)
task
# # output: 
# Task(title='Laundry', desc='Wash clothes', urgency=3)


# %%
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title 
        self.desc = desc
        self.urgency = urgency


# %%
task = Task("Laundry", "Wash clothes", 3)   # generat new instance Task object


# %%
task.__dict__
# # output: 
# {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}


# %%
# bad case: 
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
    
    def complete(self):
        self.status = "completed"
    
    def add_tag(self, tag):
        if not self.tags:
            self.tags = []
        self.tags.append(tag)

task = Task("Laundry", "Wash clothes", 3)
task.status
# # output: 
# AttributeError: 'Task' object has no attribute 'status'


# %%
task.complete()
print(task.status)
# output: completed


# %%
# better case:
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.status = "created"
        self.tags = []
    
    def complete(self):
        self.status = "completed"
    
    def add_tag(self, tag):
        self.tags.append(tag)

task = Task("Laundry", "Wash clothes", 3)
task.__dict__
# # output: 
# {'title': 'Laundry',
#  'desc': 'Wash clothes',
#  'urgency': 3,
#  'status': 'created',
#  'tags': []}


# %%
# bad case: instance attribute
class Task:
    def __init__(self, title, desc, urgency, user):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.user = user        # instance attribute -> more memory cost


# %%
# better case: class atribute
class Task:
    user = "the logged in user"     # class attribute

    def __init__(self, title, desc, urgency, user):
        pass


# %%
# generate new instance method
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"
    
    def complete(self):
        print(f"Memory Address (self): {id(self)}")
        self.status = "completed"

task = Task("Laundry", "Wash clothes", 3)
task.complete()
# output: Memory Address (self): 2419063077376


task_id = f"Memory Address (task): {id(task)}"
task_id
# output: Memory Address (task): 2419063077376


# %%
# staticmethod -> generate utility method
from datetime import datetime

class Task:
    @staticmethod
    def get_timestamp():
        now = datetime.now()
        timestamp = now.strftime("%b %d %Y, %H:%M")
        return timestamp

refresh_time = f"Date Refreshed: {Task.get_timestamp()}"    # user_defined_class.staticmethod(arg0, arg1, arg2)
refresh_time
# output: 'Date Refreshed: Oct 06 2025, 20:27'


# %%
# bad case: configure Task's instance object
task_dict = {"title": "Laundry", "desc": "Wash clothes", "urgency": 3}

task = Task(task_dict["title"], task_dict["desc"], task_dict["urgency"])


# %%
# better case: classmethod
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"
    
    @classmethod
    def task_from_dict(cls, task_dict):
        title = task_dict["title"]
        desc = task_dict["desc"]
        urgency = task_dict["urgency"]
        task_obj = cls(title, desc, urgency)    # use Task class generator
        return task_obj

task = Task.task_from_dict(task_dict)
task.__dict__
# # output: 
# {'title': 'Laundry',
#  'desc': 'Wash clothes',
#  'urgency': 3,
#  '_status': 'created'}


# %%
# bad case: unencapsulation
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"
        self.note = ""
    
    def complete(self, note = ""):
        self.status = "complted"
        self.note = self.format_note(note)
    
    def format_note(self, note):   # _: protected, __: private
        formatted_note = note.title()
        return formatted_note
    
    def _format_note(self, note): # protected method
        formatted_note = note.title()
        return formatted_note

    def __format_note(self, note): # private method
        formatted_note = note.title()
        return formatted_note


# %%
# first case: _format_note(): protected method 
task = Task("Laundry", "Wash clothes", 3)
task._format_note("abc")
# output: 'Abc'


# %%
# second case: __format_note(): private method -> can't access out of Task class
task = Task("Laundry", "Wash clothes", 3)
task.__format_note("abc")
# output: Attribute: 'Task' object has no attribute '__format_note'


# %%
# name mangling
task._Task__format_note("a note")   # _classname__private_method
# output: 'A Note'


# %%
# before: 
task.status
# output: created

task.status = "completed"
task.status
# output: completed


# %%
# after: property dacorator
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"    # protected member variable
    
    @property
    def status(self):
        return self._status
    
    def complete(self):
        self._status = "completed"


# %%
task = Task("Laundry", "Wash clothes", 3)
task.status     # can access to a status(instance method) <- property dacorator
# output: 'created'


# %%
# can't set attribute 'status'
task.status = "completed"
# output: AttributeError: can't set attribute 'status'


# %%
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"
    
    @property
    def status(self):
        return self._status
    
    @status.setter      # property setter(instance method)
    def status(self, value):
        allowed_values = ["created", "started", "completed", "suspended"]
        if value in allowed_values:
            self._status = value
            print(f"task status set to {value}")
        else:
            print(f"invalid status: {value}")

task = Task("Laundry", "Wash clothes", 3)
task.status = "completed"
# output: task status set to completed

task.status = "random"
# output: invalid status: random


# %%
