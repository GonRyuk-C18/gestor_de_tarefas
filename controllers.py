#Lógica de negócio (criação, edição, ordenação, etc.)#

from models import Task
from database import add_task, get_all_tasks as db_get_all_tasks, get_task as db_get_task, update_task,update_task_status, delete_task as db_delete_task
from datetime import datetime

tasks = []

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
def create_task(conection, title, description, due_date, priority):
    task = Task(title, description, due_date, priority)
    # tasks.append(task)
    task_id = add_task(conection,task)
    task.id = task_id
    return task

def get_all_tasks():
    return tasks

def get_all_tasks_db(conection, order_by):
    return db_get_all_tasks(conection, order_by)

def get_task_db(conection,task_id):
    return db_get_task(conection,task_id)

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

def change_task_db(conection, task_id, new_title=None, new_description=None, new_due_date=None, new_priority=None, new_status=None):
    return update_task(conection, task_id, new_title, new_description, new_due_date, new_priority, new_status)

def update_task_status_db(conection,task_id,new_status):
    tasks1 = get_all_tasks_db(conection)

    for taskx in tasks1:
        if taskx['id'] == task_id:
            return update_task_status(conection, task_id, new_status)

    return None
    #return update_task_status(conection,task_id,new_status)
def delete_task(task_index):
    if task_index <0 or task_index >= len(tasks):
        return  False
    del tasks[task_index]
    return True

def delete_task_db(conection, task_id):
    return db_delete_task(conection, task_id)
