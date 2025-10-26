class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency
    
    def _update_db(self):
        # update database's records
        print("update the database")
    
    def update_urgency(self, urgency):
        self.urgency = urgency
        self.update_db()

if __name__ == "__main__":
    task = Task("Laundry", 3)
    task.update_urgency(4)

# # output: 
# Traceback (most recent call last):
#   File "pyrepo\how_to_python\task_test.py", line 16, in <module>
#     task.update_urgency(4)
#   File "pyrepo\how_to_python\task_test.py", line 12, in update_urgency
#     self.update_db()
# AttributeError: 'Task' object has no attribute 'update_db'