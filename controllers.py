#Lógica de negócio (criação, edição, ordenação, etc.)#

from models import Task

tasks = []

def create_task(title, description, due_date, priority):
    task = Task(title, description, due_date, priority)
    tasks.append(task)
    return task

def get_all_tasks():
    return tasks

def change_task(task_index, new_title=None, new_description=None, new_due_date=None, new_priority=None, new_status=None):
    if task_index <0 or task_index >= len(tasks):
        return None
    task = tasks[task_index]
    if new_title is not None:
        task.title = new_title
    if new_description is not None:
        task.description = new_description
    if new_due_date is not None:
        task.due_date = new_due_date
    if new_priority is not None:
        task.priority = new_priority
    if new_status is not None:
        task.status = new_status

    return task

def delete_task(task_index):
    if task_index <0 or task_index >= len(tasks):
        return  False
    del tasks[task_index]
    return True