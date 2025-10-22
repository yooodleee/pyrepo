########################################
## Logging
########################################


# %%
import logging

logger_not_good = logging.Logger("task_app")


# %%
logger_good = logging.getLogger("task_app")


# %%
logger0 = logging.Logger("task_app")
logger1 = logging.Logger("task_app")
logger2 = logging.Logger("task_app")

assert logger0 is not logger1 and logger2


# %%
# default case: print
class Task:
    def __init__(self, title):
        self.title = title
    
    def remove_from_db(self):
        task_removed = True
        return task_removed

task = Task("Laundry")
if task.remove_from_db():
    print(f"removed the task {task.title} from the databsae")

# output: removed the task Laundry from the database


# %%
# case: add a file handler to logger
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("taskier.log")   # file handler
logger.addHandler(file_handler)     # add a handler to logger


# %%
# write a record to log file
task = Task("Laundry")
if task.remove_from_db():
    logger.warning(f"removed the task {task.title} from the database")


# %%
# check a log content
def chceck_log_content(filename):
    with open(filename) as file:
        return file.read()

log_records = chceck_log_content("taskier.log")
print(log_records)
# output: 
# removed the task Laundry from the database


# %%
# stream handler
stream_handler = logging.StreamHandler()

logger.addHandler(stream_handler)

logger.warning("Just a random warning event.")
# output: Just a random warning event.


# %%
log_records = chceck_log_content("taskier.log")

print(log_records)
# # output: 
# removed the task Laundry from the database
# Just a random warning event.


# %%
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

print(logger.level, logging._levelToName[logger.level])
# output: 30 WARNING


# %%
def logging_messages_all_levels():
    logger.critical("--Critical message")
    logger.error("--Error message")
    logger.warning("--Warning message")
    logger.info("--Info message")
    logger.debug("--Debug message")

logging_messages_all_levels()

log_records = chceck_log_content("taskier.log")
print(log_records)
# # output: 
# --Critical message
# --Error message
# --Warning message
# removed the task Laundry from the database
# Just a random warning event.
# --Critical message
# --Error message
# --Warning message


# %%
# set different log levels
logger.setLevel(logging.DEBUG)      # set logger's log level to a DEBUG

handler_warning = logging.FileHandler("taskier_warning.log")
handler_warning.setLevel(logging.WARNING)   # set handler's log level to a WARNING

logger.addHandler(handler_warning)
handler_critical = logging.FileHandler("taskier_critical.log")  
handler_critical.setLevel(logging.CRITICAL) # set handler's log level to a CRITICAL

logger.addHandler(handler_critical)

logging_messages_all_levels()

warning_log_records = chceck_log_content("taskier_warning.log")
print(warning_log_records)
# # output: 
# --Critical message
# --Error message
# --Warning message

critical_log_records = chceck_log_content("taskier_critical.log")
print(critical_log_records)
# # output: 
# --Critical message


# %%
# set log record formatter to a stream handler
import logging

logger = logging.getLogger(__name__)    # search logger and set a log level
logger.setLevel(logging.DEBUG)

logger.handlers = []        

# set formatter
formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def log_some_records():
    logger.info("App is starting")
    logger.error("Failed to save the task to the db")
    logger.info("Created a task by the user")
    logger.critical("Can't update the status of the task")


log_some_records()
# # output: 
# 2025-10-22 13:38:12,973 [INFO] - __main__ App is starting
# 2025-10-22 13:38:12,973 [ERROR] - __main__ Failed to save the task to the db
# 2025-10-22 13:38:12,973 [INFO] - __main__ Created a task by the user
# 2025-10-22 13:38:12,975 [CRITICAL] - __main__ Can't update the status of the task


# %%
