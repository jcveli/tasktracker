# Task Tracker CLI 

A simple command-line interface (CLI) application for tracking tasks. This tool allows users to add, view, update, and delete tasks directly from the terminal.
Done for educational purpose for [roadmap.sh activity](https://roadmap.sh/projects/task-tracker).

Program works on a continous loop until user chooses to exit by typing "q" or "quit" in the terminal.


In the terminal, run the following command to clone the repository:
```
git clone https://github.com/jeraldv/tasktracker.git
python main.py
```
Terminal will look like this:
```
Task Tracker. Available tasks: add, update, delete, mark-in-progress, mark-done, list. Type Q or Quit to exit.
```

Following actions are:
- Add a task
- Update a task
- Delete a task
- Mark a task as in-progress
- Mark a task as done
- List all tasks

```
add "task name" - Adds a new task with the specified name.
update "task id" "new task name" - Updates the name of the task with the specified ID.
delete "task id" - Deletes the task with the specified ID.
mark-in-progress "task id" - Marks the task with the specified ID as in-progress.
mark-done "task id" - Marks the task with the specified ID as done.
list - Lists all tasks.     
    - can also filter tasks by status using the following commands:
        - list all - Lists all tasks.
        - list in-progress - Lists only tasks that are in progress.
        - list done - Lists only tasks that are done.   
```

Also added tests for the above actions using unittest module.

Worked with PyCharm IDE. 


