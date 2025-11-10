###########################
## Coroutine and Task 
###########################


# %%
import asyncio
import time 


# %%
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())

# output: 
# hello 
# world 


# %%

# coroutine 
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# # output: 
# started at 15:12:52
# hello
# world
# finished at 15:12:55


# %%

# task
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take around 2 seconds).
    await task1 
    await task2 

    print(f"finished at {time.strftime('%X')}")

# # output: 
# started at 15:20:32
# hello
# world
# finished at 15:20:34


# %%
import asyncio

async def nested():
    return 42

async def main():
    nested() # will raise a "RuntimeWarning".

    # wait
    print(await nested()) # "42"

asyncio.run(main())


# %%
async def nested():
    return 42

async def main():
    task = asyncio.create_task(nested())

    await task

asyncio.run(main())


# %%
async def main():
    await function_that_returns_a_future_object()

    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )


# %%
async def my_task():
    print("Task Start")
    
    try:
        await asyncio.sleep(5)
        print("Task Finish")
    except asyncio.CancelledError:
        print("Canceled Task")
        raise 

async def main():
    task = asyncio.create_task(my_task())
    await asyncio.sleep(1)
    task.cancel()

    try:
        await task 
    except asyncio.CancelledError:
        print("Except Task's canceled error in main function.")


asyncio.run(main())


# %%
from asyncio import TaskGroup 


class TerminateTaskGroup(Exception):
    """Exception for Terminate Task Group."""

async def force_terminate_task_grup():
    raise TerminateTaskGroup()

async def job(task_id, sleep_time):
    print(f"Task {task_id}: start")
    await asyncio.sleep(sleep_time)
    print(f"Task {task_id}: done")

async def main():
    try:
        async with TaskGroup() as group:
            group.create_task(job(1, 0.5))
            group.create_task(job(2, 1.5))

            await asyncio.sleep(1)

            group.create_task(force_terminate_task_grup())
    except TerminateTaskGroup:
        pass

asyncio.run(main())
# # output:
# Task 1: start
# Task 2: start
# Task 1: done


# %%
# Exception
 
import asyncio 

async def task1():
    await asyncio.sleep(1)
    raise ValueError("ValueError from task1")


async def task2():
    await asyncio.sleep(2)
    raise KeyError("KeyError from task2")


async def main():
    results = await asyncio.gather(task1(), task2(), return_exceptions=True)
    # results = await asyncio.gather(task1(), task2())

    for result in results:
        if isinstance(result, Exception):
            print(f"Caught exception: {result}")
        else:
            print(f"Task result: {result}")


asyncio.run(main())
# output: 
# Caught exception: ValueError from task1
# Caught exception: KeyError from task2


# %%
# ExceptionGroups

import asyncio
from exceptiongroup import ExceptionGroup # Python 3.11

async def task1():
    await asyncio.sleep(1)
    raise ValueError("ValueError from task1")


async def task2():
    await asyncio.sleep(2)
    raise KeyError("KeyError from task2")


async def main():
    # gathering all exceptions
    results = await asyncio.gather(task1(), task2(), return_exceptions=True)
    
    exceptions = [result for result in results if isinstance(result, Exception)]
    if exceptions:
        raise ExceptionGroup("Multiple exceptions occurred", exceptions)


try:
    asyncio.run(main())

except* ValueError as e:
    for sub_exception in e.exceptions:
        print(f"Caught ValueError: {sub_exception}")

except* KeyError as e:
    for sub_exception in e.exceptions:
        print(f"Caught KeyError: {sub_exception}")


# output: 
# Caught ValueError: ValueError from task1
# Cuahgt KeyError: KeyError from task2


# %%
from asyncio import TaskGroup 
import asyncio

async def task(n):
    if n % 2 == 0:
        await asyncio.sleep(0.1)
        raise ValueError(f"ValueError in task {n}")
    return f"Task {n} completed successfully"


async def main():
    try:
        results = []
        async with TaskGroup() as tg:
            for i in range(10):
                t = tg.create_task(task(i))
                results.append(t)
    
    except* ValueError as e:
        print(e.exceptions)

    for temp_task in results:
        if not temp_task.cancelled() and temp_task.exception() is None:
            print(temp_task.result())
        else:
            print(f"Task {temp_task.get_name()} did not complete successfully")


async def main2():
    tasks = [task(i) for i in range(4)]
    result = await asyncio.gather(*tasks, return_exceptions=True)
    print(result)


asyncio.run(main())
asyncio.run(main2())


# %%
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    L = await asyncio.gather(   # Coroutines will be wrapped in a future and scheduled in the event loop.
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)


asyncio.run(main())
# # output:
#     Task A: Compute factorial(2), currently i=2...
#     Task B: Compute factorial(3), currently i=2...
#     Task C: Compute factorial(4), currently i=2...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3), currently i=3...
#     Task C: Compute factorial(4), currently i=3...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4), currently i=4...
#     Task C: factorial(4) = 24
#     [2, 6, 24]


# %%
# sync case: one process, one thread
import requests
import time
import os
import threading


def fetch(url):
    print(f"ID: {os.getpid()} | Thread: {threading.get_ident()} | url: {url}")
    response = requests.get(url)
    return response.text

def main():
    urls = ["https://www.naver.com", "https://www.google.com", "https://daum.net"] * 10
    for url in urls:
        fetch(url)

if __name__ == "__main__":
    start = time.time()
    main()
    print("elapsed-time: ", time.time() - start)

# # output: 
# elapsed-time:  7.926071882247925


# %%
# async case: aiohttp(not requests)
import aiohttp
import asyncio
import time
import os
import threading


async def fetch(session, url):
    print(f"PID: {os.getpid()} | Thread: {threading.get_ident()} | url: {url}")
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://www.naver.com", "https://www.google.com", "https://daum.net"] * 10

    async with aiohttp.ClientSession() as session:
        _ = await asyncio.gather(*[fetch(session, url) for url in urls])

if __name__ == "__name__":
    start = time.time()
    asyncio.run(main())
    print("elapsed-time: ", time.time() - start)

# # output: 
# elapsed-time: 0.53


# %%
# one process, one threading
import os
import threading 
import time


def calculate(n):
    print(f"{os.getpid()} process | {threading.get_ident()} thread | n: {n}")
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += i * j * k
    return total

def main(nums):
    results = [calculate(num) for num in nums]
    print(results)

if __name__ == "__main__":
    start = time.time()
    main([300] * 10)
    print("elapsed-time: ", time.time() - start)

# # output: 
# elapsed-time:  9.546371221542358


# %%
# multi-thread: concurrent
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def calculate(n):
    print(f"{os.getpid()} process | {threading.get_ident()} thraed | n: {n}")
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += i * j * k
    return total

def main(nums):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(calculate, nums))
        print(results)

if __name__ == "__main__":
    start = time.time()
    main([300] * 10)
    print("elapsed-time: ", time.time() - start)

# # output: 
# elapsed-time:  9.263675212860107


# %%
# multi-processing: concurrent
import os
import threading
import time
from concurrent.futures import ProcessPoolExecutor


def calculate(n):
    print(f"{os.getpid()} process | {threading.get_ident()} thread | n: {n}")
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += i * j * k
    return total

def main(nums):
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(calculate, nums))
        print(results)

if __name__ == "__main__":
    import multiprocessing 
    multiprocessing.freeze_support()    

    start = time.time()
    main([50] * 4)
    print("elapsed-time: ", time.time() - start)

# # output: 
# BrokenProcessPool: A process in the process pool was terminated abruptly while the future was running or pending.


# %%