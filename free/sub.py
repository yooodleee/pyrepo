# %%
test = [2, 3, 4, 5]
test_list = map(float, test)
test_list
# output: <map at 0x23c3575ec40>


# %%
test_list = []

for i in test:
    i = float(i)
    test_list.append(i)
print(test_list)
# output: [2.0, 3.0, 4.0, 5.0]

test = [2, 3, 4, 5]
test_list = list(map(float, test))
print(test_list)
# output: [2.0, 3.0, 4.0, 5.0]


# %%
tst = [1, 2, 3, 4, 5]
test_list = list(map(lambda x: x * 567, tst))   # 1 * 567, 2 * 567, 3 * 567, ...
print(test_list)
# output: [567, 1134, 1701, 2268, 2835]


# %%
li = [lambda x: x * 567 for x in range(8)]      # can't access to a 'x'
li
# # output: 
# [<function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>,
#  <function __main__.<listcomp>.<lambda>(x)>]


# %%
li = [x * 567 for x in range(8)]
li
# output: [0, 567, 1134, 1701, 2268, 2835, 3402, 3969]


# %%
[i * 10.0 for i in range(5)]
# output: [0.0, 10.0, 20.0, 30.0, 40.0]


# %%
def test(x):
    x = int(x) + 5
    return x

[test(i) for i in range(6)]
# output: [5, 6, 7, 8, 9, 10]


# %%
def test(x):
    # check constraint 
    if not isinstance(x, int): raise TypeError 

    # operation
    x += 5
    return x

[test(i) for i in range('str')]
# output: TypeError: 'str' object cannot be interpreted as an integer

[test(i) for i in range(10)]
# output: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


# %%
[i for i in range(10) if i % 2 == 0]
# output: [0, 2, 4, 6, 8]


# %%
[i for i in range(31) if i % 2 == 0 if i % 6 == 0]
# output: [0, 5, 12, 18, 24, 30]


# %%
[(i, j) for i in range(2) for j in range(4)]
# output: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]


# %%
[(i, j) for i in range(5) if i % 2 == 0 for j in range(10) if j % 3 == 0]
# # output: 
# [(0, 0),
#  (0, 3),
#  (0, 6),
#  (0, 9),
#  (2, 0),
#  (2, 3),
#  (2, 6),
#  (2, 9),
#  (4, 0),
#  (4, 3),
#  (4, 6),
#  (4, 9)]


# %%
li = []

for i in range(5):
    for j in range(10):
        if i % 2 == 0 and j % 3 == 0:
            li.append((i, j))

print(li)
# # output: 
# [(0, 0), (0, 3), (0, 6), (0, 9), (2, 0), (2, 3), (2, 6), (2, 9), (4, 0), (4, 3), (4, 6), (4, 9)]


# %%
enumerate(li, 0)
# output: <enumerate at 0x23c36b836c0>


# %%
enumerate(li, end=0)
# output: TypeError: 'end' is an invalid keyword argument for enumerate()


# %%
for i, v in enumerate(li):
    print(i, v)

# # output: 
# 0 (0, 0)
# 1 (0, 3)
# 2 (0, 6)
# 3 (0, 9)
# 4 (2, 0)
# 5 (2, 3)
# 6 (2, 6)
# 7 (2, 9)
# 8 (4, 0)
# 9 (4, 3)
# 10 (4, 6)
# 11 (4, 9)


# %%
alp = ['a', 'b', 'c', 'd', 'e']

idx = 0
for v in alp:
    print(idx, v)
    idx += 1

# # output: 
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e


# %%
for i, v in enumerate(li, start=1):
    print(i, v)

# # output: 
# 1 (0, 0)
# 2 (0, 3)
# 3 (0, 6)
# 4 (0, 9)
# 5 (2, 0)
# 6 (2, 3)
# 7 (2, 6)
# 8 (2, 9)
# 9 (4, 0)
# 10 (4, 3)
# 11 (4, 6)
# 12 (4, 9)


# %%
nums = [1, 2, 3]
letters = ["A", "B", "C"]

for pair in zip(nums, letters):     # yields n-length tuple
    print(pair)

# # output: 
# (1, 'A')
# (2, 'B')
# (3, 'C')


# %%
# non-zip case:
nums = [1, 2, 3]
letters = ["A", "B", "C"]

for i in range(3):
    pair = (nums[i], letters[i])
    print(pair)

# # output: 
# (1, 'A')
# (2, 'B')
# (3, 'C')


# %%
for num, upper, lower in zip("12345", "ABCDE", "abcde"):    # unpacking
    print(num, upper, lower)

# # output: 
# 1 A a
# 2 B b
# 3 C c
# 4 D d
# 5 E e


# %%
num = [1, 2, 3, 4, 5]
upper = ["A", "B", "C", "D", "E"]
lower = ["a", "b", "c", "d", "e"]

for i in range(5):
    pair = (num[i], upper[i], lower[i])
    print(pair)

# # output: 
# (1, 'A', 'a')
# (2, 'B', 'b')
# (3, 'C', 'c')
# (4, 'D', 'd')
# (5, 'E', 'e')


# %%
# unzip
nums = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(nums, letters))
print(pairs)
# # output: 
# [(1, 'A'), (2, 'B'), (3, 'C')]


# %%
nums, letters = zip(*pairs)
print(nums)
# output: (1, 2, 3)

print(letters)
# output: ('A', 'B', 'C')


# %%
nums = ["1", "2", "3"]
letters = ["A"]

list(zip(nums, letters))
# output: [('1', 'A')]


# %%
def plus(x, y):
    return x * y

plus(1, 10) # 10
print((lambda x, y: x * y)(1, 10))  # 10


# %%
_list = [1, 2, 3, 4, 5]
_list = map(lambda x: x * 10, _list)    # iterable: _list

for i in _list:
    print(i)    # 10, 20, 30, 40, 50


# %%
# filter
users = [
    {'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'gender': 'M'},
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'gender': 'F'},
    {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'gender': 'M'},
    {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'gender': 'F'},
    {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'gender': 'F'}
]

def check_if_the_user_is_a_man(user):
    return user["gender"] == "M"

for man in filter(check_if_the_user_is_a_man, users):
    print(man)

# # output: 
# {'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'gender': 'M'}
# {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'gender': 'M'}


# %%
# Counter
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import Counter

total_shares = Counter()

for name, shares, price in portfolio:
    total_shares[name] += shares

total_shares['IBM']     # 150


# %%
# defaultdict
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import defaultdict

holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))

holdings['IBM'] # [(50, 91.1), (100, 45.23)]


# %%
def mul(x, y):
    return x * y

li1 = [1, 2, 3]
li2 = [10, 20, 30]

result = map(mul, li1, li2)
list(result)
# output: [10, 40, 90]


# %%
a = [1, 2, 3]
b = [2, 4, 6, 8, 10]

rst = map(lambda x, y: x * y, a, b)
print(list(rst))
# output: [2, 8, 18]


# %%
logs_example = [
	"INFO:User logged in",
	"ERROR:Not authorized user",
	"INFO:Data processed",
	"ERROR:Timeout occurred",
	"INFO:Data processed",
	"INFO:Data processed",
	"ERROR:File not found",
]

for line_number, log in enumerate(logs_example, start=1):
    if "ERROR" in log:
        print(f"Error found at lien {line_number}: {log}")

# # output: 
# Error found at lien 2: ERROR:Not authorized user
# Error found at lien 4: ERROR:Timeout occurred
# Error found at lien 7: ERROR:File not found


# %%
import time

def heavy_work(name):
		result = 0
		for i in range(4000000):
				result += i
		print('%s done' % name)

start = time.time()

for i in range(4):
		heavy_work(i)

end = time.time()

print("executed time: %f seconds" % (end - start))
# # output: 
# 0 done
# 1 done
# 2 done
# 3 done
# executed time: 0.293246 seconds


# %%
from multiprocessing import Process
import time
import logging 

def main():
    # set Logging format
    form = "%(asctime)s: %(message)s"
    logging.basicConfig(form=form, level=logging.INFO, datefmt="%H:%M:%S")

    # check method's argument
    p = Process(target=process_function, args=('First', ))
    logging.info("Main-Process: before creating Process")

    # start process
    p.start()
    logging.info("Main-Process: During Process...")

    # wait until process terminates
    logging.info("Main-Process: Joined Process")
    p.join()

    # # If you need to force a process to terminate under certain conditions
    # logging.info("Main-Process: Terminated Process...")
    # p.terminate()

    # check process's status
    print(f'Process p is alive: {p.is_alive()}')

def process_function(name):
    print(f"This is Sub-Process {name}: starting")
    time.sleep(3)
    print(f"This is Sub-Process {name}: finishing")

if __name__ == "__main__":
    main()


# %%
from multiprocessing import Process, Queue, current_process
import time
import os


def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
    
    # produce
    q.put(sub_total)
    
    # process's id and result
    print(f'Process ID: {process_id} Process Name: {process_name}')
    print(f'Result is: {sub_total}')

def main():
    parent_process_id = os.getpid()
    print(f'Parent process ID: {parent_process_id}')

    processes = list()

    # execution time recording for performance measurement
    start = time.time()

    # declaration Queue
    q = Queue()
    for i in range(5):
        p = Process(name=str(i), target=worker, args=(i, 10000, q))

        processes.append(p)
        p.start()
    
    for process in processes:
        process.join()
    
    # pure execution time 
    print("---- %s seconds ----" % (time.time() - start))

    # exit flag
    q.put('exit')
    total = 0
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp
    
    print(f'Main-Processing Total Count: {total}')
    print("Multi process is Done!")

if __name__ == "__main__":
    main()

# # output: 
# Parent process ID: 4012
# ---- 0.12848114967346191 seconds ----
# Main-Processing Total Count: 0
# Multi process is Done!


# %%
from multiprocessing import Process, Pipe, current_process
import time
import os


def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
    
    # lock the pipeline when child sends with send 
    conn.send(sub_total)
    conn.close()

    # process's id and result
    print(f'Process ID: {process_id} Process Name: {process_name}')
    print(f'Result is: {sub_total}')

def main():
    parent_process_id = os.getpid()
    print(f'Parent process ID: {parent_process_id}')

    # execution time recording for performance measurement
    start = time.time()

    # declaration Pipe
    parent_conn, child_conn = Pipe()

    p = Process(name='child', target=worker, args=('child', 10000, child_conn))
    p.start()
    p.join()

    # pure execution time 
    print("---- %s seconds ----" % (time.time() - start))

    print(f'Main-Processing Total Count: {parent_conn.recv()}') # receive a object
    print("Multi process is Done!")

if __name__ == "__main__":
    main()


# %%
# Data Descriptor: __get__(), __set__()
class Descriptor:
    def __get__(self, instance, owner):
        print("Get the value of an attribute")
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        print("Set the value of an attribute")
        instance.__dict__[self.name] = value
    
class MyClass:
    x = Descriptor()


# %%
# Non-Data Descriptor: __get__()
class NonDescriptor:
    def __get__(self, instance, owner):
        print("Get the value of an attribute")
        return instance.__dict__[self.name]
    
class MyClass:
    x = NonDescriptor()


# %%
# Class Descriptor
class ClassDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print("Get the value of an attribute")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("Set the value of an attribute")
        instance.__dict__[self.name] = value

class MyClass:
    x = ClassDescriptor()

class MyOtherClass(MyClass):
    pass

obj1 = MyClass()
obj2 = MyOtherClass()
obj1.x = 10
obj2.x = 20
print(obj1.x)
print(obj2.x)

# # output: 
# Set the value of an attribute
# Set the value of an attribute
# Get the value of an attribute
# 10
# Get the value of an attribute
# 20


# %%
# Slots
class SlotClass:
    __slots__ = ('name', )

class NoSlotClass:
    pass

slot = SlotClass()
no_slot = NoSlotClass()
no_slot.name = 'a'

slot.__dict__       # AttributeError: 'SlotClass' object has no attribute '__dict__'
no_slot.__dict__


# %%
class Point3D:
    __slots__ = ('x', 'y', 'z')
    # __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'3D coordinates: ({self.x}, {self.y}, {self.z})'

def main():
    p1 = Point3D(1, 1, 1)
    p2 = Point3D(24, 27, 31)
    print(p1)   # 3D coordinates: (1, 1, 1)
    print(p2)   # 3D coordinates: (24, 27, 31)

    p1.v1 = 30
    # output: AttributeError: 'Point3D' object has no attribute 'v1'
    # output2: p1.v1 = 30

    print(p1.__dict__)
    # output: AttributeError: 'Point3D' object has no attribute '__dict__'
    # output2: {'x': 1, 'y': 1, 'z': 1, 'v1': 30}

if __name__ == "__main__":
    main()


# %%
import gc

gc.set_threshold(3)

a = 'alpha'
b = 'bravo'
c = 'charlie'
d = 'delta'


# %%
del d

e = 'echo'
f = 'foxtrot'
g = 'golf'


# %%
import weakref

class Dummy(object):
     def __init__(self):
          self.data = list(range(int(1e8)))

dummy = Dummy()
temp = weakref.ref(dummy)
print(len(temp().data))
# 100000000

del dummy       
print(temp())
# None


# %%
