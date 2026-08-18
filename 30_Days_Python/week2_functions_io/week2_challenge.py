# Week 2 Challenge: CLI JSON Task Manager
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by implementing the functions.
# You can run 'python week2_challenge_test.py' to verify your solutions.

import json
import os

# ======================================================================
# JSON Task Manager Operations
# ======================================================================
# Your objective is to build a module that manages a checklist of tasks stored in
# a local JSON file. Each task is represented as a dictionary:
#   {'id': int, 'title': str, 'completed': bool}

# Task 1: Load Tasks
# ----------------------------------------------------------------------
# Complete the function 'load_tasks' that accepts a 'filepath' (str).
# 1. If the file does not exist, return an empty list: []
# 2. Otherwise, open the file in read mode, load the JSON content, and return
#    the list of tasks.
# 3. Handle potential ValueError/json.JSONDecodeError by returning [] if the file is corrupted.

def load_tasks(filepath):
    # TODO: Safely load tasks list from filepath. Return [] if empty/corrupted.
    pass


# Task 2: Save Tasks
# ----------------------------------------------------------------------
# Complete the function 'save_tasks' that accepts a 'filepath' (str) and a
# list of dictionaries 'tasks'.
# 1. Open the file in write mode and serialize the 'tasks' list into JSON.
# 2. Format the JSON with indent=4 to make it human-readable.

def save_tasks(filepath, tasks):
    # TODO: Write tasks list to filepath in JSON format
    pass


# Task 3: Add Task
# ----------------------------------------------------------------------
# Complete the function 'add_task' that accepts a list 'tasks' and a 'title' (str).
# 1. Generate a new task ID by setting it to: (length of current tasks list) + 1.
# 2. Create a new task dictionary: {'id': new_id, 'title': title, 'completed': False}
# 3. Append the new task to 'tasks'.
# 4. Return the modified 'tasks' list.

def add_task(tasks, title):
    # TODO: Create task dict, append to tasks list, and return tasks
    pass


# Task 4: Complete Task
# ----------------------------------------------------------------------
# Complete the function 'complete_task' that accepts a list 'tasks' and a
# 'task_id' (int).
# 1. Find the task in the 'tasks' list that has the matching 'id'.
# 2. Set that task's 'completed' status to True.
# 3. Return the modified 'tasks' list.
# 4. If the task ID is not found, return the list unmodified.

def complete_task(tasks, task_id):
    # TODO: Find task by id, toggle completed, and return tasks list
    pass
