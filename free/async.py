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