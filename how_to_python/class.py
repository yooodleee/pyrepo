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
print(task)
# # output: 
# <__main__.Task object at 0x000001D8C8E84760>


# %%
# __str__()
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title 
        self.desc = desc
        self.urgency = urgency
    
    def __str__(self):  # instance method, return str
        return f"{self.title}: {self.desc}, urgency level {self.urgency}"

task = Task("Laundry", "Wash clothes", 3)
print(task)
# output: Laundry: Wash clothes, urgency level 3

task
# output: <__main__.Task at 0x1d8c8e84190>


# %%
# bad case:
planned_task = f"Next Task - {task}"

print(planned_task)
# output: Next Task - Laundry: Wash clothes, urgency level 3

# better case: str(instance)
str(task)
# output: 'Laundry: Wash clothes, urgency level 3'


# %%
planned_task    # val(str)
# output: 'Next Task - Laundry: Wash clothes, urgency level 3'

task            # task instance
# output: <__main__.Task at 0x1d8c8eaf070>


# %%
# __repr__()
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
    
    def __str__(self):
        return f"{self.title}: {self.desc}, urgency level {self.urgency}"
    
    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r}, {self.urgency})"     # !r -> __repr__()

task = Task("Laundry", "Wash clothes", 3)
task
# output: Task('Laundry', 'Wash clothes', 3)

# call __repr__() method -> repr(instance): task instance
repr(task)
# output: "Task('Laundry', 'Wash clothes', 3)"


# %%
task = Task("Laundry", "Wash clothes", 3)

task_repr = repr(task)

task_repr_eval = eval(task_repr)

print(type(task_repr_eval))
# output: <class '__main__.Task'>

print(task_repr_eval)
# output: Laundry: Wash clothes, urgency level 3


# %%
# bad case: no conversion flag(!r)
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
    
    def __str__(self):
        return f"{self.title}: {self.desc}, urgency level {self.urgency}"   
    
    def __repr__(self):
        return f"Task({self.title}, {self.desc}, {self.urgency})"   # no conversion flag(!r)

task = Task("Laundry", "Wash clothes", 3)

print(repr(task))
# output: Task(Laundry, Wash clothes, 3)


# %%
eval(repr(task))
# output: SyntaxError: invalid syntax. Perhaps you forgot a comma?


# %%
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def login(self):
        print(f"An employee {self.name} just logged in.")
    
    def logout(self):
        print(f"An employee {self.name} just logged out.")

class Supervisor(Employee):
    pass    

# generate Supervisor instance object.
supervisor = Supervisor("John", "1001")

print(supervisor.name)
# output: John

supervisor.login()
# output: An employee John just logged in.

supervisor.logout()
# output: An employee John just logged out.


# %%
# overriding: Method Resolution Order(MRO)
class Supervisor(Employee):
    def login(self):
        print(f"A supervisor {self.name} just logged in.")

supervisor = Supervisor("John", "1001")

supervisor.login()
# output: A supervisor John just logged in.


# %%
Supervisor.mro()
# output: [__main__.Supervisor, __main__.Employee, object]


# %%
# super()
class Supervisor(Employee):
    def logout(self):
        super().logout()    # generate parent class's proxy instance(ref Employee class)
        print("Additional logout actions for a supervisor")

supervisor = Supervisor("John", "1001")

supervisor.logout() # 1) Employee logout() # 2) Supervisor logout()
# # output: 
# An employee John just logged out.
# Additional logout actions for a supervisor


# %%
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def _request_vacation(self):    # protected method
        print("Send a vacation request to the employee's supervisor.")
    
    def __transfer_group(self):     # private method
        print("Transfer the employee to a different group.")

class Supervisor(Employee):
    def do_something(self):
        self._request_vacation()    # access to a protected method
        self.__transfer_group()     # access to a private method

supervisor = Supervisor("John", "1001")
supervisor.do_something()
# # output: 
# Send a vacation request to the employee's supervisor.
# AttributeError: 'Supervisor' object has no attribute '_Supervisor__transfer_group'


# %%
# wrong case:
def move_to(direction: str, distance: float):
    if direction in {"north", "south", "east", "west"}:
        message = f"Go to the {direction} for {distance} miles"
    else:
        message = "Wrong input for direction"
    print(message)

move_to("North", 2)
# output: Wrong input for direction


# %%
class Direction: 
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

print(Direction.NORTH)
# output: 0

print(Direction.SOUTH)
# output: 1


# %%
def move_to(direction: Direction, distance: float):
    pass

move_to(Direction.NORTH, 2)
# outut: Expected type 'Direction', got 'int' instead


# %%
from enum import Enum

class Direction(Enum):  # subclassing
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

class DirectionOneLiner(Enum):
    NORTH = 0; SOUTH = 1; EAST = 2; WEST = 3


# %%
north = Direction.NORTH

print("north type:", type(north))
# output: north type: <enum 'Direction'>

print("north check instance of Direction:", isinstance(north, Direction))
# output: north check instance of Direction: True


# %%
print("north name:", north.name)
# output: north name: NORTH

print("north value:", north.value)
# output: north value: 0


# %%
direction_value = 2

direction = Direction(direction_value)

print("Direction to go:", direction)
# output: Direction to go: Direction.EAST


# %%
unknown_direction = Direction(8)
# output: ValueError: 8 is not a valid Direction


# %%
all_directions = list(Direction)

print(all_directions)
# output: [<Direction.NORTH: 0>, <Direction.SOUTH: 1>, <Direction.EAST: 2>, <Direction.WEST: 3>]


# %%
for direction in Direction:
    pass


# %%
# bad case:
def move_to(direction: Direction, distance: float):
    if direction in Direction:
        message = f"Go to the {direction} for {distance} miles"
    else:
        message = "Wrong input for direction"
    print(message)

move_to(Direction.NORTH, 3)
# output: Go to the Direction.NORTH for 3 miles


# %%
# better case: add new user defined method
class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    def __str__(self):
        return self.name.lower()
    
def move_to(direction: Direction, distance: float):
    if direction in Direction:
        message = f"Go to the {direction} for {distance} miles"
    else:
        message = "Wrong input for direction"
    print(message)

move_to(Direction.NORTH, 3)
# output: Go to the north for 3 miles


# %%
# generate dataclass
from dataclasses import dataclass

@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float

bill0 = Bill(5, 60.5, "John", 10)

bill_output = f"Today's bill: {bill0}"

print(bill_output)
# output: Today's bill: Bill(table_number=5, meal_amount=60.5, served_by='John', tip_amount=10)


# %%
print(Bill.__annotations__)
# output: {'table_number': <class 'int'>, 'meal_amount': <class 'float'>, 'served_by': <class 'str'>, 'tip_amount': <class 'float'>}


# %%
# set filed's default value
@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float = 0

bill1 = Bill(5, 60.5, "John")
print(bill1)
# output: Bill(table_number=5, meal_amount=60.5, served_by='John', tip_amount=0)


# %%
# wrong case:
@dataclass
class TestClass:
    attribute_with_default: int = 0
    attr1: str
    attr2: float

# output: TypeError: non-default argument 'attr1' follows default argument


# %%
# correct case:
@dataclass
class TestClass:
    attr1: str
    attr2: float
    attribute_with_default: int = 0


# %%
@dataclass(frozen=True)
class ImmutableBill:
    meal_amount: float
    served_by: str

immutable_bill = ImmutableBill(50, "John")
immutable_bill.served_by = "David"
# output: FrozenInstanceError: cannot assign to field 'served_by'


# %%
@dataclass
class BaseBill:
    meal_amount: float

@dataclass
class TippedBill(BaseBill):
    tip_amount: float

tipped_bill = TippedBill(60, 10)

print(tipped_bill)
# output: TippedBill(meal_amount=60, tip_amount=10)


# %%
# wrong case:
@dataclass
class BaseBill:
    meal_amount: float = 50

@dataclass
class TippedBill(BaseBill):
    tip_amount: float

# output: TypeError: non-default argument 'tip_amount' follows default argument


# %%
# correct case:
@dataclass
class BaseBill:
    meal_amount: float = 50

@dataclass
class TippedBill(BaseBill):
    tip_amount: float = 0


# %%
tasks_json = """
[
    {
        "title": "Laundry",
        "desc": "Wash clothes",
        "urgency": 3
    },
    {
        "title": "Homework",
        "desc": "Physics + Math",
        "urgency": 5
    }
]
"""


# %%
import json

tasks_read = json.loads(tasks_json)

print(tasks_read)
# # output: 
# [{'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}, {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5}]


# %%
# use classmethod
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    desc: str
    urgency: int

    @classmethod
    def task_from_dict(cls, task_dict): # cls: Task class
        return cls(**task_dict)         # access to a dictionary object and return to a keyword argument

tasks = [Task.task_from_dict(x) for x in tasks_read]

print(tasks)
# # output: 
# [Task(title='Laundry', desc='Wash clothes', urgency=3), Task(title='Homework', desc='Physics + Math', urgency=5)]


# %%
# loads method -> a JSON document to a Python object

json.loads("2.2")
# output: 2.2

json.loads("A string")
# output: JSONDecodeError: Expecting value: line 1 column 1 (char 0)

json.loads('"A string"')
# output: 'A string'

json.loads('false') # bool
# output: False

json.loads('null') is None  # JSON null -> None
# output: True

# %%
